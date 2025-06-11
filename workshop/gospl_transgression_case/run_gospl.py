from gospl.model import Model

print(">> 正在加载 config.yml 并运行 GOSPL 模拟...")
model = Model("config.yml")
model.run()
