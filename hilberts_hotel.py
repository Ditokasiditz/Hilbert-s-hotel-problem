import time
import sys
from typing import List, Dict, Set


class HilbertHotel:
    def __init__(self):
        self.rooms: Dict[int, str] = {}  # หมายเลขห้อง: ช่องทางที่มา
        self.channels: Dict[str, Set[int]] = {
            "A": set(),
            "B": set(),
            "C": set(),
            "D": set(),
        }
        self.max_room: int = 0

    def calculate_room_number(self, channel: str, guest_number: int) -> int:
        channel_index = ord(channel) - ord("A")
        return 4 * guest_number + channel_index + 1

    def add_guests(self, channel: str, count: int):
        start_time = time.time()
        for i in range(count):
            room_number = self.calculate_room_number(
                channel, len(self.channels[channel])
            )
            self.rooms[room_number] = channel
            self.channels[channel].add(room_number)
            self.max_room = max(self.max_room, room_number)
        end_time = time.time()
        print(
            f"เพิ่มแขก {count} คนในช่องทาง {channel} ใช้เวลา {end_time - start_time:.6f} วินาที"
        )
        self.print_summary()

    def add_room_manual(self, room_number: int, channel: str):
        start_time = time.time()
        if room_number in self.rooms:
            print(f"ห้อง {room_number} มีแขกพักอยู่แล้ว")
        else:
            self.rooms[room_number] = channel
            self.channels[channel].add(room_number)
            self.max_room = max(self.max_room, room_number)
            print(f"เพิ่มห้อง {room_number} ในช่องทาง {channel} สำเร็จ")
        end_time = time.time()
        print(f"เพิ่มห้องแบบ manual ใช้เวลา {end_time - start_time:.6f} วินาที")
        self.print_summary()

    def remove_room_manual(self, room_number: int):
        start_time = time.time()
        if room_number in self.rooms:
            channel = self.rooms[room_number]
            del self.rooms[room_number]
            self.channels[channel].remove(room_number)
            if room_number == self.max_room:
                self.max_room = max(self.rooms.keys()) if self.rooms else 0
            print(f"ลบห้อง {room_number} สำเร็จ")
        else:
            print(f"ไม่พบห้อง {room_number}")
        end_time = time.time()
        print(f"ลบห้องแบบ manual ใช้เวลา {end_time - start_time:.6f} วินาที")
        self.print_summary()

    def sort_rooms(self):
        start_time = time.time()
        sorted_rooms = sorted(self.rooms.items())
        end_time = time.time()
        print(f"จัดเรียงห้องใช้เวลา {end_time - start_time:.6f} วินาที")
        print("ห้องที่จัดเรียงแล้ว:", sorted_rooms)
        return sorted_rooms

    def search_room(self, room_number: int):
        start_time = time.time()
        result = self.rooms.get(room_number, "ไม่พบห้อง")
        end_time = time.time()
        print(f"ค้นหาห้อง {room_number} ใช้เวลา {end_time - start_time:.6f} วินาที")
        print(f"ผลการค้นหา: {result}")
        return result

    def count_empty_rooms(self):
        start_time = time.time()
        empty_count = self.max_room - len(self.rooms)
        end_time = time.time()
        print(f"นับจำนวนห้องว่างใช้เวลา {end_time - start_time:.6f} วินาที")
        print(f"จำนวนห้องว่าง: {empty_count}")
        return empty_count

    def write_to_file(self, filename: str):
        start_time = time.time()
        with open(filename, "w") as f:
            for room, channel in sorted(self.rooms.items()):
                f.write(f"ห้อง {room}: ช่องทาง {channel}\n")
        end_time = time.time()
        print(f"เขียนไฟล์ใช้เวลา {end_time - start_time:.6f} วินาที")
        print(f"ข้อมูลถูกเขียนลงในไฟล์ {filename}")

    def memory_usage(self):
        memory = sys.getsizeof(self.rooms) + sys.getsizeof(self.channels)
        print(f"การใช้หน่วยความจำ: {memory} bytes")
        return memory

    def print_summary(self):
        print("\n=== สรุปสถานะโรงแรม ===")
        print(f"จำนวนห้องทั้งหมดที่มีแขก: {len(self.rooms)}")
        print(f"หมายเลขห้องสูงสุด: {self.max_room}")
        for channel, rooms in self.channels.items():
            print(f"ช่องทาง {channel}: {len(rooms)} ห้อง")
        print(f"จำนวนห้องว่าง: {self.max_room - len(self.rooms)}")
        print("========================\n")


def main():
    hotel = HilbertHotel()

    while True:
        print("\n1. เพิ่มแขก")
        print("2. เพิ่มห้องแบบ manual")
        print("3. ลบห้องแบบ manual")
        print("4. จัดเรียงห้อง")
        print("5. ค้นหาห้อง")
        print("6. นับจำนวนห้องว่าง")
        print("7. เขียนข้อมูลลงไฟล์")
        print("8. แสดงการใช้หน่วยความจำ")
        print("9. ออกจากโปรแกรม")

        choice = input("เลือกการทำงาน: ")

        if choice == "1":
            channel = input("ใส่ช่องทาง (A/B/C/D): ")
            count = int(input("ใส่จำนวนแขก: "))
            hotel.add_guests(channel, count)
        elif choice == "2":
            room = int(input("ใส่หมายเลขห้อง: "))
            channel = input("ใส่ช่องทาง (A/B/C/D): ")
            hotel.add_room_manual(room, channel)
        elif choice == "3":
            room = int(input("ใส่หมายเลขห้องที่ต้องการลบ: "))
            hotel.remove_room_manual(room)
        elif choice == "4":
            hotel.sort_rooms()
        elif choice == "5":
            room = int(input("ใส่หมายเลขห้องที่ต้องการค้นหา: "))
            hotel.search_room(room)
        elif choice == "6":
            hotel.count_empty_rooms()
        elif choice == "7":
            filename = input("ใส่ชื่อไฟล์: ")
            hotel.write_to_file(filename)
        elif choice == "8":
            hotel.memory_usage()
        elif choice == "9":
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง")


if __name__ == "__main__":
    main()
