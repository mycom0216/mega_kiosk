import pickle
import getpass # 관리자 비밀번호 입력시 미출력
from datetime import datetime

# 초기화면에서 메뉴 선택 / 관리자 기능 분류
def displayInfo(info):
    order_in = ""
    mode = 0
    flag_input = True
    
    print("=" * printcnt)
    print(info)
    print("-" * printcnt)
    
    while (flag_input):
        order_in = input("주문하기(Yes - y/No - n)\nSelect : ")
    
        if (order_in == "y"):
            # mode = 1
            #결제 완료 테스트 목적의 기능 변경
            # mode = 5
            mode = 3
        elif (order_in == "/admin"):
            mode = 6
        elif (order_in == "n"):
            mode = 0
            print("감사합니다.\n안녕히 가세요")
        else : 
            print("다시 시도하세요")
        flag_input = False
    return mode

# 메뉴 화면에서 메뉴 기틀이 되는 함수
def menuMain():
    cate_in = ""
    categorys = []
    
    for menu in menus:
        if menu["category"] not in categorys:
            categorys.append(menu["category"])
            
    print("=" * printcnt)
    print("메뉴 주문")
    print("-" * printcnt)
    idx = 1
    for cate in categorys:
        print(f"{idx}. {cate}",end="\t")
        idx += 1
    print()
    print("-" * printcnt)
    print("장바구니(/cart) / 주문 취소(/cancel)")
    cate_in = input("카테고리를 선택해주세요\n선택 : ")
    
    if (cate_in.isdigit() and (0 < int(cate_in) < len(categorys) + 1)):
        select_cate = int(cate_in)-1
        categoryMenuSelect(categorys[select_cate])
    elif (cate_in == "/cancel"):
        orders["menu"] = {}
    else : 
        pass
        
    print("=" * printcnt)

#메뉴 화면에서 카테고리별 메뉴 선택 기능
def categoryMenuSelect(cate):
    menu_in = ""
    quan_in = ""
    menu_num = 0
    quan_num = 0
    cate_code = ""
    
    for k, v in category_code.items():
        if v == cate:
            cate_code = k
    
    idx = 1
    for menu in menus:
        if menu["category"] == cate:
            menu_nm = menu['menu']
            stock = menu["stock"]
            price = int(menu['price'])
            desc = menu['description']
            stat = "🔴 품절" if stock == 0 else "🟢 판매중"
            
            print(f"{idx}. {menu_nm} : {desc}")
            print(f"재고 : {stat} {stock}, 가격 : {price}")
            print("---------------------------")
            idx += 1
    
    menu_in = input("메뉴를 선택해주세요\n선택 : ")
    quan_in = input("메뉴 수량을 입력해주세요\n선택 : ")
    
    if (menu_in.isdigit() and quan_in.isdigit() and
        (0 < int(menu_in) < idx) and (0 < int(quan_in) < 999)):
        menu_cd = ""
        menu_num = int(menu_in)
        quan_num = int(quan_in)
        menu_cd = cate_code + menu_in
        
        if menu_cd in list(orders["menu"]):
            orders["menu"][menu_cd] += quan_num
        else : 
            orders["menu"][menu_cd] = quan_num
        
        print(orders)
    elif ():
        pass
    else :
        pass

# 초기 화면에서 관리자 기능 진입시 관리자 인증 기능
def adminCheck(pwd):
    admin_pwd = ""
    
    # 기준 입력 방식의 보안이 문제가 있다 판단하여 보유 내장 모듈에서 출력 안되게 사용
    print("=" * printcnt)
    print("관리자 기능")
    print("=" * printcnt)
    admin_pwd = getpass.getpass("관리자 비밀번호 입력 : ")
    if (admin_pwd == pwd):
        print("관리자임을 확인했습니다.")
        return True
    else :
        print("비밀번호가 틀립니다.")
        return False

# 광고화면(최초화면) 수정 기능
def adminInfoChange(info):
    info_in = ""
    change_data = "안녕하세요.\n메가커피 광주 소촌점입니다."
    upd_in = ""
    
    print("-" * printcnt)
    print (f"현재 : {info}")
    print("-" * printcnt) 
    
    info_in = input("수정하시겠습니까?\n(yes-y/no-n)")
    
    if (info_in == "y"):
        print("-" * printcnt) 
        upd_in = input("수정\n 입력 : ")
        
        if (len(upd_in) != 0):            
            change_data = upd_in
        
        return change_data

# 관리자 기능 목록 출력 함수
def adminHeadPrint(mode_list):
    print("=" * printcnt)
    print("관리자 기능 목록")
    print("=" * printcnt)
    
    idx = 1
    for menu_nm in mode_list:
        print(f"{idx}. {menu_nm}")
        idx += 1 

# 데이터 관리를 파일(pickle)로 하여 데이터 읽고 해당 데이터 반환 하는 함수
def fileDataReturn(pos):
    file_data = ""
    # load admin password data
    with open(pos, 'rb') as fr:
        file_data = pickle.load(fr)
    
    return file_data

