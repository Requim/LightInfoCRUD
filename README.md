# LightInfoCRUD - 灯具信息

> 基于 FastAPI + SQLAlchemy + PostgreSQL  

---

## 项目简介

这是一个灯具信息的 CRUD（增删改查）管理系统，提供完整的 RESTful API 接口。

---

##  技术栈

| 组件         | 技术       |
| ------------ | ---------- |
| **框架**     | FastAPI    |
| **ORM**      | SQLAlchemy |
| **数据库**   | PostgreSQL |
| **数据验证** | Pydantic   |
| **服务器**   | Uvicorn    |

---

## 项目结构

```
LightInfoCRUD/
├── api/
│   └── v1/
│       └── light_crdu_int.py    # API 路由（增删改查）
├── db/
│   ├── session.py               # 数据库连接配置
│   └── data_struct.py           # 数据库模型（表结构）
├── schemas/
│   └── light.py                 # Pydantic 数据模式
├── conf/
│   └── config.py                # 配置加载
├── config.yaml                  # 配置文件
├── main.py                      # 应用入口
└── README.md                    # 说明文档
```

---

## 快速开始

### 1. 环境准备

```
# 或使用 requirements.txt（如有）
pip install -r requirements.txt
```

### 2. 数据库配置

编辑 `config.yaml`：

```
database:
  url: "postgresql://postgres:password@localhost:1234/light_db"
```

**参数说明**：
- `postgres`: 数据库用户名
- `password`: 数据库密码
- `localhost`: 数据库地址
- `1234`: 端口号
- `light_db`: 数据库名称



### 4. 启动服务

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

启动成功后访问：
- **API 文档**: http://localhost:8000/docs
- **备用文档**: http://localhost:8000/redoc

---

## API 接口列表

### 基础信息

| 属性         | 值                                    |
| ------------ | ------------------------------------- |
| **基础路径** | `/api/v1/lights`                      |
| **服务地址** | `http://localhost:8000`               |
| **完整路径** | `http://localhost:8000/api/v1/lights` |

---

### 接口详情

#### 新增灯具 (Create)

```
POST /api/v1/lights/
Content-Type: application/json

{
  "brand": "XXXX",
  "model": "xxxx",
  "power": 10,
  "color_temp": 1111
}
```

**请求参数**：

| 字段       | 类型    | 必填 | 说明                  |
| ---------- | ------- | ---- | --------------------- |
| brand      | string  | 是   | 品牌（最大 50 字符）  |
| model      | string  | 是   | 型号（最大 100 字符） |
| power      | integer | 是   | 功率（瓦特）          |
| color_temp | integer | 是   | 色温（开尔文）        |

**响应示例**：
```
{
  "id": 1,
  "brand": "XXXX",
  "model": "xxxx",
  "power": 10,
  "color_temp": 1111
}
```

---

####  查询灯具列表 (Read)

```
GET /api/v1/lights/?skip=0&limit=100
```

**查询参数**：
| 参数  | 类型    | 默认值 | 说明               |
| ----- | ------- | ------ | ------------------ |
| skip  | integer | 0      | 跳过记录数（分页） |
| limit | integer | 100    | 返回数量限制       |

**响应示例**：
```
[
  {
    "id": 1,
  "brand": "XXXX",
  "model": "xxxx",
  "power": 10,
  "color_temp": 1111
  }
]
```

---

#### 修改灯具 (Update)

```
PUT /api/v1/lights/1
Content-Type: application/json

{
  "brand": "XXXX",
  "model": "xxxx",
  "power": 11,
  "color_temp": 1111
}
```

**路径参数**：
| 参数     | 类型    | 说明    |
| -------- | ------- | ------- |
| light_id | integer | 灯具 ID |

**响应示例**：

```
{
  "id": 1,
  "brand": "XXXX",
  "model": "xxxx",
  "power": 11,
  "color_temp": 1111
}
```

---

#### 删除灯具 (Delete)

```
DELETE /api/v1/lights/1
```

**路径参数**：

| 参数     | 类型    | 说明    |
| -------- | ------- | ------- |
| light_id | integer | 灯具 ID |

**响应示例**：
```
{
  "message": "Success"
}
```

---

## 测试方法

### 方法 1：使用 Swagger UI（推荐）

1. 启动服务后访问：http://localhost:8000/docs
2. 在界面上直接测试所有接口

### 方法 2：使用 Postman

#### 1. 新增灯具 

- **Method**: `POST`

- **URL**: `http://127.0.0.1:8000/api/v1/lights/`

- **Headers**: `Content-Type: application/json`

- **Body** -> **raw** (JSON):

  JSON

  ```
  {
    "brand": "XXXX",
    "model": "xxxx",
    "power": 10,
    "color_temp": 1111
  }
  ```

  *期望返回：200 OK，并带上自动生成的 `"id": 1`。*

------

#### 2. 获取列表 (READ LIST)

- **Method**: `GET`

- **URL**: `http://127.0.0.1:8000/api/v1/lights/?skip=0&limit=10` 

  *期望返回：灯具数组 `[...]`。如果库里没数据，返回 `[]`。*

------

#### 3. 修改灯具

- **Method**: `PUT`

- **URL**: `http://127.0.0.1:8000/api/v1/lights/1` (注意最后的 1 是你要改的灯具 ID)

- **Body** -> **raw** (JSON):

  JSON

  ```
  {
    "brand": "XXXX",
    "model": "xxxx",
    "power": 11,
    "color_temp": 1111
  }
  ```

  *期望返回：更新后的完整数据对象。*

------

#### 4. 删除灯具 (DELETE)

- **Method**: `DELETE`

- **URL**: `http://127.0.0.1:8000/api/v1/lights/1` 

  *期望返回：`{"message": "Success"}`。如果 ID 错误，返回 404。*