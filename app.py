import streamlit as st

from ui_pages import dashboard, map, add_data, ai_helper, file_tag, flight_task
from ui_pages.dashboard import dashboard
from ui_pages.map import render_map
from ui_pages.add_data import single_parser, multi_parser
from ui_pages.ai_helper import ai_helper
from ui_pages.file_tag import file_tag
from ui_pages.flight_task import flight_task

st.set_page_config(page_title="大疆无人机数据管理平台", layout="wide", page_icon="🚁")

st.sidebar.title("🚁 功能菜单")
app_mode = st.sidebar.radio("功能菜单", [
    "📊 数据展示与查询",
    "🌏 遥感采样点地图",
    "🔍 单张图片解析",
    "📂 文件夹批量入库",
    "🧠 数据库实验室",
    "🗃️ 目录标记管理",
    "✈️ 飞行任务时长统计"
],
label_visibility="collapsed")

if app_mode == "📊 数据展示与查询":
    dashboard()
elif app_mode == "🌏 遥感采样点地图":
    render_map()
elif app_mode == "🔍 单张图片解析":
    single_parser()
elif app_mode == "📂 文件夹批量入库":
    multi_parser()
elif app_mode == "🧠 数据库实验室":
    ai_helper()
elif app_mode == "🗃️ 目录标记管理":
    file_tag()
elif app_mode == "✈️ 飞行任务时长统计":
    flight_task()