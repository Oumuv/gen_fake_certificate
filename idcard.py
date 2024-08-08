from PIL import Image, ImageDraw, ImageFont
import random
from utils.idcard_entity import *


def generate_id_card(idcard_info):
    idcard_save_dir = "res/"

    # 身份证信息
    name = idcard_info.get_name()
    gender = idcard_info.get_gender()
    nation = idcard_info.get_nation()
    year = str(idcard_info.get_birth_year())
    mon = str(idcard_info.get_birth_month())
    day = str(idcard_info.get_birth_day())
    org = idcard_info.get_province_name() + idcard_info.get_city_name() + '公安局'
    valid_start = year + '.'
    valid_start = valid_start + '0' + mon if len(mon) == 1 else valid_start + mon
    valid_start = valid_start + '.0' + day if len(day) == 1 else valid_start + "." + day
    valid_end = str(int(year) + 50) + valid_start[4:]
    valid_range = valid_start + '-' + valid_end
    addr = idcard_info.get_addr()
    idn = idcard_info.get_id()

    # 设置字体样式
    name_font = ImageFont.truetype('resource/font/hei.ttf', 20)
    other_font = ImageFont.truetype('resource/font/hei.ttf', 20)
    bdate_font = ImageFont.truetype('resource/font/fzhei.ttf', 20)
    id_font = ImageFont.truetype('resource/font/ocrb10bt.ttf', 21)

    # 创建一个空白的身份证模板图片
    front = Image.open("resource/bkimg/male.png" if gender == "男" else "resource/bkimg/woman.png")  # 正面
    draw = ImageDraw.Draw(front)
    # 在模板上添加个人信息
    draw.text((90, 34), name, fill=(0, 0, 0), font=name_font)
    draw.text((90, 78), gender, fill=(0, 0, 0), font=other_font)
    draw.text((210, 78), nation, fill=(0, 0, 0), font=other_font)
    draw.text((90, 120), year, fill=(0, 0, 0), font=bdate_font)
    draw.text((180, 120), mon, fill=(0, 0, 0), font=bdate_font)
    draw.text((230, 120), day, fill=(0, 0, 0), font=bdate_font)

    start = 0
    loc = 167
    while start + 11 < len(addr):
        draw.text((90, loc), addr[start:start + 11], fill=(0, 0, 0), font=other_font)
        start += 11
        loc += 22
    draw.text((90, loc), addr[start:], fill=(0, 0, 0), font=other_font)
    draw.text((180, 280), idn, fill=(0, 0, 0), font=id_font)




    # 保存生成的身份证图片
    output_filename = f"{name}_id_card_front.png"
    front.save(idcard_save_dir + output_filename)


    # 背面信息
    back = Image.open("resource/bkimg/front.png")  # 背面
    drawback = ImageDraw.Draw(back)
    output_filename = f"{name}_id_card_back.png"

    drawback.text((220, 249), org, fill=(0, 0, 0), font=other_font)
    drawback.text((220, 290), valid_range, fill=(0, 0, 0), font=other_font)
    back.save(idcard_save_dir + output_filename)


if __name__ == "__main__":
    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    areaCode = "440101"
    id = generate_id(areaCode, random_sex)
    provinceName = "广东省"
    cityName = "广州市"
    addr = provinceName + cityName + "天河区园丁路41号"
    name = "张三"
    nation = "汉"
    idcard = IDCard(name, nation, addr, id, provinceName, cityName)

    generate_id_card(idcard)
