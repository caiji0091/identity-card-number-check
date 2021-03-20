#!/usr/bin/env python
# -- coding: utf-8 --
# @Time    : 2021/3/20 11:59
# @Author  : caiji


def ch_code(data):
    ch = 0
    # 算法参考GB 11643-1999
    cof = list("79058421637905842")  # 系数coefficient
    for i in range(17):
        cof1 = int(cof[i])
        if cof[i] == '0':
            cof1 = 10
        ch = ch + int(data[i]) * cof1
    ch = ch % 11    # 算出第一步校验码
    ch_dict = list("10X98765432")  # 校验码字典查询，其实就是顺序换一下
    return ch_dict[ch]


if __name__ == '__main__':
    opt = input("请输入身份证前17位予以校验：")
    if len(opt) == 17:
        print("校验码为：", ch_code(opt))
    else:
        print("请检查身份证位数是否正确！")
