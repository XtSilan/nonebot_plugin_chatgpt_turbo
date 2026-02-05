from pydantic import Extra, BaseModel
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    oneapi_key: Optional[str] = ""  # （必填）OpenAI官方或者是支持OneAPI的大模型中转服务商提供的KEY
    oneapi_url: Optional[str] = ""  # （可选）大模型中转服务商提供的中转地址，使用OpenAI官方服务不需要填写
    oneapi_model: Optional[str] = "gpt-4o" # （可选）使用的语言大模型，使用识图功能请填写合适的大模型名称
    r1_reason: bool = True # （可选）是否展示思维链（仅对支持思维链的模型生效）
    enable_private_chat: bool = True   # 是否开启私聊对话
    merge_msg: bool = False  # 是否合并转发回复
    # chatgpt_turbo_public: bool = True  # 是否开启群聊对话
    system_prompt: Optional[str] = ""  # （可选）系统提示词，用于设定机器人角色和行为
    temperature: Optional[float] = 1.0  # （可选）温度参数，控制生成文本的随机性，范围一般为0.0-2.0，默认值1.0
class ConfigError(Exception):
    pass