# 데이터 관리를 목적으로 파일을 쓰는 함수
def fileDataWrite(pos, data):
    with open(pos, 'wb') as fw:
        pickle.dump(data, fw)

# 메뉴가 공통적으로 출력됨에 따라 세로형 출력 함수
def printMenus(list):
    idx = 0
    for menu in list:
        print(f"{idx + 1}. {menu}")
        idx += 1

# 결제 기능 기틀 함수
def paymentMain(orders, payment_menu_list, discount_list, payment_list):
    menu_mode = 0
    menu_in = ""
    menu_num = 0
    flag_payment = True
    
    while (flag_payment) : 
        print("=" * printcnt)
        print("결제")
        print("=" * printcnt)
        
        printMenus(payment_menu_list)
        
        menu_in = input("결제 메뉴를 선택해주세요.\n선택 : ")
        if (menu_in.isdigit() and (0 < int(menu_in) < len(payment_menu_list)+1)):
            menu_num = int(menu_in)
            
            if (menu_num == 1):
                # "할인"
                orders["coupon"] = discountMain(discount_list)
                menu_mode = 3
            elif (menu_num == 2):
                # "결제 수단"
                temp_dict = {}
                temp_dict = mileageMain(payment_list)
                if temp_dict["method"] == "mileage":
                    orders["mileage"] = temp_dict
                elif temp_dict["method"] == "cash":
                    orders["payment"] = temp_dict
                menu_mode = 3
            elif (menu_num == 3):
                # "장바구니"
                menu_mode = 2
                flag_payment = False
            elif (menu_num == 4):
                # "주문취소"
                menu_mode = 99
                flag_payment = False
            elif (menu_num == 5):
                # "결제 "
                menu_mode = 4
                flag_payment = False
        else : 
            print("다시 선택해 주세요")
            
        return menu_mode

# 마일리지 기능 기틀 함수
def mileageMain(pay_list):
    payment_in = ""
    payment_num = 0
    user_payment = {}

    print("=" * printcnt)
    print("결제 - 할인 선택")
    print("=" * printcnt)
    printMenus(pay_list)
    
    payment_in = input ("결제 수단을 선택해주세요\n선택 : ")
    print("=" * printcnt)
    if (payment_in.isdigit() and (0 < int(payment_in) <= len(pay_list)+1)):
        payment_num = int(payment_in)
        
        #마일리지 선택
        if (payment_num == 16):
            print(f"{pay_list[payment_num - 1]}을 선택하셨습니다.")
            print("=" * printcnt)
            flag_cash = True
            
            while flag_cash:    
                cash_in = input("입금해주세요\n금액 : ")
                if (cash_in.isdigit()):
                    user_payment["method"] = "cash"
                    user_payment["cash"] = int(cash_in)
                    flag_cash = False
                    
                    return user_payment
                else :
                    print("재 입금해주세요")
        elif (payment_num == 17):
            phone_num = ""
            print(f"{pay_list[payment_num - 1]}을 선택하셨습니다.")
            print("=" * printcnt)
            
            mileage_in = input("핸드폰 번호를 입력해주세요\n선택 : ")
            if ("-" in mileage_in):
                phone_num = mileage_in.replace("-")
            else : 
                phone_num = mileage_in
                
            for user in list(users):
                print(phone_num , user["phone_num"])
                if phone_num == user["phone_num"]:
                    user_payment = user
                    user_payment["method"] = "mileage"
                # else :
                #     print("신규 고객님 반갑습니다.")
                #     now = datetime.now()
                #     date_str = now.strftime("%Y-%m-%d %H:%M")
                    
                #     user_payment["method"] = "mileage"
                #     user_payment["phone_num"] = phone_num
                #     user_payment["grade"] = "user"
                #     user_payment["mileage"] = 0
                #     user_payment["visit_num"] = 0
                #     user_payment["last_day"] = date_str
                    
                #     return user_payment
        else : 
            print("시스템 오류로 수리 중입니다.")
            return None
        return user_payment
    else : 
        print("재 선택해주세요.")

# 결제에서 할인 관련 기틀 함수    
def discountMain(discnt_list):
    discnt_in = ""
    discnt_num = 0
    use_coupon = ""
    flag_discount = True
    
    print("=" * printcnt)
    print("결제 - 할인 선택")
    print("=" * printcnt)
    
    while (flag_discount):
        printMenus(discnt_list)
        print("-" * printcnt)
        discnt_in = input("할인 수단을 선택해주세요\n선택 : ")
        if (discnt_in.isdigit() and (0 < int(discnt_in) <= len(discnt_list))):
            discnt_num = int(discnt_in)
            
            if discnt_num == 6:
                print(f"{discnt_list[discnt_num-1]}을 선택하셨습니다.")
                cpn_in = input("쿠폰 코드를 입력하세요\n입력 : ")
                print(coupons)
                if not(cpn_in.isdigit()):
                    for cpn in list(coupons) :
                        if cpn_in == cpn["code"] and (bool(cpn["used"]) == False):
                                print("쿠폰이 확인되었습니다.")
                                use_coupon = cpn
                                flag_discount = False
                else : 
                    print("잘못된 쿠폰입니다.")
            else : 
                print("시스템 오류로 수리 중입니다.")
                use_coupon = None
        else : 
            print("재 선택해주세요.")
        print("-" * printcnt)
            
    return use_coupon


