# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-27 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_provice', models.CharField(choices=[('河北省', '河北省'), ('山西省', '山西省'), ('内蒙古自治区', '内蒙古自治区'), ('辽宁省', '辽宁省'), ('吉林省', '吉林省'), ('黑龙江省', '黑龙江省'), ('江苏省', '江苏省'), ('浙江省', '浙江省'), ('安徽省', '安徽省'), ('福建省', '福建省'), ('江西省', '江西省'), ('山东省', '山东省'), ('河南省', '河南省'), ('湖北省', '湖北省'), ('湖南省', '湖南省'), ('广东省', '广东省'), ('广西壮族自治区', '广西壮族自治区'), ('海南省', '海南省'), ('四川省', '四川省'), ('贵州省', '贵州省'), ('云南省', '云南省'), ('陕西省', '陕西省'), ('甘肃省', '甘肃省'), ('青海省', '青海省'), ('西藏自治区', '西藏自治区'), ('宁夏回族自治区', '宁夏回族自治区'), ('台湾', '台湾'), ('北京市', '北京市'), ('天津市', '天津市'), ('上海市', '上海市'), ('重庆市', '重庆市'), ('香港', '香港'), ('澳门', '澳门'), ('新疆维吾尔自治区', '新疆维吾尔自治区')], max_length=10, verbose_name='省')),
                ('loc_city', models.CharField(choices=[('石家庄市', '石家庄市'), ('邯郸市', '邯郸市'), ('唐山市', '唐山市'), ('保定市', '保定市'), ('秦皇岛市', '秦皇岛市'), ('邢台市', '邢台市'), ('张家口市', '张家口市'), ('承德市', '承德市'), ('沧州市', '沧州市'), ('廊坊市', '廊坊市'), ('衡水市', '衡水市'), ('辛集市', '辛集市'), ('晋州市', '晋州市'), ('新乐市', '新乐市'), ('遵化市', '遵化市'), ('迁安市', '迁安市'), ('霸州市', '霸州市'), ('三河市', '三河市'), ('定州市', '定州市'), ('涿州市', '涿州市'), ('安国市', '安国市'), ('高碑店市', '高碑店市'), ('泊头市', '泊头市'), ('任丘市', '任丘市'), ('黄骅市', '黄骅市'), ('河间市', '河间市'), ('冀州市', '冀州市'), ('深州市', '深州市'), ('南宫市', '南宫市'), ('沙河市', '沙河市'), ('武安市', '武安市'), ('太原市', '太原市'), ('大同市', '大同市'), ('朔州市', '朔州市'), ('阳泉市', '阳泉市'), ('长治市', '长治市'), ('晋城市', '晋城市'), ('忻州市', '忻州市'), ('吕梁市', '吕梁市'), ('晋中市', '晋中市'), ('临汾市', '临汾市'), ('运城市', '运城市'), ('古交市', '古交市'), ('潞城市', '潞城市'), ('高平市', '高平市'), ('原平市', '原平市'), ('孝义市', '孝义市'), ('汾阳市', '汾阳市'), ('介休市', '介休市'), ('侯马市', '侯马市'), ('霍州市', '霍州市'), ('永济市', '永济市'), ('河津市', '河津市'), ('呼和浩特市', '呼和浩特市'), ('包头市', '包头市'), ('乌海市', '乌海市'), ('赤峰市', '赤峰市'), ('呼伦贝尔市', '呼伦贝尔市'), ('通辽市', '通辽市'), ('乌兰察布市', '乌兰察布市'), ('鄂尔多斯市', '鄂尔多斯市'), ('巴彦淖尔市', '巴彦淖尔市'), ('满洲里市', '满洲里市'), ('扎兰屯市', '扎兰屯市'), ('牙克石市', '牙克石市'), ('根河市', '根河市'), ('额尔古纳市', '额尔古纳市'), ('乌兰浩特市', '乌兰浩特市'), ('阿尔山市', '阿尔山市'), ('霍林郭勒市', '霍林郭勒市'), ('锡林浩特市', '锡林浩特市'), ('二连浩特市', '二连浩特市'), ('丰镇市', '丰镇市'), ('沈阳市', '沈阳市'), ('大连市', '大连市'), ('朝阳市', '朝阳市'), ('阜新市', '阜新市'), ('铁岭市', '铁岭市'), ('抚顺市', '抚顺市'), ('本溪市', '本溪市'), ('辽阳市', '辽阳市'), ('鞍山市', '鞍山市'), ('丹东市', '丹东市'), ('营口市', '营口市'), ('盘锦市', '盘锦市'), ('锦州市', '锦州市'), ('葫芦岛市', '葫芦岛市'), ('新民市', '新民市'), ('瓦房店市', '瓦房店市'), ('庄河市', '庄河市'), ('北票市', '北票市'), ('凌源市', '凌源市'), ('调兵山市', '调兵山市'), ('开原市', '开原市'), ('灯塔市', '灯塔市'), ('海城市', '海城市'), ('凤城市', '凤城市'), ('东港市', '东港市'), ('大石桥市', '大石桥市'), ('盖州市', '盖州市'), ('凌海市', '凌海市'), ('北镇市', '北镇市'), ('兴城市', '兴城市'), ('长春市', '长春市'), ('吉林市', '吉林市'), ('白城市', '白城市'), ('松原市', '松原市'), ('四平市', '四平市'), ('辽源市', '辽源市'), ('通化市', '通化市'), ('白山市', '白山市'), ('德惠市', '德惠市'), ('榆树市', '榆树市'), ('磐石市', '磐石市'), ('蛟河市', '蛟河市'), ('桦甸市', '桦甸市'), ('舒兰市', '舒兰市'), ('洮南市', '洮南市'), ('大安市', '大安市'), ('双辽市', '双辽市'), ('公主岭市', '公主岭市'), ('梅河口市', '梅河口市'), ('集安市', '集安市'), ('临江市', '临江市'), ('延吉市', '延吉市'), ('图们市', '图们市'), ('敦化市', '敦化市'), ('珲春市', '珲春市'), ('龙井市', '龙井市'), ('和龙市', '和龙市'), ('扶余市', '扶余市'), ('哈尔滨市', '哈尔滨市'), ('齐齐哈尔市', '齐齐哈尔市'), ('黑河市', '黑河市'), ('大庆市', '大庆市'), ('伊春市', '伊春市'), ('鹤岗市', '鹤岗市'), ('佳木斯市', '佳木斯市'), ('双鸭山市', '双鸭山市'), ('七台河市', '七台河市'), ('鸡西市', '鸡西市'), ('牡丹江市', '牡丹江市'), ('绥化市', '绥化市'), ('尚志市', '尚志市'), ('五常市', '五常市'), ('讷河市', '讷河市'), ('北安市', '北安市'), ('五大连池市', '五大连池市'), ('铁力市', '铁力市'), ('同江市', '同江市'), ('富锦市', '富锦市'), ('虎林市', '虎林市'), ('密山市', '密山市'), ('绥芬河市', '绥芬河市'), ('海林市', '海林市'), ('宁安市', '宁安市'), ('安达市', '安达市'), ('肇东市', '肇东市'), ('海伦市', '海伦市'), ('穆棱市', '穆棱市'), ('东宁市', '东宁市'), ('抚远市', '抚远市'), ('南京市', '南京市'), ('徐州市', '徐州市'), ('连云港市', '连云港市'), ('宿迁市', '宿迁市'), ('淮安市', '淮安市'), ('盐城市', '盐城市'), ('扬州市', '扬州市'), ('泰州市', '泰州市'), ('南通市', '南通市'), ('镇江市', '镇江市'), ('常州市', '常州市'), ('无锡市', '无锡市'), ('苏州市', '苏州市'), ('常熟市', '常熟市'), ('张家港市', '张家港市'), ('太仓市', '太仓市'), ('昆山市', '昆山市'), ('江阴市', '江阴市'), ('宜兴市', '宜兴市'), ('溧阳市', '溧阳市'), ('扬中市', '扬中市'), ('句容市', '句容市'), ('丹阳市', '丹阳市'), ('如皋市', '如皋市'), ('海门市', '海门市'), ('启东市', '启东市'), ('高邮市', '高邮市'), ('仪征市', '仪征市'), ('兴化市', '兴化市'), ('泰兴市', '泰兴市'), ('靖江市', '靖江市'), ('东台市', '东台市'), ('邳州市', '邳州市'), ('新沂市', '新沂市'), ('杭州市', '杭州市'), ('宁波市', '宁波市'), ('湖州市', '湖州市'), ('嘉兴市', '嘉兴市'), ('舟山市', '舟山市'), ('绍兴市', '绍兴市'), ('衢州市', '衢州市'), ('金华市', '金华市'), ('台州市', '台州市'), ('温州市', '温州市'), ('丽水市', '丽水市'), ('临安市', '临安市'), ('建德市', '建德市'), ('慈溪市', '慈溪市'), ('余姚市', '余姚市'), ('平湖市', '平湖市'), ('海宁市', '海宁市'), ('桐乡市', '桐乡市'), ('诸暨市', '诸暨市'), ('嵊州市', '嵊州市'), ('江山市', '江山市'), ('兰溪市', '兰溪市'), ('永康市', '永康市'), ('义乌市', '义乌市'), ('东阳市', '东阳市'), ('临海市', '临海市'), ('温岭市', '温岭市'), ('瑞安市', '瑞安市'), ('乐清市', '乐清市'), ('龙泉市', '龙泉市'), ('合肥市', '合肥市'), ('芜湖市', '芜湖市'), ('蚌埠市', '蚌埠市'), ('淮南市', '淮南市'), ('马鞍山市', '马鞍山市'), ('淮北市', '淮北市'), ('铜陵市', '铜陵市'), ('安庆市', '安庆市'), ('黄山市', '黄山市'), ('滁州市', '滁州市'), ('阜阳市', '阜阳市'), ('宿州市', '宿州市'), ('六安市', '六安市'), ('亳州市', '亳州市'), ('池州市', '池州市'), ('宣城市', '宣城市'), ('巢湖市', '巢湖市'), ('桐城市', '桐城市'), ('天长市', '天长市'), ('明光市', '明光市'), ('界首市', '界首市'), ('宁国市', '宁国市'), ('厦门市', '厦门市'), ('福州市', '福州市'), ('南平市', '南平市'), ('三明市', '三明市'), ('莆田市', '莆田市'), ('泉州市', '泉州市'), ('漳州市', '漳州市'), ('龙岩市', '龙岩市'), ('宁德市', '宁德市'), ('福清市', '福清市'), ('长乐市', '长乐市'), ('邵武市', '邵武市'), ('武夷山市', '武夷山市'), ('建瓯市', '建瓯市'), ('永安市', '永安市'), ('石狮市', '石狮市'), ('晋江市', '晋江市'), ('南安市', '南安市'), ('龙海市', '龙海市'), ('漳平市', '漳平市'), ('福安市', '福安市'), ('福鼎市', '福鼎市'), ('南昌市', '南昌市'), ('九江市', '九江市'), ('景德镇市', '景德镇市'), ('鹰潭市', '鹰潭市'), ('新余市', '新余市'), ('萍乡市', '萍乡市'), ('赣州市', '赣州市'), ('上饶市', '上饶市'), ('抚州市', '抚州市'), ('宜春市', '宜春市'), ('吉安市', '吉安市'), ('瑞昌市', '瑞昌市'), ('共青城市', '共青城市'), ('乐平市', '乐平市'), ('瑞金市', '瑞金市'), ('德兴市', '德兴市'), ('丰城市', '丰城市'), ('樟树市', '樟树市'), ('高安市', '高安市'), ('井冈山市', '井冈山市'), ('贵溪市', '贵溪市'), ('济南市', '济南市'), ('青岛市', '青岛市'), ('聊城市', '聊城市'), ('德州市', '德州市'), ('东营市', '东营市'), ('淄博市', '淄博市'), ('潍坊市', '潍坊市'), ('烟台市', '烟台市'), ('威海市', '威海市'), ('日照市', '日照市'), ('临沂市', '临沂市'), ('枣庄市', '枣庄市'), ('济宁市', '济宁市'), ('泰安市', '泰安市'), ('莱芜市', '莱芜市'), ('滨州市', '滨州市'), ('菏泽市', '菏泽市'), ('胶州市', '胶州市'), ('即墨市', '即墨市'), ('平度市', '平度市'), ('莱西市', '莱西市'), ('临清市', '临清市'), ('乐陵市', '乐陵市'), ('禹城市', '禹城市'), ('安丘市', '安丘市'), ('昌邑市', '昌邑市'), ('高密市', '高密市'), ('青州市', '青州市'), ('诸城市', '诸城市'), ('寿光市', '寿光市'), ('栖霞市', '栖霞市'), ('海阳市', '海阳市'), ('龙口市', '龙口市'), ('莱阳市', '莱阳市'), ('莱州市', '莱州市'), ('蓬莱市', '蓬莱市'), ('招远市', '招远市'), ('荣成市', '荣成市'), ('乳山市', '乳山市'), ('滕州市', '滕州市'), ('曲阜市', '曲阜市'), ('邹城市', '邹城市'), ('新泰市', '新泰市'), ('肥城市', '肥城市'), ('郑州市', '郑州市'), ('开封市', '开封市'), ('洛阳市', '洛阳市'), ('平顶山市', '平顶山市'), ('安阳市', '安阳市'), ('鹤壁市', '鹤壁市'), ('新乡市', '新乡市'), ('焦作市', '焦作市'), ('濮阳市', '濮阳市'), ('许昌市', '许昌市'), ('漯河市', '漯河市'), ('三门峡市', '三门峡市'), ('南阳市', '南阳市'), ('商丘市', '商丘市'), ('周口市', '周口市'), ('驻马店市', '驻马店市'), ('信阳市', '信阳市'), ('荥阳市', '荥阳市'), ('新郑市', '新郑市'), ('登封市', '登封市'), ('新密市', '新密市'), ('偃师市', '偃师市'), ('孟州市', '孟州市'), ('沁阳市', '沁阳市'), ('卫辉市', '卫辉市'), ('辉县市', '辉县市'), ('林州市', '林州市'), ('禹州市', '禹州市'), ('长葛市', '长葛市'), ('舞钢市', '舞钢市'), ('义马市', '义马市'), ('灵宝市', '灵宝市'), ('项城市', '项城市'), ('巩义市', '巩义市'), ('邓州市', '邓州市'), ('永城市', '永城市'), ('汝州市', '汝州市'), ('济源市', '济源市'), ('武汉市', '武汉市'), ('十堰市', '十堰市'), ('襄阳市', '襄阳市'), ('荆门市', '荆门市'), ('孝感市', '孝感市'), ('黄冈市', '黄冈市'), ('鄂州市', '鄂州市'), ('黄石市', '黄石市'), ('咸宁市', '咸宁市'), ('荆州市', '荆州市'), ('宜昌市', '宜昌市'), ('随州市', '随州市'), ('丹江口市', '丹江口市'), ('老河口市', '老河口市'), ('枣阳市', '枣阳市'), ('宜城市', '宜城市'), ('钟祥市', '钟祥市'), ('汉川市', '汉川市'), ('应城市', '应城市'), ('安陆市', '安陆市'), ('广水市', '广水市'), ('麻城市', '麻城市'), ('武穴市', '武穴市'), ('大冶市', '大冶市'), ('赤壁市', '赤壁市'), ('石首市', '石首市'), ('洪湖市', '洪湖市'), ('松滋市', '松滋市'), ('宜都市', '宜都市'), ('枝江市', '枝江市'), ('当阳市', '当阳市'), ('恩施市', '恩施市'), ('利川市', '利川市'), ('仙桃市', '仙桃市'), ('天门市', '天门市'), ('潜江市', '潜江市'), ('长沙市', '长沙市'), ('衡阳市', '衡阳市'), ('张家界市', '张家界市'), ('常德市', '常德市'), ('益阳市', '益阳市'), ('岳阳市', '岳阳市'), ('株洲市', '株洲市'), ('湘潭市', '湘潭市'), ('郴州市', '郴州市'), ('永州市', '永州市'), ('邵阳市', '邵阳市'), ('怀化市', '怀化市'), ('娄底市', '娄底市'), ('耒阳市', '耒阳市'), ('常宁市', '常宁市'), ('浏阳市', '浏阳市'), ('津市市', '津市市'), ('沅江市', '沅江市'), ('汨罗市', '汨罗市'), ('临湘市', '临湘市'), ('醴陵市', '醴陵市'), ('湘乡市', '湘乡市'), ('韶山市', '韶山市'), ('资兴市', '资兴市'), ('武冈市', '武冈市'), ('洪江市', '洪江市'), ('冷水江市', '冷水江市'), ('涟源市', '涟源市'), ('吉首市', '吉首市'), ('广州市', '广州市'), ('深圳市', '深圳市'), ('清远市', '清远市'), ('韶关市', '韶关市'), ('河源市', '河源市'), ('梅州市', '梅州市'), ('潮州市', '潮州市'), ('汕头市', '汕头市'), ('揭阳市', '揭阳市'), ('汕尾市', '汕尾市'), ('惠州市', '惠州市'), ('东莞市', '东莞市'), ('珠海市', '珠海市'), ('中山市', '中山市'), ('江门市', '江门市'), ('佛山市', '佛山市'), ('肇庆市', '肇庆市'), ('云浮市', '云浮市'), ('阳江市', '阳江市'), ('茂名市', '茂名市'), ('湛江市', '湛江市'), ('英德市', '英德市'), ('连州市', '连州市'), ('乐昌市', '乐昌市'), ('南雄市', '南雄市'), ('兴宁市', '兴宁市'), ('普宁市', '普宁市'), ('陆丰市', '陆丰市'), ('恩平市', '恩平市'), ('台山市', '台山市'), ('开平市', '开平市'), ('鹤山市', '鹤山市'), ('四会市', '四会市'), ('罗定市', '罗定市'), ('阳春市', '阳春市'), ('化州市', '化州市'), ('信宜市', '信宜市'), ('高州市', '高州市'), ('吴川市', '吴川市'), ('廉江市', '廉江市'), ('雷州市', '雷州市'), ('南宁市', '南宁市'), ('桂林市', '桂林市'), ('柳州市', '柳州市'), ('梧州市', '梧州市'), ('贵港市', '贵港市'), ('玉林市', '玉林市'), ('钦州市', '钦州市'), ('北海市', '北海市'), ('防城港市', '防城港市'), ('崇左市', '崇左市'), ('百色市', '百色市'), ('河池市', '河池市'), ('来宾市', '来宾市'), ('贺州市', '贺州市'), ('岑溪市', '岑溪市'), ('桂平市', '桂平市'), ('北流市', '北流市'), ('东兴市', '东兴市'), ('凭祥市', '凭祥市'), ('宜州市', '宜州市'), ('合山市', '合山市'), ('靖西市', '靖西市'), ('海口市', '海口市'), ('三亚市', '三亚市'), ('三沙市', '三沙市'), ('儋州市', '儋州市'), ('文昌市', '文昌市'), ('琼海市', '琼海市'), ('万宁市', '万宁市'), ('东方市', '东方市'), ('五指山市', '五指山市'), ('成都市', '成都市'), ('广元市', '广元市'), ('绵阳市', '绵阳市'), ('德阳市', '德阳市'), ('南充市', '南充市'), ('广安市', '广安市'), ('遂宁市', '遂宁市'), ('内江市', '内江市'), ('乐山市', '乐山市'), ('自贡市', '自贡市'), ('泸州市', '泸州市'), ('宜宾市', '宜宾市'), ('攀枝花市', '攀枝花市'), ('巴中市', '巴中市'), ('达州市', '达州市'), ('资阳市', '资阳市'), ('眉山市', '眉山市'), ('雅安市', '雅安市'), ('崇州市', '崇州市'), ('邛崃市', '邛崃市'), ('都江堰市', '都江堰市'), ('彭州市', '彭州市'), ('江油市', '江油市'), ('什邡市', '什邡市'), ('广汉市', '广汉市'), ('绵竹市', '绵竹市'), ('阆中市', '阆中市'), ('华蓥市', '华蓥市'), ('峨眉山市', '峨眉山市'), ('万源市', '万源市'), ('简阳市', '简阳市'), ('西昌市', '西昌市'), ('康定市', '康定市'), ('马尔康市', '马尔康市'), ('贵阳市', '贵阳市'), ('六盘水市', '六盘水市'), ('遵义市', '遵义市'), ('安顺市', '安顺市'), ('毕节市', '毕节市'), ('铜仁市', '铜仁市'), ('清镇市', '清镇市'), ('赤水市', '赤水市'), ('仁怀市', '仁怀市'), ('凯里市', '凯里市'), ('都匀市', '都匀市'), ('兴义市', '兴义市'), ('福泉市', '福泉市'), ('昆明市', '昆明市'), ('曲靖市', '曲靖市'), ('玉溪市', '玉溪市'), ('丽江市', '丽江市'), ('昭通市', '昭通市'), ('普洱市', '普洱市'), ('临沧市', '临沧市'), ('保山市', '保山市'), ('安宁市', '安宁市'), ('宣威市', '宣威市'), ('芒市', '芒市'), ('瑞丽市', '瑞丽市'), ('大理市', '大理市'), ('楚雄市', '楚雄市'), ('个旧市', '个旧市'), ('开远市', '开远市'), ('蒙自市', '蒙自市'), ('弥勒市', '弥勒市'), ('景洪市', '景洪市'), ('文山市', '文山市'), ('香格里拉市', '香格里拉市'), ('腾冲市', '腾冲市'), ('西安市', '西安市'), ('延安市', '延安市'), ('铜川市', '铜川市'), ('渭南市', '渭南市'), ('咸阳市', '咸阳市'), ('宝鸡市', '宝鸡市'), ('汉中市', '汉中市'), ('榆林市', '榆林市'), ('商洛市', '商洛市'), ('安康市', '安康市'), ('韩城', '韩城'), ('华阴', '华阴'), ('兴平', '兴平'), ('兰州市', '兰州市'), ('嘉峪关市', '嘉峪关市'), ('金昌市', '金昌市'), ('白银市', '白银市'), ('天水市', '天水市'), ('酒泉市', '酒泉市'), ('张掖市', '张掖市'), ('武威市', '武威市'), ('庆阳市', '庆阳市'), ('平凉市', '平凉市'), ('定西市', '定西市'), ('陇南市', '陇南市'), ('玉门市', '玉门市'), ('敦煌市', '敦煌市'), ('临夏市', '临夏市'), ('合作市', '合作市'), ('西宁市', '西宁市'), ('海东市', '海东市'), ('格尔木市', '格尔木市'), ('德令哈市', '德令哈市'), ('玉树市', '玉树市'), ('拉萨市', '拉萨市'), ('日喀则市', '日喀则市'), ('昌都市', '昌都市'), ('林芝市', '林芝市'), ('山南市', '山南市'), ('银川市', '银川市'), ('石嘴山市', '石嘴山市'), ('吴忠市', '吴忠市'), ('中卫市', '中卫市'), ('固原市', '固原市'), ('灵武市', '灵武市'), ('青铜峡市', '青铜峡市'), ('台北市', '台北市'), ('新北市', '新北市'), ('桃园市', '桃园市'), ('台中市', '台中市'), ('台南市', '台南市'), ('高雄市', '高雄市'), ('基隆市', '基隆市'), ('新竹市', '新竹市'), ('嘉义市', '嘉义市'), ('北京市', '北京市'), ('天津市', '天津市'), ('上海市', '上海市'), ('重庆市', '重庆市'), ('香港特别行政区', '香港特别行政区'), ('澳门特别行政区', '澳门特别行政区'), ('乌鲁木齐市', '乌鲁木齐市'), ('克拉玛依市', '克拉玛依市'), ('吐鲁番市', '吐鲁番市'), ('哈密市', '哈密市'), ('喀什市', '喀什市'), ('阿克苏市', '阿克苏市'), ('和田市', '和田市'), ('阿图什市', '阿图什市'), ('阿拉山口市', '阿拉山口市'), ('博乐市', '博乐市'), ('昌吉市', '昌吉市'), ('阜康市', '阜康市'), ('库尔勒市', '库尔勒市'), ('伊宁市', '伊宁市'), ('奎屯市', '奎屯市'), ('塔城市', '塔城市'), ('乌苏市', '乌苏市'), ('阿勒泰市', '阿勒泰市'), ('霍尔果斯市', '霍尔果斯市'), ('石河子市', '石河子市'), ('阿拉尔市', '阿拉尔市'), ('图木舒克市', '图木舒克市'), ('五家渠市', '五家渠市'), ('北屯市', '北屯市'), ('铁门关市', '铁门关市'), ('双河市', '双河市'), ('可克达拉市', '可克达拉市'), ('昆玉市', '昆玉市')], max_length=10, verbose_name='城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最⼩查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最⼤查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最⼩交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最⼤交友年龄')),
                ('sex', models.CharField(choices=[('男', 'mail'), ('女', 'famail')], default='男', max_length=4, verbose_name='性别')),
                ('vibration', models.BooleanField(default=True, verbose_name='开启震动')),
                ('only_matche', models.BooleanField(default=False, verbose_name='不让为匹配的⼈看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='⾃动播放视频')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=12, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('sex', models.CharField(choices=[('男', 'mail'), ('女', 'famail')], default='男', max_length=4, verbose_name='性别')),
                ('birth_year', models.IntegerField(default=2000, verbose_name='年')),
                ('birth_month', models.IntegerField(default=1, verbose_name='月')),
                ('birth_day', models.IntegerField(default=1, verbose_name='日')),
                ('avatar', models.CharField(default=None, max_length=128, verbose_name='头像')),
                ('loc_provice', models.CharField(choices=[('河北省', '河北省'), ('山西省', '山西省'), ('内蒙古自治区', '内蒙古自治区'), ('辽宁省', '辽宁省'), ('吉林省', '吉林省'), ('黑龙江省', '黑龙江省'), ('江苏省', '江苏省'), ('浙江省', '浙江省'), ('安徽省', '安徽省'), ('福建省', '福建省'), ('江西省', '江西省'), ('山东省', '山东省'), ('河南省', '河南省'), ('湖北省', '湖北省'), ('湖南省', '湖南省'), ('广东省', '广东省'), ('广西壮族自治区', '广西壮族自治区'), ('海南省', '海南省'), ('四川省', '四川省'), ('贵州省', '贵州省'), ('云南省', '云南省'), ('陕西省', '陕西省'), ('甘肃省', '甘肃省'), ('青海省', '青海省'), ('西藏自治区', '西藏自治区'), ('宁夏回族自治区', '宁夏回族自治区'), ('台湾', '台湾'), ('北京市', '北京市'), ('天津市', '天津市'), ('上海市', '上海市'), ('重庆市', '重庆市'), ('香港', '香港'), ('澳门', '澳门'), ('新疆维吾尔自治区', '新疆维吾尔自治区')], max_length=10, verbose_name='省')),
                ('loc_city', models.CharField(choices=[('石家庄市', '石家庄市'), ('邯郸市', '邯郸市'), ('唐山市', '唐山市'), ('保定市', '保定市'), ('秦皇岛市', '秦皇岛市'), ('邢台市', '邢台市'), ('张家口市', '张家口市'), ('承德市', '承德市'), ('沧州市', '沧州市'), ('廊坊市', '廊坊市'), ('衡水市', '衡水市'), ('辛集市', '辛集市'), ('晋州市', '晋州市'), ('新乐市', '新乐市'), ('遵化市', '遵化市'), ('迁安市', '迁安市'), ('霸州市', '霸州市'), ('三河市', '三河市'), ('定州市', '定州市'), ('涿州市', '涿州市'), ('安国市', '安国市'), ('高碑店市', '高碑店市'), ('泊头市', '泊头市'), ('任丘市', '任丘市'), ('黄骅市', '黄骅市'), ('河间市', '河间市'), ('冀州市', '冀州市'), ('深州市', '深州市'), ('南宫市', '南宫市'), ('沙河市', '沙河市'), ('武安市', '武安市'), ('太原市', '太原市'), ('大同市', '大同市'), ('朔州市', '朔州市'), ('阳泉市', '阳泉市'), ('长治市', '长治市'), ('晋城市', '晋城市'), ('忻州市', '忻州市'), ('吕梁市', '吕梁市'), ('晋中市', '晋中市'), ('临汾市', '临汾市'), ('运城市', '运城市'), ('古交市', '古交市'), ('潞城市', '潞城市'), ('高平市', '高平市'), ('原平市', '原平市'), ('孝义市', '孝义市'), ('汾阳市', '汾阳市'), ('介休市', '介休市'), ('侯马市', '侯马市'), ('霍州市', '霍州市'), ('永济市', '永济市'), ('河津市', '河津市'), ('呼和浩特市', '呼和浩特市'), ('包头市', '包头市'), ('乌海市', '乌海市'), ('赤峰市', '赤峰市'), ('呼伦贝尔市', '呼伦贝尔市'), ('通辽市', '通辽市'), ('乌兰察布市', '乌兰察布市'), ('鄂尔多斯市', '鄂尔多斯市'), ('巴彦淖尔市', '巴彦淖尔市'), ('满洲里市', '满洲里市'), ('扎兰屯市', '扎兰屯市'), ('牙克石市', '牙克石市'), ('根河市', '根河市'), ('额尔古纳市', '额尔古纳市'), ('乌兰浩特市', '乌兰浩特市'), ('阿尔山市', '阿尔山市'), ('霍林郭勒市', '霍林郭勒市'), ('锡林浩特市', '锡林浩特市'), ('二连浩特市', '二连浩特市'), ('丰镇市', '丰镇市'), ('沈阳市', '沈阳市'), ('大连市', '大连市'), ('朝阳市', '朝阳市'), ('阜新市', '阜新市'), ('铁岭市', '铁岭市'), ('抚顺市', '抚顺市'), ('本溪市', '本溪市'), ('辽阳市', '辽阳市'), ('鞍山市', '鞍山市'), ('丹东市', '丹东市'), ('营口市', '营口市'), ('盘锦市', '盘锦市'), ('锦州市', '锦州市'), ('葫芦岛市', '葫芦岛市'), ('新民市', '新民市'), ('瓦房店市', '瓦房店市'), ('庄河市', '庄河市'), ('北票市', '北票市'), ('凌源市', '凌源市'), ('调兵山市', '调兵山市'), ('开原市', '开原市'), ('灯塔市', '灯塔市'), ('海城市', '海城市'), ('凤城市', '凤城市'), ('东港市', '东港市'), ('大石桥市', '大石桥市'), ('盖州市', '盖州市'), ('凌海市', '凌海市'), ('北镇市', '北镇市'), ('兴城市', '兴城市'), ('长春市', '长春市'), ('吉林市', '吉林市'), ('白城市', '白城市'), ('松原市', '松原市'), ('四平市', '四平市'), ('辽源市', '辽源市'), ('通化市', '通化市'), ('白山市', '白山市'), ('德惠市', '德惠市'), ('榆树市', '榆树市'), ('磐石市', '磐石市'), ('蛟河市', '蛟河市'), ('桦甸市', '桦甸市'), ('舒兰市', '舒兰市'), ('洮南市', '洮南市'), ('大安市', '大安市'), ('双辽市', '双辽市'), ('公主岭市', '公主岭市'), ('梅河口市', '梅河口市'), ('集安市', '集安市'), ('临江市', '临江市'), ('延吉市', '延吉市'), ('图们市', '图们市'), ('敦化市', '敦化市'), ('珲春市', '珲春市'), ('龙井市', '龙井市'), ('和龙市', '和龙市'), ('扶余市', '扶余市'), ('哈尔滨市', '哈尔滨市'), ('齐齐哈尔市', '齐齐哈尔市'), ('黑河市', '黑河市'), ('大庆市', '大庆市'), ('伊春市', '伊春市'), ('鹤岗市', '鹤岗市'), ('佳木斯市', '佳木斯市'), ('双鸭山市', '双鸭山市'), ('七台河市', '七台河市'), ('鸡西市', '鸡西市'), ('牡丹江市', '牡丹江市'), ('绥化市', '绥化市'), ('尚志市', '尚志市'), ('五常市', '五常市'), ('讷河市', '讷河市'), ('北安市', '北安市'), ('五大连池市', '五大连池市'), ('铁力市', '铁力市'), ('同江市', '同江市'), ('富锦市', '富锦市'), ('虎林市', '虎林市'), ('密山市', '密山市'), ('绥芬河市', '绥芬河市'), ('海林市', '海林市'), ('宁安市', '宁安市'), ('安达市', '安达市'), ('肇东市', '肇东市'), ('海伦市', '海伦市'), ('穆棱市', '穆棱市'), ('东宁市', '东宁市'), ('抚远市', '抚远市'), ('南京市', '南京市'), ('徐州市', '徐州市'), ('连云港市', '连云港市'), ('宿迁市', '宿迁市'), ('淮安市', '淮安市'), ('盐城市', '盐城市'), ('扬州市', '扬州市'), ('泰州市', '泰州市'), ('南通市', '南通市'), ('镇江市', '镇江市'), ('常州市', '常州市'), ('无锡市', '无锡市'), ('苏州市', '苏州市'), ('常熟市', '常熟市'), ('张家港市', '张家港市'), ('太仓市', '太仓市'), ('昆山市', '昆山市'), ('江阴市', '江阴市'), ('宜兴市', '宜兴市'), ('溧阳市', '溧阳市'), ('扬中市', '扬中市'), ('句容市', '句容市'), ('丹阳市', '丹阳市'), ('如皋市', '如皋市'), ('海门市', '海门市'), ('启东市', '启东市'), ('高邮市', '高邮市'), ('仪征市', '仪征市'), ('兴化市', '兴化市'), ('泰兴市', '泰兴市'), ('靖江市', '靖江市'), ('东台市', '东台市'), ('邳州市', '邳州市'), ('新沂市', '新沂市'), ('杭州市', '杭州市'), ('宁波市', '宁波市'), ('湖州市', '湖州市'), ('嘉兴市', '嘉兴市'), ('舟山市', '舟山市'), ('绍兴市', '绍兴市'), ('衢州市', '衢州市'), ('金华市', '金华市'), ('台州市', '台州市'), ('温州市', '温州市'), ('丽水市', '丽水市'), ('临安市', '临安市'), ('建德市', '建德市'), ('慈溪市', '慈溪市'), ('余姚市', '余姚市'), ('平湖市', '平湖市'), ('海宁市', '海宁市'), ('桐乡市', '桐乡市'), ('诸暨市', '诸暨市'), ('嵊州市', '嵊州市'), ('江山市', '江山市'), ('兰溪市', '兰溪市'), ('永康市', '永康市'), ('义乌市', '义乌市'), ('东阳市', '东阳市'), ('临海市', '临海市'), ('温岭市', '温岭市'), ('瑞安市', '瑞安市'), ('乐清市', '乐清市'), ('龙泉市', '龙泉市'), ('合肥市', '合肥市'), ('芜湖市', '芜湖市'), ('蚌埠市', '蚌埠市'), ('淮南市', '淮南市'), ('马鞍山市', '马鞍山市'), ('淮北市', '淮北市'), ('铜陵市', '铜陵市'), ('安庆市', '安庆市'), ('黄山市', '黄山市'), ('滁州市', '滁州市'), ('阜阳市', '阜阳市'), ('宿州市', '宿州市'), ('六安市', '六安市'), ('亳州市', '亳州市'), ('池州市', '池州市'), ('宣城市', '宣城市'), ('巢湖市', '巢湖市'), ('桐城市', '桐城市'), ('天长市', '天长市'), ('明光市', '明光市'), ('界首市', '界首市'), ('宁国市', '宁国市'), ('厦门市', '厦门市'), ('福州市', '福州市'), ('南平市', '南平市'), ('三明市', '三明市'), ('莆田市', '莆田市'), ('泉州市', '泉州市'), ('漳州市', '漳州市'), ('龙岩市', '龙岩市'), ('宁德市', '宁德市'), ('福清市', '福清市'), ('长乐市', '长乐市'), ('邵武市', '邵武市'), ('武夷山市', '武夷山市'), ('建瓯市', '建瓯市'), ('永安市', '永安市'), ('石狮市', '石狮市'), ('晋江市', '晋江市'), ('南安市', '南安市'), ('龙海市', '龙海市'), ('漳平市', '漳平市'), ('福安市', '福安市'), ('福鼎市', '福鼎市'), ('南昌市', '南昌市'), ('九江市', '九江市'), ('景德镇市', '景德镇市'), ('鹰潭市', '鹰潭市'), ('新余市', '新余市'), ('萍乡市', '萍乡市'), ('赣州市', '赣州市'), ('上饶市', '上饶市'), ('抚州市', '抚州市'), ('宜春市', '宜春市'), ('吉安市', '吉安市'), ('瑞昌市', '瑞昌市'), ('共青城市', '共青城市'), ('乐平市', '乐平市'), ('瑞金市', '瑞金市'), ('德兴市', '德兴市'), ('丰城市', '丰城市'), ('樟树市', '樟树市'), ('高安市', '高安市'), ('井冈山市', '井冈山市'), ('贵溪市', '贵溪市'), ('济南市', '济南市'), ('青岛市', '青岛市'), ('聊城市', '聊城市'), ('德州市', '德州市'), ('东营市', '东营市'), ('淄博市', '淄博市'), ('潍坊市', '潍坊市'), ('烟台市', '烟台市'), ('威海市', '威海市'), ('日照市', '日照市'), ('临沂市', '临沂市'), ('枣庄市', '枣庄市'), ('济宁市', '济宁市'), ('泰安市', '泰安市'), ('莱芜市', '莱芜市'), ('滨州市', '滨州市'), ('菏泽市', '菏泽市'), ('胶州市', '胶州市'), ('即墨市', '即墨市'), ('平度市', '平度市'), ('莱西市', '莱西市'), ('临清市', '临清市'), ('乐陵市', '乐陵市'), ('禹城市', '禹城市'), ('安丘市', '安丘市'), ('昌邑市', '昌邑市'), ('高密市', '高密市'), ('青州市', '青州市'), ('诸城市', '诸城市'), ('寿光市', '寿光市'), ('栖霞市', '栖霞市'), ('海阳市', '海阳市'), ('龙口市', '龙口市'), ('莱阳市', '莱阳市'), ('莱州市', '莱州市'), ('蓬莱市', '蓬莱市'), ('招远市', '招远市'), ('荣成市', '荣成市'), ('乳山市', '乳山市'), ('滕州市', '滕州市'), ('曲阜市', '曲阜市'), ('邹城市', '邹城市'), ('新泰市', '新泰市'), ('肥城市', '肥城市'), ('郑州市', '郑州市'), ('开封市', '开封市'), ('洛阳市', '洛阳市'), ('平顶山市', '平顶山市'), ('安阳市', '安阳市'), ('鹤壁市', '鹤壁市'), ('新乡市', '新乡市'), ('焦作市', '焦作市'), ('濮阳市', '濮阳市'), ('许昌市', '许昌市'), ('漯河市', '漯河市'), ('三门峡市', '三门峡市'), ('南阳市', '南阳市'), ('商丘市', '商丘市'), ('周口市', '周口市'), ('驻马店市', '驻马店市'), ('信阳市', '信阳市'), ('荥阳市', '荥阳市'), ('新郑市', '新郑市'), ('登封市', '登封市'), ('新密市', '新密市'), ('偃师市', '偃师市'), ('孟州市', '孟州市'), ('沁阳市', '沁阳市'), ('卫辉市', '卫辉市'), ('辉县市', '辉县市'), ('林州市', '林州市'), ('禹州市', '禹州市'), ('长葛市', '长葛市'), ('舞钢市', '舞钢市'), ('义马市', '义马市'), ('灵宝市', '灵宝市'), ('项城市', '项城市'), ('巩义市', '巩义市'), ('邓州市', '邓州市'), ('永城市', '永城市'), ('汝州市', '汝州市'), ('济源市', '济源市'), ('武汉市', '武汉市'), ('十堰市', '十堰市'), ('襄阳市', '襄阳市'), ('荆门市', '荆门市'), ('孝感市', '孝感市'), ('黄冈市', '黄冈市'), ('鄂州市', '鄂州市'), ('黄石市', '黄石市'), ('咸宁市', '咸宁市'), ('荆州市', '荆州市'), ('宜昌市', '宜昌市'), ('随州市', '随州市'), ('丹江口市', '丹江口市'), ('老河口市', '老河口市'), ('枣阳市', '枣阳市'), ('宜城市', '宜城市'), ('钟祥市', '钟祥市'), ('汉川市', '汉川市'), ('应城市', '应城市'), ('安陆市', '安陆市'), ('广水市', '广水市'), ('麻城市', '麻城市'), ('武穴市', '武穴市'), ('大冶市', '大冶市'), ('赤壁市', '赤壁市'), ('石首市', '石首市'), ('洪湖市', '洪湖市'), ('松滋市', '松滋市'), ('宜都市', '宜都市'), ('枝江市', '枝江市'), ('当阳市', '当阳市'), ('恩施市', '恩施市'), ('利川市', '利川市'), ('仙桃市', '仙桃市'), ('天门市', '天门市'), ('潜江市', '潜江市'), ('长沙市', '长沙市'), ('衡阳市', '衡阳市'), ('张家界市', '张家界市'), ('常德市', '常德市'), ('益阳市', '益阳市'), ('岳阳市', '岳阳市'), ('株洲市', '株洲市'), ('湘潭市', '湘潭市'), ('郴州市', '郴州市'), ('永州市', '永州市'), ('邵阳市', '邵阳市'), ('怀化市', '怀化市'), ('娄底市', '娄底市'), ('耒阳市', '耒阳市'), ('常宁市', '常宁市'), ('浏阳市', '浏阳市'), ('津市市', '津市市'), ('沅江市', '沅江市'), ('汨罗市', '汨罗市'), ('临湘市', '临湘市'), ('醴陵市', '醴陵市'), ('湘乡市', '湘乡市'), ('韶山市', '韶山市'), ('资兴市', '资兴市'), ('武冈市', '武冈市'), ('洪江市', '洪江市'), ('冷水江市', '冷水江市'), ('涟源市', '涟源市'), ('吉首市', '吉首市'), ('广州市', '广州市'), ('深圳市', '深圳市'), ('清远市', '清远市'), ('韶关市', '韶关市'), ('河源市', '河源市'), ('梅州市', '梅州市'), ('潮州市', '潮州市'), ('汕头市', '汕头市'), ('揭阳市', '揭阳市'), ('汕尾市', '汕尾市'), ('惠州市', '惠州市'), ('东莞市', '东莞市'), ('珠海市', '珠海市'), ('中山市', '中山市'), ('江门市', '江门市'), ('佛山市', '佛山市'), ('肇庆市', '肇庆市'), ('云浮市', '云浮市'), ('阳江市', '阳江市'), ('茂名市', '茂名市'), ('湛江市', '湛江市'), ('英德市', '英德市'), ('连州市', '连州市'), ('乐昌市', '乐昌市'), ('南雄市', '南雄市'), ('兴宁市', '兴宁市'), ('普宁市', '普宁市'), ('陆丰市', '陆丰市'), ('恩平市', '恩平市'), ('台山市', '台山市'), ('开平市', '开平市'), ('鹤山市', '鹤山市'), ('四会市', '四会市'), ('罗定市', '罗定市'), ('阳春市', '阳春市'), ('化州市', '化州市'), ('信宜市', '信宜市'), ('高州市', '高州市'), ('吴川市', '吴川市'), ('廉江市', '廉江市'), ('雷州市', '雷州市'), ('南宁市', '南宁市'), ('桂林市', '桂林市'), ('柳州市', '柳州市'), ('梧州市', '梧州市'), ('贵港市', '贵港市'), ('玉林市', '玉林市'), ('钦州市', '钦州市'), ('北海市', '北海市'), ('防城港市', '防城港市'), ('崇左市', '崇左市'), ('百色市', '百色市'), ('河池市', '河池市'), ('来宾市', '来宾市'), ('贺州市', '贺州市'), ('岑溪市', '岑溪市'), ('桂平市', '桂平市'), ('北流市', '北流市'), ('东兴市', '东兴市'), ('凭祥市', '凭祥市'), ('宜州市', '宜州市'), ('合山市', '合山市'), ('靖西市', '靖西市'), ('海口市', '海口市'), ('三亚市', '三亚市'), ('三沙市', '三沙市'), ('儋州市', '儋州市'), ('文昌市', '文昌市'), ('琼海市', '琼海市'), ('万宁市', '万宁市'), ('东方市', '东方市'), ('五指山市', '五指山市'), ('成都市', '成都市'), ('广元市', '广元市'), ('绵阳市', '绵阳市'), ('德阳市', '德阳市'), ('南充市', '南充市'), ('广安市', '广安市'), ('遂宁市', '遂宁市'), ('内江市', '内江市'), ('乐山市', '乐山市'), ('自贡市', '自贡市'), ('泸州市', '泸州市'), ('宜宾市', '宜宾市'), ('攀枝花市', '攀枝花市'), ('巴中市', '巴中市'), ('达州市', '达州市'), ('资阳市', '资阳市'), ('眉山市', '眉山市'), ('雅安市', '雅安市'), ('崇州市', '崇州市'), ('邛崃市', '邛崃市'), ('都江堰市', '都江堰市'), ('彭州市', '彭州市'), ('江油市', '江油市'), ('什邡市', '什邡市'), ('广汉市', '广汉市'), ('绵竹市', '绵竹市'), ('阆中市', '阆中市'), ('华蓥市', '华蓥市'), ('峨眉山市', '峨眉山市'), ('万源市', '万源市'), ('简阳市', '简阳市'), ('西昌市', '西昌市'), ('康定市', '康定市'), ('马尔康市', '马尔康市'), ('贵阳市', '贵阳市'), ('六盘水市', '六盘水市'), ('遵义市', '遵义市'), ('安顺市', '安顺市'), ('毕节市', '毕节市'), ('铜仁市', '铜仁市'), ('清镇市', '清镇市'), ('赤水市', '赤水市'), ('仁怀市', '仁怀市'), ('凯里市', '凯里市'), ('都匀市', '都匀市'), ('兴义市', '兴义市'), ('福泉市', '福泉市'), ('昆明市', '昆明市'), ('曲靖市', '曲靖市'), ('玉溪市', '玉溪市'), ('丽江市', '丽江市'), ('昭通市', '昭通市'), ('普洱市', '普洱市'), ('临沧市', '临沧市'), ('保山市', '保山市'), ('安宁市', '安宁市'), ('宣威市', '宣威市'), ('芒市', '芒市'), ('瑞丽市', '瑞丽市'), ('大理市', '大理市'), ('楚雄市', '楚雄市'), ('个旧市', '个旧市'), ('开远市', '开远市'), ('蒙自市', '蒙自市'), ('弥勒市', '弥勒市'), ('景洪市', '景洪市'), ('文山市', '文山市'), ('香格里拉市', '香格里拉市'), ('腾冲市', '腾冲市'), ('西安市', '西安市'), ('延安市', '延安市'), ('铜川市', '铜川市'), ('渭南市', '渭南市'), ('咸阳市', '咸阳市'), ('宝鸡市', '宝鸡市'), ('汉中市', '汉中市'), ('榆林市', '榆林市'), ('商洛市', '商洛市'), ('安康市', '安康市'), ('韩城', '韩城'), ('华阴', '华阴'), ('兴平', '兴平'), ('兰州市', '兰州市'), ('嘉峪关市', '嘉峪关市'), ('金昌市', '金昌市'), ('白银市', '白银市'), ('天水市', '天水市'), ('酒泉市', '酒泉市'), ('张掖市', '张掖市'), ('武威市', '武威市'), ('庆阳市', '庆阳市'), ('平凉市', '平凉市'), ('定西市', '定西市'), ('陇南市', '陇南市'), ('玉门市', '玉门市'), ('敦煌市', '敦煌市'), ('临夏市', '临夏市'), ('合作市', '合作市'), ('西宁市', '西宁市'), ('海东市', '海东市'), ('格尔木市', '格尔木市'), ('德令哈市', '德令哈市'), ('玉树市', '玉树市'), ('拉萨市', '拉萨市'), ('日喀则市', '日喀则市'), ('昌都市', '昌都市'), ('林芝市', '林芝市'), ('山南市', '山南市'), ('银川市', '银川市'), ('石嘴山市', '石嘴山市'), ('吴忠市', '吴忠市'), ('中卫市', '中卫市'), ('固原市', '固原市'), ('灵武市', '灵武市'), ('青铜峡市', '青铜峡市'), ('台北市', '台北市'), ('新北市', '新北市'), ('桃园市', '桃园市'), ('台中市', '台中市'), ('台南市', '台南市'), ('高雄市', '高雄市'), ('基隆市', '基隆市'), ('新竹市', '新竹市'), ('嘉义市', '嘉义市'), ('北京市', '北京市'), ('天津市', '天津市'), ('上海市', '上海市'), ('重庆市', '重庆市'), ('香港特别行政区', '香港特别行政区'), ('澳门特别行政区', '澳门特别行政区'), ('乌鲁木齐市', '乌鲁木齐市'), ('克拉玛依市', '克拉玛依市'), ('吐鲁番市', '吐鲁番市'), ('哈密市', '哈密市'), ('喀什市', '喀什市'), ('阿克苏市', '阿克苏市'), ('和田市', '和田市'), ('阿图什市', '阿图什市'), ('阿拉山口市', '阿拉山口市'), ('博乐市', '博乐市'), ('昌吉市', '昌吉市'), ('阜康市', '阜康市'), ('库尔勒市', '库尔勒市'), ('伊宁市', '伊宁市'), ('奎屯市', '奎屯市'), ('塔城市', '塔城市'), ('乌苏市', '乌苏市'), ('阿勒泰市', '阿勒泰市'), ('霍尔果斯市', '霍尔果斯市'), ('石河子市', '石河子市'), ('阿拉尔市', '阿拉尔市'), ('图木舒克市', '图木舒克市'), ('五家渠市', '五家渠市'), ('北屯市', '北屯市'), ('铁门关市', '铁门关市'), ('双河市', '双河市'), ('可克达拉市', '可克达拉市'), ('昆玉市', '昆玉市')], max_length=10, verbose_name='城市')),
            ],
        ),
    ]
