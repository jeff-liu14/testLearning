class Hero:
    hero_hp = 100
    hero_power = 190
    hero_name = ""

    def fight(self, enemy_hp, enemy_power, enemy_name):
        hero_final_hp = self.hero_hp - enemy_power
        enemy_final_hp = enemy_hp - self.hero_power
        if hero_final_hp > enemy_final_hp:
            print(f"{self.hero_name}赢了")
        elif enemy_final_hp > hero_final_hp:
            print(f"{enemy_name}赢了")
        else:
            print("平局")


class Jinx(Hero):
    hero_hp = 1200
    hero_power = 210
    hero_name = "Jinx"


class EZ(Hero):
    hero_hp = 1100
    hero_power = 190
    hero_name = "EZ"


class Timo(Hero):
    hero_hp = 1100
    hero_power = 190
    hero_name = "Timo"


class HeroFactory:
    def creat_hero(self, hero):
        if hero == "ez":
            return EZ()
        elif hero == "jinx":
            return Jinx()
        elif hero == "timo":
            return Timo()
        else:
            raise Exception("此英雄不存在")


if __name__ == '__main__':
    hero_factory = HeroFactory()
    ez = hero_factory.creat_hero("ez")
    jinx = hero_factory.creat_hero("jinx")
    ez.fight(jinx.hero_hp, jinx.hero_power, jinx.hero_name)