printcnt = 80
dir_name = "./data/"
file_menu_name = "mega.pik"
file_info_name = "mega_info.pik"
file_admin_name = "admin.pik"
file_coupon_name = "coupon.pik"
file_user_name = "user.pik"
admin_pwd = ""
info_data = ""
main_flag = True
mode_stat = 0
menus = {}
coupons = {}
user = {}
orders = {"menu":"", "coupon":"", "payment":"","mileage":""}
mode = ("광고", "메뉴", "장바구니", "결제", "마일리지","결제 완료")
admin_mode = ("광고 화면 관리", "메뉴 품절 관리", "신 메뉴 관리", "관리 모드 종료", "프로그램 관리")
payment_menu = ("할인", "결제 수단", "장바구니", "주문 취소", "결제")
discount_list = ("KT VIP", "T 멤버쉽", "CJ One", "Kia Memebers", "T 우주(SKT)", "메가 쿠폰")
payment_list = ("카드 결제", "앱 카드", "카카오 페이", "페이코", "네이버 페이", "제로페이 페이북", "하나 페이", "KB 페이", "신한 SOL 페이", "당근페이", "알리 페이", "모바일 상품권", "메가 선불 카드", "CJ 기프트 카드", "현대 M 포인트 카드", "현금", "마일리지")
category_code = {"c":"커피",
                 "t":"티",
                 "a":"에이드",
                 "s":"스무디",
                 "d":"디카페인",
                 "n":"논 커피"}

# load Data 
menus = fileDataReturn(dir_name + file_menu_name)
admin_pwd = fileDataReturn(dir_name + file_admin_name)
info_data = fileDataReturn(dir_name + file_info_name)
coupons = fileDataReturn(dir_name + file_coupon_name)
users =  fileDataReturn(dir_name + file_user_name)

# test Data
orders["menu"] = {"c9": 2,"a3" : 2,"s3" : 1}

# Main code
while(main_flag):
    if (mode_stat == 0):
        #광고 화면
        mode_stat = displayInfo(info_data)
    elif (mode_stat == 1):
        menuMain()
        
    elif (mode_stat == 2):
        print("장바구니", mode_stat)
        input()
    elif (mode_stat == 3):
        stat = paymentMain(orders, payment_menu, discount_list, payment_list)
        # 결제
        
        # 주문 취소의 경우 초기화 필요 작업        
        if (stat == 99):
            orders = {"menu":"", "coupon":"", "payment":"","mileage":""}
            mode_stat = 0
        else : 
            mode_stat = stat
    elif (mode_stat == 4):
        print("마일리지", mode_stat)
        input()
    elif (mode_stat == 5):
        #"결제 완료"
        print("=" * printcnt)
        print("결제 완료")
        print("=" * printcnt)
        
        total = 0
        
        for menu in list(menus):
            for k, v in orders["menu"].items():
                if (menu["menu_code"] == k):
                    total += (v * int(menu["price"]))
                    print(f"{menu["menu"]:<25}, {v}, {menu["price"]}, {v * int(menu["price"])}")
        
        print("=" * printcnt)
        print (f"Total is {total:>10}")
        print("-" * printcnt)
        print("=" * printcnt)
        input("test")
    elif (mode_stat == 6 and adminCheck(admin_pwd)):
        # 관리자 모드
        admin_flag = True

        while (admin_flag):
            admin_in = ""
            admin_in_num = 0
            info_temp = ""
                
            adminHeadPrint(admin_mode)
                
            print("-" * printcnt)
            admin_in = input(f"관리 항목 선택 (1 ~ {len(admin_mode)}): ")
            if (admin_in.isdigit()):
                admin_in_num = int(admin_in)
                
                #광고 화면 관리
                if (admin_in_num == 1):
                    info_temp = adminInfoChange(info_data)
                    if (info_temp is not None):
                        info_data = info_temp
                        #save Data
                        fileDataWrite(dir_name + file_info_name, info_temp)
                #메뉴 품절 관리
                elif (admin_in_num == 2):
                    pass
                #신 메뉴 관리
                elif (admin_in_num == 3):
                    pass
                #관리 모드 종료
                elif (admin_in_num == 4):
                    mode_stat = 0
                    admin_flag = False
                    print("관리 모드를 중지합니다.")
                #프로그램 종료
                elif (admin_in_num == 5):
                    main_flag = False
                    admin_flag = False
                    print("프로그램을 종료합니다.")
            else :
                print("재선택하세요")
            print("-" * printcnt)
