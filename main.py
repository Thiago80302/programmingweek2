from app_data import AppData
from abstract_demo import Dog, Cat, LandBird, FlyBird, Horse
from heroes import HumanHero, Batman


print(AppData.APP_VERSION)

dog = Dog("Killer")
cat = Cat("Garfield")
dog1 = Dog("Caramelo")

donald = LandBird("Donald")
Pidjeot = FlyBird("Pidjeot")

horse = Horse("Thunder")

print(f"Dog - {dog.describe()}")
print(f"Cat - {cat.describe()}")
print(f"Duck - {donald.describe()}")
print(f"Horse - {horse.describe()}")
print(f"Donald jumps {donald.jump()}")
print(f"Pidjeot jumps {Pidjeot.jump()}")
print(f"Garfield jumps {cat.jump()}")
print(f"Thunder jumps {horse.jump()}")
print(f"Thunder runs {horse.run()}")

human_hero = HumanHero()

batman = Batman()

batman.fly()
batman.land()
batman.super_intelligence()