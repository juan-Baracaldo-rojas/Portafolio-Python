# inventory.py
import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
# displayInventory(stuff)

def createDict(lista):
    dic={}
    for item in lista:
        dic.setdefault(item,0)
        dic[item]=dic[item]+1
    return dic

def addToInventory(inventory, addedItems):
    dicItems=createDict(addedItems)
    for k,v in dicItems.items():
        for item in inventory.keys():
            if k == item:
                inventory[k]=inventory[k]+v
        print('key {} - value {}'.format(k,v))
        inventory.setdefault(k,v)
        pprint.pprint(inventory)
    return inventory
    
print('inventory sin loot \n')
displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff=addToInventory(stuff,dragonLoot)
print('inventory con loot \n')
displayInventory(stuff)