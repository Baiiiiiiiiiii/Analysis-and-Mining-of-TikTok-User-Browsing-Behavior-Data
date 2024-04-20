import pandas as pd
import numpy as np

from pyecharts.charts import *
from pyecharts import options as opts


class Chart():
    def __init__(self, title, data):
        self.title = title  # 图表标题
        self.data = data  # 图表数据

    def line_chart(self):
        """
        创建一个线性图表
        """
        chart = (
            Line(init_opts= opts.InitOpts(theme='light',width='500px',height='300px'))  # 使用Line这个类来创建一个线性图表
            .add_xaxis([i[0] for i in self.data])  # 利用列表推导式从data中提取每个元组的第一个元素作为x轴的值
            .add_yaxis(
                '',
                [i[0] for i in self.data],  # 使用列表推导式从data中提取每个元组的第二个元素作为y轴的值
                is_symbol_show= False,  # 不在数据点上显示标记符号
                areastyle_opts= opts.AreaStyleOpts(opacity=1,color='cyan')  # 设置了图表的区域填充样式，包括不透明度，颜色
            )
            .set_global_opts(  # 设置全局选项
                title_opts=opts.TitleOpts(title=self.title),  # 设置图表的标题
                xaxis_opts=opts.AxisOpts(type_="category",boundary_gap=True),  # 设置x轴的类型为category和边界的间隙
                yaxis_opts=opts.AxisOpts(
                    type_="value",  # 设置y轴的类型为value
                    axistick_opts=opts.AxisTickOpts(is_show=True),  # 显示轴刻度
                    splitline_opts=opts.SplitLineOpts(is_show=True),  # 显示分割线
                ),
            )
        )
        return chart

    def pie_chart(self):
        """
        创建饼状图
        """
        chart = (
            Pie(init_opts=opts.InitOpts(theme='light',width='500px',height='300px'))  # 使用pie类创建饼图实例
            .add('',self.data,radius=["30%","45%"],  # 设置饼状图的内半径：30%和外半径：45%
                label_opts=opts.LabelOpts(formatter="{b}:{d}%"))  # b表示每个扇形的数据类别，d表示每个扇形占总量的百分比
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=self.title
                ),
                legend_opts= opts.LegendOpts(pos_left="0%",pos_top="55",orient='vertical')
            )
        )
        return chart

    def fl_chart(self):
        return None
