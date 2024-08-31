
#list
Menu_Noodle = ["เส้นเล็ก","เส้นใหญ่","บะหมี่","หมี่ขาว","วุ้นเส้น","มาม่า"]
Menu_Water = ["น้ำใส","น้ำตก","ต้มยำ","เย็นตาโฟ"]
Menu_Meat = ["หมู","วัว","ไก่","ลูกชิ้นหมู","ลูกชิ้นเนื้อ","ลูกชิ้นปลา","ตับ"]
Menu_Topping = ["กากหมู","แคปหมู","ไข่ออนเซน","ปลาเส้น","เกี๊ยวทอด","ไม่เอา"]
Menu_Size = ["ปกติ","พิเศษ"]
Menu_Ice = ["เอา","ไม่เอา"]
Menu_Drink = ["ชานม","ชาเขียว","โค้ก","น้ำเปล่า"]


#LOGO
print("         /   /   /      ")
print("        \   \   \       ")
print("        /   /   /       ")
print(" ::::::::::::::::::::::: ")
print("   :::::::::::::::::::   ")
print("     :::::::::::::::      ")
print("        =====         ")
print("\n")


#ต้อนรับ
print("ร้านก๋วยเตี๋ยวใจฟูสวัสดีครับ/ค่ะ")
print("รับอะไรดีครับ")
print("\n")


#สั่งอาหาร
print(Menu_Noodle)
Order_เส้น  = input("เส้นอะไรดี=")
while True:
  if Order_เส้น in Menu_Noodle:
    break
  print("ทางร้านไม่มีเส้นที่คุณสั่ง กรุณาสั่งใหม่")
  Order_เส้น = input("เส้นอะไรดี=")


print(Menu_Water)
Order_น้ำก๊วยเตี๋ยว  = input("น้ำก๊วยเตี๋ยวอะไรดี=")
while True:
  if Order_น้ำก๊วยเตี๋ยว in Menu_Water:
    break
  print("ทางร้านไม่มีน้ำก๋วยเตี๋ยวที่คุณสั่ง กรุณาสั่งใหม่")
  Order_น้ำก๊วยเตี๋ยว = input("น้ำก๊วยเตี๋ยวอะไรดี=")


print(Menu_Meat)
Order_เนื้อ  = input("เนื้ออะไรดี=")
while True:
  if Order_เนื้อ in Menu_Meat:
    break
  print("ทางร้านไม่มีเนื้อที่คุณสั่ง กรุณาสั่งใหม่")
  Order_เนื้อ = input("เนื้ออะไรดี=")


print(Menu_Topping)
Order_ท้อปปิ้ง  = input("รับเป็นท้อปปิ้งอะไรดีครับ/ค่ะ=")
while True:
  if Order_ท้อปปิ้ง == "ไม่เอา":
    Price_Topping = 0
    break
  if Order_ท้อปปิ้ง in Menu_Topping:
    if Order_ท้อปปิ้ง == "ไข่ออนเซน":
      Price_Topping = 10
    else:
      Price_Topping = 15
    break
  print("ทางร้านไม่มีท้อปปิ้งที่คุณสั่ง กรุณาสั่งใหม่")
  Order_ขนาด = input("รับเป็นท้อปปิ้งอะไรดีครับ/ค่ะ=")


print(Menu_Size)
Order_ขนาด  = input("รับเป็นพิเศษหรือปกติดีครับ/ค่ะ=")
while True:
  if Order_ขนาด in Menu_Size:
    if Order_ขนาด == "ปกติ":
      Price_Size = 40
    else:
      Price_Size = 50
    break
  print("ทางร้านไม่มีขนาดที่คุณสั่ง กรุณาสั่งใหม่")
  Order_ขนาด = input("รับเป็นพิเศษหรือปกติดีครับ/ค่ะ=")


print(Menu_Ice)
Order_น้ำแข็ง  = input("เอาน้ำแข็งไหมครับ/ค่ะ=")
while True:
  if Order_น้ำแข็ง in Menu_Ice:
    break
  print("ทางร้านไม่มีน้ำแข็งที่คุณสั่ง กรุณาสั่งใหม่")
  Order_น้ำแข็ง = input("เอาน้ำแข็งไหมครับ/ค่ะ=")


print(Menu_Drink)
Order_น้ำ  = input("เอาน้ำอะไรครับ/ค่ะ=")
while True:
  if Order_น้ำ in Menu_Drink:
    if Order_น้ำ == "น้ำเปล่า":
      Price_Drink = 10
    else:
      Price_Drink = 20
    break
  print("ทางร้านไม่มีน้ำที่คุณสั่ง กรุณาสั่งใหม่")
  Order_น้ำ = input("เอาน้ำอะไรครับ/ค่ะ=")

#สรุปรายการ
print("\n")
print("สรุปรายการที่สั่ง:")
print("เส้น: {}\nน้ำก๊วยเตี๋ยว: {}\nเนื้อ: {}\nท็อปปิ้ง: {}\nน้ำแข็ง: {}\nขนาด: {}\nเครื่องดื่ม: {}".format(
    Order_เส้น, Order_น้ำก๊วยเตี๋ยว, Order_เนื้อ, Order_ท้อปปิ้ง, Order_น้ำแข็ง, Order_ขนาด, Order_น้ำ))

#สรุปค่าอาหาร
total_price = Price_Size + Price_Drink + Price_Topping
print("ราคารวมทั้งหมด: {} บาท".format(total_price))
payment = float(input("กรุณาใส่จำนวนเงินที่ลูกค้าจ่าย: "))
change = payment - total_price
print("เงินทอน: {} บาท".format(change))
print("\n")
#จบ
print("Thank you for your order")
