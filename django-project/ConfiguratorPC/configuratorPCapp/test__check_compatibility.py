from random import randint
from SQLfunctions import getListFromTable
from check_compatibility import check_compatibility


basket = {
    'motherboard': getListFromTable('motherboard')[randint(len(getListFromTable('motherboard')-1))],
    'cpu': getListFromTable('cpu')[randint(len(getListFromTable('cpu')-1))],
    'gpu': getListFromTable('gpu')[randint(len(getListFromTable('gpu')-1))],
    'power_supply': getListFromTable('power_supply')[randint(len(getListFromTable('power_supply')-1))],
    'case': getListFromTable('case')[randint(len(getListFromTable('case') - 1))],
    'storage': getListFromTable('storage')[randint(len(getListFromTable('storage') - 1))],
    'ram': getListFromTable('ram')[randint(len(getListFromTable('ram') - 1))],
    'cooler': getListFromTable('cooler')[randint(len(getListFromTable('cooler') - 1))],
    'fan': getListFromTable('fan')[randint(len(getListFromTable('fan') - 1))],
}