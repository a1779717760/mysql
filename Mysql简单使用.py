from pymysql import *
import pprint

class STUDENT(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', password='root', database='python_test',
                       charset='utf8')
        self.cs1 = self.conn.cursor()

    def __del__(self):
        self.cs1.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cs1.execute(sql)
        for temp in self.cs1.fetchall():
            pprint.pprint(temp)

    def show_all_name(self):
        sql = 'select name from student;'
        self.execute_sql(sql)

    def show_all_age(self):
        sql = 'select age from student;'
        self.execute_sql(sql)

    def show_all_height(self):
        sql = 'select height from student;'
        self.execute_sql(sql)

    def print_menu(self):
        print("------hello------")
        print('1.所以名字')
        print('2.所有年龄')
        print('3.所有身高')
        num = input('请输入功能对应序号:')
        return num

    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                self.show_all_name()
            elif num == '2':
                self.show_all_age()
            elif num == '3':
                self.show_all_height()
            else:
                print("输入有误")

def main():
    student = STUDENT()
    student.run()

if __name__ == '__main__':
    main()