import json
import EasyObj


# 读取package.json
def readPackageJson():
    with open('package.json', 'r') as f:
        data = f.read()
        return EasyObj.BetterDict(json.loads(data))


# 写入package.json
def writePackageJson(data):
    with open('package.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


# 解析版本号
def parseVersion(version):
    return EasyObj.BetterList([int(i) for i in version.split('.')])


if __name__ == "__main__":

    # 读取版本号
    package = readPackageJson()

    version = parseVersion(package.version)
    version[version.length - 1] += 1

    package.version = '.'.join([str(i) for i in version])

    writePackageJson(package)
