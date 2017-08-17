from scrapy.selector import Selector
import re
st = '''                    <li><a data-id="242" data-key="巴西" href="http://plan.qyer.com/search_0_0_242_0_0_0_1/">巴西</a></li>
                    <li><a data-id="509" data-key="秘鲁" href="http://plan.qyer.com/search_0_0_509_0_0_0_1/">秘鲁</a></li>
                    <li><a data-id="243" data-key="阿根廷" href="http://plan.qyer.com/search_0_0_243_0_0_0_1/">阿根廷</a></li>
                    <li><a data-id="575" data-key="智利" href="http://plan.qyer.com/search_0_0_575_0_0_0_1/">智利</a></li>
                    <li><a data-id="429" data-key="玻利维亚" href="http://plan.qyer.com/search_0_0_429_0_0_0_1/">玻利维亚</a></li>
                    <li><a data-id="453" data-key="哥伦比亚" href="http://plan.qyer.com/search_0_0_453_0_0_0_1/">哥伦比亚</a></li>
                    <li><a data-id="443" data-key="厄瓜多尔" href="http://plan.qyer.com/search_0_0_443_0_0_0_1/">厄瓜多尔</a></li>
                    <li><a data-id="557" data-key="委内瑞拉" href="http://plan.qyer.com/search_0_0_557_0_0_0_1/">委内瑞拉</a></li>
                    <li><a data-id="561" data-key="乌拉圭" href="http://plan.qyer.com/search_0_0_561_0_0_0_1/">乌拉圭</a></li>
                    <li><a data-id="415" data-key="巴拉圭" href="http://plan.qyer.com/search_0_0_415_0_0_0_1/">巴拉圭</a></li>
                    <li><a data-id="1293" data-key="苏里南" href="http://plan.qyer.com/search_0_0_1293_0_0_0_1/">苏里南</a></li>
                    <li><a data-id="449" data-key="福克兰群岛（马尔维纳斯群岛）" href="http://plan.qyer.com/search_0_0_449_0_0_0_1/">福克兰群岛（马尔维纳斯群岛）</a></li>
                    <li><a data-id="460" data-key="圭亚那" href="http://plan.qyer.com/search_0_0_460_0_0_0_1/">圭亚那</a></li>
                    <li><a data-id="1292" data-key="法属圭亚那" href="http://plan.qyer.com/search_0_0_1292_0_0_0_1/">法属圭亚那</a></li>
          '''
city = '''
  window.__pageData__ = {
    citys:[
            {id:'64',name:'里约热内卢',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=64'},
            {id:'6842',name:'圣保罗',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6842'},
            {id:'10362',name:'伊瓜苏市',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=10362'},
            {id:'6823',name:'马瑙斯',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6823'},
            {id:'6809',name:'巴西利亚',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6809'},
            {id:'6830',name:'萨尔瓦多',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6830'},
            {id:'6821',name:'库里蒂巴',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6821'},
            {id:'6814',name:'大坎普',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6814'},
            {id:'6813',name:'博尼图',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6813'},
            {id:'6810',name:'贝洛奥里藏特',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6810'},
            {id:'6805',name:'阿雷格里港',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6805'},
            {id:'6826',name:'欧鲁普雷图',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6826'},
            {id:'6834',name:'圣卡塔琳娜州',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6834'},
            {id:'11319',name:'库亚巴',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=11319'},
            {id:'10341',name:'巴西圣路易斯',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=10341'},
            {id:'6822',name:'累西腓',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6822'},
            {id:'10342',name:'巴西贝伦',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=10342'},
            {id:'6838',name:'乌巴图巴',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6838'},
            {id:'6817',name:'福塔莱萨',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6817'},
            {id:'6815',name:'迪亚曼蒂纳',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6815'},
            {id:'6804',name:'阿拉卡茹',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6804'},
            {id:'13991',name:'弗洛里亚诺波利斯',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=13991'},
            {id:'6825',name:'纳塔尔',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6825'},
            {id:'6807',name:'奥林达',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6807'},
            {id:'6806',name:'安格拉-杜斯雷斯',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6806'},
            {id:'10339',name:'马赛约',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=10339'},
          ],
      level:[
            {text:'一级精华',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?elite=1'},
            {text:'二级精华',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?elite=2'},
            {text:'三级精华',url:'http://plan.qyer.com/search_0_0_242_0_0_0_1/?elite=3'},
          ],
'''
name_pattern = re.compile(u'<a data-id="\d*" data-key="\D*" href="(http://.*)">.*</a>')

city_pattern = re.compile(u'{id:\'\d*\',name:\'\D*\',url:\'(http:.*)\'}')


test = '''

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="keywords" content="旅游行程安排,旅游线路推荐,行程单,穷游行程助手">
  <meta name="description" content="穷游行程助手：为旅行者提供最佳旅游线路推荐，旅游线路规划，详细旅游行程安排，并支持一键导出行程单，方便随时查看及送签使用。">
  <meta name="google-site-verification"
        content="DVVM1p1HEm8vE1wVOQ9UjcKP--pNAsg_pleTU5TkFaM">
  <title>旅游线路推荐_旅游行程安排规划_一键导出行程单 - 穷游行程助手</title>
  <link rel="shortcut icon" href="//www.qyer.com/favicon.ico">
  <link rel="stylesheet" href="//common2.qyerstatic.com/plan/desktop/home/css/style.61bf817d75b39188df4010786f85adc3.css">
  <script>
    window.QYER = {
      uid: [0][0] || 0
    };
    window._RATrack = window._RATrack||{
      'platform': 'web',
      'channel':'plan',
      'page_type':'index',
      'ugc_type':'plan_index',
      'ugc_content':''
    };
  </script>
  
<script>
  window.__pageData__ = {
    citys:[
          ],
      level:[
            {text:'一级精华',url:'http://plan.qyer.com/search_0_0_0_0_0_0_1/?elite=1'},
            {text:'二级精华',url:'http://plan.qyer.com/search_0_0_0_0_0_0_1/?elite=2'},
            {text:'三级精华',url:'http://plan.qyer.com/search_0_0_0_0_0_0_1/?elite=3'},
          ],
    urlParameter:{
      startTime:'0',
      place:'0',
      datCount:'0',
      topic:'0',
      city:'0',
      essence:'0',
      order:'0',
      page:'0',
      kw:'0'
    },
    t :1501645914
    //1468209600
  };
</script>
<style type="text/css">
  .q-layer-header .logo{width: auto!important;}
</style>

  <script src="//common1.qyerstatic.com/plan/desktop/shared/js/header.8ca03cdbf7c946554afe9b49f686ef20.js"></script>
</head>
<body>
  

      





<style>
    .tip_passport_bindmobile{height: 40px; line-height: 40px; background-color: rgb(224, 241, 223); font-size: 14px; padding-left: 28px; position: relative; margin-top: -40px;transition:All .3s ease; -webkit-transition:All .3s ease; -moz-transition:All .3s ease; -o-transition:All .3s ease;color:#323232;}
    .tip_passport_bindmobile a{color: #323232; text-decoration: underline;}
    .tip_passport_bindmobile img{width:12px;height:12px;position: absolute; top: 15px; right: 17px; cursor: pointer; }

    .tip_passport_bindmobile_masker{position:fixed;top:0;left:0;width:100%;height:100%;background-image:url(//static.qyer.com/models/common/images/bg_255_255_255_0.7.png);z-index:2000;display: none; }
    .tip_passport_bindmobile_dialog{box-sizing: border-box; width: 340px; height: 180px; border: solid 1px rgb(192, 192, 192); background-color: rgb(255, 255, 255); box-shadow: 0 0 10px #ccc; position: absolute; top: 50%; left: 50%; margin: -90px 0 0 -170px; padding: 30px 20px 0 20px; } 
    .tip_passport_bindmobile_dialog_title{font-size: 18px;color: #323232;text-align: center;margin-bottom: 5px; } 
    .tip_passport_bindmobile_dialog_text{font-size: 14px;color: #959595;}
    .tip_passport_bindmobile_dialog_btn{width:84px;height:28px;line-height:28px;display:inline-block;font-size:14px;color:rgb(50,50,50);text-decoration:none !important;margin-top:15px;background-color:rgb(236,236,236);border:solid 1px rgb(192,192,192);cursor:pointer;border-radius:3px;}
    .tip_passport_bindmobile_dialog_btn:hover{background-color:rgb(243,243,243);}
    .tip_passport_bindmobile_dialog_btnBind{margin-left:20px; background-color:rgb(59,160,92); border:solid 1px rgb(59,160,92); color:#fff; }
    .tip_passport_bindmobile_dialog_btnBind:hover{background-color:rgb(71,197,113); border:solid 1px rgb(71,197,113); }
    .tip_passport_bindmobile_dialog_close{position:absolute;top:16px;right:16px;cursor:pointer;}
</style>
<div id="tip_passport_bindmobile" class="tip_passport_bindmobile">
	<span>
		穷游网将实行手机绑定实名制，为了您的帐号安全请及时绑定手机号。
    	<a target="_blank" href="//bbs.qyer.com/thread-2779523-1.html">查看详细说明</a>
	</span>
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpBRjUzNThGRDU3QkQxMUU3QjUyQ0M1QkZCNDUzNkFCOCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpBRjUzNThGRTU3QkQxMUU3QjUyQ0M1QkZCNDUzNkFCOCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkFGNTM1OEZCNTdCRDExRTdCNTJDQzVCRkI0NTM2QUI4IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkFGNTM1OEZDNTdCRDExRTdCNTJDQzVCRkI0NTM2QUI4Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Lb1GqgAAAKlJREFUeNqckkEOwiAQRQc8GFvO0AULjNF4IKMx7aILz9AlHMdDGPyYT0MomzrJD014bwJMVQjhLSIL4o0xH+lUjPGAZUKsJuyQmRs9eCazZMEjL2RopQoeyHiVUmo3RuRE54kcCbt85J9QdXsQuFO4sMG53G8VKCksN4JC8Qp4hbTsrP+OtOvSGFz7dK506zyr05zgBs7Fb1fNacqCLZPs/RqVlBn7FWAASJhkb97XPw8AAAAASUVORK5CYII=" />
</div>
<div id="tip_passport_bindmobile_masker" class="tip_passport_bindmobile_masker">
    <div class="tip_passport_bindmobile_dialog">
        <h5 class="tip_passport_bindmobile_dialog_title">帐号安全提示</h5>
        <p class="tip_passport_bindmobile_dialog_text">穷游网将实行手机绑定实名制，为了您的帐号安全，请及时绑定手机号。</p>
        <div style="text-align:center;"> 
            <a class="tip_passport_bindmobile_dialog_btn" href="//bbs.qyer.com/thread-2779523-1.html" target="_blank" >查看说明</a>
            <a class="tip_passport_bindmobile_dialog_btn tip_passport_bindmobile_dialog_btnBind"  href="//passport.qyer.com/account/mobile/bind" target="_blank" >立即绑定</a>
        </div>
        <img id="tip_passport_bindmobile_dialog_close" class="tip_passport_bindmobile_dialog_close" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpBNTMyODU3OTU5OEExMUU3QTgwMUVFNzYzN0YwQkI1NSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpBNTMyODU3QTU5OEExMUU3QTgwMUVFNzYzN0YwQkI1NSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkE1MzI4NTc3NTk4QTExRTdBODAxRUU3NjM3RjBCQjU1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkE1MzI4NTc4NTk4QTExRTdBODAxRUU3NjM3RjBCQjU1Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+jb9fzQAAAKlJREFUeNqckkEOwiAQRQc8GFvO0AULjNF4IKMx7aILz9AlHMdDGPyYT0MomzrJD014bwJMVQjhLSIL4o0xH+lUjPGAZUKsJuyQmRs9eCazZMEjL2RopQoeyHiVUmo3RuRE54kcCbt85J9QdXsQuFO4sMG53G8VKCksN4JC8Qp4hbTsrP+OtOvSGFz7dK506zyr05zgBs7Fb1fNacqCLZPs/RqVlBn7FWAASJhkb97XPw8AAAAASUVORK5CYII=" />
    </div>
</div>
<script>
    (function(){

        function setCookie(name, value,time) {
            var exp = new Date();
            exp.setTime(exp.getTime() + (time||259200000));
            document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString() + ";path=/;domain=qyer.com";
        };
        function getCookie(objName){
            var arrStr = document.cookie.split("; ");
            for(var i = 0;i < arrStr.length;i ++){
                var temp = arrStr[i].split("=");
                if(temp[0] == objName) return unescape(temp[1]);
           } 
        }

        window.__userStatusCallBack = function (data) {

            // 显示通栏
            (function(){
                var isShowTopTip = data.uid 
                            && data.userinfo.bind_phone!=1 
                            && getCookie('tip_passport_bindmobile')!="1"
                            && !/^https?:\/\/qyer\.com/gi.test(location.href)
                            ;
                // 显示顶部提示
                if(isShowTopTip){
                    var $dom = $('#tip_passport_bindmobile');
                    $dom.css('marginTop','0').find('img').click(function(){
                        $dom.css('marginTop','-40px');
                        setCookie('tip_passport_bindmobile',1);
                    })

                }
            })();


            // 增加 UGC 监听，关键操作出现绑定账号提示
            (function(){
                if(data.uid && data.userinfo.bind_phone!=1 ){
                    // modal 关闭事件
                    $('#tip_passport_bindmobile_dialog_close').on('click',function(){
                        $('#tip_passport_bindmobile_masker').remove();
                        setCookie('tip_passport_ugc_bindmobile',1);
                    });

                    // 代理全局 mousedown 事件，判断用户行为，进行绑定弹窗提示
                    var filter = [
                        '[data-bn-ipg=index-head-userdrop-poicomment]', // 写点评
                        '.cfsub.cn-pub', // 写帖子
                        '.ask_askhelp_btn', // 提问
                        '[data-bn-ipg=planhome-createplan]', // 创建行程-自己制定
                        '[data-bn-ipg=planhome-1-createplan-bymyself]', // 创建行程-自己制定
                        '[data-bn-ipg=planhome-1-createplan-createforme]', // 创建行程-帮我制定
                        '#addPhoto.ui-button.btn-default-full.btn-upload', // 上传图片
                    ].join(',')
                    $(document.body).on('mousedown',filter,function(){
                        if( getCookie('tip_passport_ugc_bindmobile') != '1' ){
                            $('#tip_passport_bindmobile_masker').show();
                            return false;
                        }
                    });
                }
            })();

        }
    })();
</script>

<script>
	window.QYER={uid:[0][0]||0};

	window._RATrack = window._RATrack||{
	 	'platform':'web',
 		'channel':'plan',
	 	'page_type':'index',
 		'ugc_type':'plan_index',
	 	'ugc_content':''
	};
</script>

<link href="//static.qyer.com/models/common/component/headfoot/dist/headerfoot_black.min.css"  rel="stylesheet" />
<script src="//static.qyer.com/models/common/component/headfoot/dist/headerfoot_black.min.js" async="async"></script>




<div class="q-layer-header">
    <div class="header-inner">
        <a data-bn-ipg="head-logo" href="//www.qyer.com"><img class="logo" src="//static.qyer.com/models/common/component/headfoot/icon/logo_116x36.png" width="58" height="18" /></a>
        <div class="nav">
            <ul class="nav-ul">
                <li class="nav-list "><a class="nav-span" href="//place.qyer.com/" data-bn-ipg="head-nav-place" title="穷游目的地">目的地</a></li>
                <li class="nav-list "><a class="nav-span" href="//guide.qyer.com/" data-bn-ipg="head-nav-guide" title="穷游锦囊">锦囊</a></li>
                <li class="nav-list nav-list-plan nav-list-selected">
                    <a class="nav-span" href="//plan.qyer.com/" data-bn-ipg="head-nav-plan" title="穷游行程助手">行程助手</a>
                </li>
                <li class="nav-list nav-list-layer  ">
                    <a class="nav-span" href="//bbs.qyer.com/" data-bn-ipg="head-nav-community" title="穷游论坛">社区<i class="iconfont icon-jiantouxia"></i></a>
                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li class="nav-list-layer">
                                <a href="//bbs.qyer.com" data-bn-ipg="head-nav-bbs" title="穷游论坛"><i class="iconfont icon-bbs1"></i> 旅行论坛 <i class="iconfont icon-jiantouyou"></i></a>
                                <div class="q-layer q-layer-section">
                                    <div class="q-layer">
                                        <div class="section-title">
                                            <a class="more" href="//bbs.qyer.com">全部版块<i class="iconfont icon-jiantouyou"></i></a>
                                            <span>热门版块</span>
                                        </div>


                                                                                                                           <dl class="section-item">
                                             <dt>兴趣小组</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-2" href="//bbs.qyer.com/forum-2-1.html">结伴同游</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-3" href="//bbs.qyer.com/forum-3-1.html">签证</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-22" href="//bbs.qyer.com/forum-22-1.html">旅行摄影</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-88" href="//bbs.qyer.com/forum-88-1.html">潜水俱乐部</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-122" href="//bbs.qyer.com/forum-122-1.html">带孩子旅行</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-49" href="//bbs.qyer.com/forum-49-1.html">明信片</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-100" href="//bbs.qyer.com/forum-100-1.html">旅行购物</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游欧洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-14" href="//bbs.qyer.com/forum-14-1.html">法国/摩纳哥</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-12" href="//bbs.qyer.com/forum-12-1.html">德国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-16" href="//bbs.qyer.com/forum-16-1.html">英国/爱尔兰</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-15" href="//bbs.qyer.com/forum-15-1.html">瑞士/列支敦士登</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-162" href="//bbs.qyer.com/forum-162-1.html">土耳其</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-25" href="//bbs.qyer.com/forum-25-1.html">挪威/瑞典/芬兰/丹麦/冰岛</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-13" href="//bbs.qyer.com/forum-13-1.html">意大利/梵蒂冈/圣马力诺/马耳他</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游亚洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-52" href="//bbs.qyer.com/forum-52-1.html">台湾</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-57" href="//bbs.qyer.com/forum-57-1.html">日本</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-106" href="//bbs.qyer.com/forum-106-1.html">泰国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-164" href="//bbs.qyer.com/forum-164-1.html">新加坡</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-165" href="//bbs.qyer.com/forum-165-1.html">斯里兰卡</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-163" href="//bbs.qyer.com/forum-163-1.html">香港/澳门</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-108" href="//bbs.qyer.com/forum-108-1.html">马来西亚/文莱</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-175" href="//bbs.qyer.com/forum-175-1.html">柬埔寨</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-104" href="//bbs.qyer.com/forum-104-1.html">马尔代夫</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-177" href="//bbs.qyer.com/forum-177-1.html">缅甸</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-59" href="//bbs.qyer.com/forum-59-1.html">伊朗</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-103" href="//bbs.qyer.com/forum-103-1.html">印度/孟加拉</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游美洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-54" href="//bbs.qyer.com/forum-54-1.html">加拿大</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-53" href="//bbs.qyer.com/forum-53-1.html">美国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-168" href="//bbs.qyer.com/forum-168-1.html">中美</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-55" href="//bbs.qyer.com/forum-55-1.html">南美/南极</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游大洋洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-56" href="//bbs.qyer.com/forum-56-1.html">澳大利亚</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-83" href="//bbs.qyer.com/forum-83-1.html">新西兰</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-178" href="//bbs.qyer.com/forum-178-1.html">太平洋海岛</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游非洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-173" href="//bbs.qyer.com/forum-173-1.html">东非地区</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-174" href="//bbs.qyer.com/forum-174-1.html">非洲海岛</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-86" href="//bbs.qyer.com/forum-86-1.html">北非地区</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-60" href="//bbs.qyer.com/forum-60-1.html">非洲其他国家</a>
                                                                                              </dd>
                                         </dl>
                                         

                                    </div>
                                </div>
                            </li>
                            <li><a href="//ask.qyer.com/" data-bn-ipg="head-nav-ask" title="旅行问答"><i class="iconfont icon-ask1"></i> 旅行问答</a></li>
                            <li><a href="//jne.qyer.com/" data-bn-ipg="head-nav-qlab" title="JNE旅行生活美学" target="_blank"><i class="iconfont icon-jne1"></i> JNE旅行生活美学</a></li>
                            <li><a href="//zt.qyer.com/" data-bn-ipg="head-nav-zt" title="特别策划" target="_blank"><i class="iconfont icon-zt"></i> 特别策划</a></li>
                            <li><a href="//rt.qyer.com/" data-bn-ipg="head-nav-rt" title="负责任的旅行" target="_blank"><i class="iconfont icon-rt1"></i> 负责任的旅行</a></li>
                        </ul>
                    </div>
                </li>

                <li class="nav-list nav-list-layer nav-list-zuishijie ">
                    <a class="nav-span" href="//z.qyer.com/" data-bn-ipg="head-nav-lastminute" title="穷游商城">穷游商城<i class="iconfont icon-jiantouxia"></i></a>
                    <div class="gif">
                        <img class="gif1" src="//static.qyer.com/models/common/component/headfoot/icon/gif.gif" height="19" width="44" >
                    </div>

                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li><a href="//z.qyer.com/package/" data-bn-ipg="head-nav-package" target="_blank" title="机酒自由行"><i class="iconfont icon-package"></i> 机酒自由行</a></li>
                            <li><a href="//z.qyer.com/local/" data-bn-ipg="head-nav-local" target="_blank" title="当地玩乐"><i class="iconfont icon-local"></i> 当地玩乐</a></li>
                            <li><a href="//z.qyer.com/visa/" data-bn-ipg="head-nav-visa" target="_blank" title="签证"><i class="iconfont icon-visa1"></i> 签证</a></li>
                            <li><a href="//z.qyer.com/cruise/" data-bn-ipg="head-nav-cruise" target="_blank" title="邮轮"><i class="iconfont icon-cruise"></i> 邮轮</a></li>
                            <li><a href="//z.qyer.com/explore/" data-bn-ipg="head-nav-explore" target="_blank" title="深度旅行"><i class="iconfont icon-explore"></i> 深度旅行</a></li>
                            <li><a href="//bx.qyer.com/" data-bn-ipg="head-nav-insure" target="_blank" title="保险"><i class="iconfont icon-bx"></i> 保险</a></li>
                            <li><a href="//z.qyer.com/travelgroup" data-bn-ipg="head-nav-travelgroup" target="_blank" title="私人订制"><i class="iconfont icon-travelgroup"></i> 私人定制</a></li>
                        </ul>
                    </div>
                </li>

                <li class="nav-list "><a class="nav-span" href="//flight.qyer.com/" data-bn-ipg="head-nav-plane" title="机票">机票</a></li>

                <li class="nav-list "><a class="nav-span" href="//hotel.qyer.com/" data-bn-ipg="head-nav-hotel" title="穷游酒店">酒店</a></li>

                <li class="nav-list nav-list-layer nav-list-yuding">
                    <span class="nav-span">预订<i class="iconfont icon-jiantouxia"></i></span>
                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li><a href="//www.qyer.com/hoteldeal/" data-bn-ipg="head-nav-hoteldeal" title="特价酒店"><i class="iconfont icon-hoteldeal"></i> 特价酒店</a></li>
                            <li><a href="//www.qyer.com/goto.php?url=https%3A%2F%2Fwww.airbnbchina.cn%2F%3Faf%3D104561116%26c%3DRESERVATION" data-bn-ipg="head-nav-airbnb" title="爱彼迎" target="_blank"><i class="iconfont icon-airbnb1"></i> 爱彼迎</a></li>
                            <li><a href="//www.qyer.com/shop/" data-bn-ipg="head-nav-shop" title="华人旅馆"><i class="iconfont icon-shop"></i> 华人旅馆</a></li>
                            <li><a href="//z.qyer.com/car/?utm_source=c03729731-pc&utm_medium=partner&utm_campaign=entry&utm_term=qyer_nav" data-bn-ipg="head-nav-car" title="租车"><i class="iconfont icon-car"></i> 租车</a></li>
                        </ul>
                    </div>
                </li>
                <!-- <li class="nav-list"><a class="nav-span icon-phone-a" href="//app.qyer.com"><i class="iconfont icon-phone"></i>手机穷游</a></li> -->
            </ul>
        </div>
        <div class="fun">
            <div id="siteSearch" class="nav-search">
                <form action="//search.qyer.com/index" method="get">
                    <input class="txt" name="wd" type="text" autocomplete="off">
                    <button class="btn" type="submit"><i class="iconfont icon-sousuo"></i><span>搜索</span></button>
                </form>
            </div>
            <div id="js_qyer_header_userStatus" class="status">
              <div class="login show">
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/" rel="noflow" data-bn-ipg="index-head-un-qq" data-type="qq"><i class="iconfont icon-qq"></i></a>
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/" rel="noflow" data-bn-ipg="index-head-un-weibo" data-type="weibo"><i class="iconfont icon-weibo"></i></a>
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/" rel="noflow" data-bn-ipg="index-head-un-wechat" data-type="weixin"><i class="iconfont icon-weixin"></i></a>

                    <a href="https://passport.qyer.com/register/mobile?refer=http://plan.qyer.com%2F" data-bn-ipg="index-head-un-register">注册</a>
                    <a href="https://passport.qyer.com/login?refer=http://plan.qyer.com%2F" data-bn-ipg="index-head-un-login">登录</a>
              </div>
            </div>
        </div>
    </div>
</div>

<!--token:d41d8cd98f00b204e9800998ecf8427e-->  
  <!-- <div id="updateTip" style="position: absolute; top: 57px; left:0; right:0; background-color: #ffffe4; border: solid 1px #ffd992; text-align: center; height: 53px; line-height: 53px; font-size: 18px; color: #323232; padding: 0 20px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;z-index:100000;max-width:1024px;margin:0 auto;">
      因维护升级，7.24日23点至次日6点（北京时间），行程助手可能出现服务异常，抱歉带来不便。
      <div style="position: absolute; right: 9px; top: -10px; font-size: 12px; cursor: pointer; font-weight: bold; color: #6d6d66; " onclick="$('#updateTip').remove()" >X</div>
  </div> -->

  
      <div class="we_head">
        <ul>
          <li><a href="//bbs.qyer.com/thread-2482054-1.html" target="_blank" data-bn-ipg="Planhome-menu-help">使用帮助</a></li>
          <li><a href="http://app.qyer.com/plan/" target="_blank" data-bn-ipg="Planhome-menu-app">APP下载</a></li>
          <li style="width: 110px"><a href="//plan.qyer.com/tailormade/?source=2" target="_blank" data-bn-ipg="Planhome-menu-tailor">免费私人定制</a></li>
          <li><a href="http://business.qyer.com/" target="_blank" data-bn-ipg="Planhome-menu-business">企业版</a></li>
        </ul>
        <a href="/" class="we_logo" data-bn-ipg="Planhome-LOGO"></a>
      </div>
      <div class="xl-index-banner-2">
        <!-- <span class="num-wrap">
          
            <span class="nums_tip">
              <span>5</span>
            </span>
            <span class="nums_tip">
              <span>7</span>
            </span>
          
        </span> -->

        <div class="xl-index-banner-2-inner">
          <div class="one-minit"></div>
          <div class="counter">
            共有 <span id="user_nums"></span> 万穷游er,创建了 <!-- <span id="counter_num"></span> --> <span class="num-wrap"></span> 个行程
          </div>
            <span class="doodle-bg">
              <span class="doodle">
                <img class="no_moon" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_moon.png" />
                <img class="no_hill" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_hill.png" />
                <img class="no_road" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_road.png" />
                <img class="no_cloud" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_cloud.png" />
                <img class="no_tree" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_tree.png" />
                <img class="no_stone" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_stone.png" />
                <img class="no_plan_sd home-doodle-sd" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_plan_sd.png" />
                <img class="no_plan home-doodle" src="//common3.qyerstatic.com/plan/desktop/home/img/doodles/d_plan.png" />
              </span>
            </span>
            <a href="/create" class="btn-0 btn-1 " data-bn-ipg="planhome-createplan" id="createBtn"  target="_blank"><i class="leftIcon">&#xe63f;</i>创建新的行程</a>
                    </div>
      </div>
      <!--ad-->
      <div class="ad_zone advertising" style="width:980px;height:130px;" id="zoneid-16" data-countries="" data-areas=""></div>
      <!--/ad-->


    <!--精品行程-->
        <!--/精品行程-->

    <div class="index-content-bg">
    <div class="ind_titles fontYaHei">不想自己做行程，为什么不看看别人的？</div>
  
  <!-- 首页筛选 -->
  <div class="ind_sifter">
    
    

        <div class="items clearfix">
      <strong class="title">
        目的地:
      </strong>
          <div id="js_placeList" class="list clearfix">
                      <a data-bn-ipg="planhome-select-country1" data-id="50" data-key="香港" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/?cityid=50">香港</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="51" data-key="澳门" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/?cityid=51">澳门</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11186" data-key="台湾" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/?cityid=11186">台湾</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="215" data-key="泰国" href="http://plan.qyer.com/search_0_0_215_0_0_0_1/">泰国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="14" data-key="日本" href="http://plan.qyer.com/search_0_0_14_0_0_0_1/">日本</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="186" data-key="法国" href="http://plan.qyer.com/search_0_0_186_0_0_0_1/">法国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="189" data-key="意大利" href="http://plan.qyer.com/search_0_0_189_0_0_0_1/">意大利</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="233" data-key="韩国" href="http://plan.qyer.com/search_0_0_233_0_0_0_1/">韩国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="213" data-key="马来西亚" href="http://plan.qyer.com/search_0_0_213_0_0_0_1/">马来西亚</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="236" data-key="美国" href="http://plan.qyer.com/search_0_0_236_0_0_0_1/">美国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="15" data-key="德国" href="http://plan.qyer.com/search_0_0_15_0_0_0_1/">德国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="232" data-key="新加坡" href="http://plan.qyer.com/search_0_0_232_0_0_0_1/">新加坡</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="182" data-key="西班牙" href="http://plan.qyer.com/search_0_0_182_0_0_0_1/">西班牙</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="13" data-key="英国" href="http://plan.qyer.com/search_0_0_13_0_0_0_1/">英国</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="524" data-key="瑞士" href="http://plan.qyer.com/search_0_0_524_0_0_0_1/">瑞士</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="219" data-key="柬埔寨" href="http://plan.qyer.com/search_0_0_219_0_0_0_1/">柬埔寨</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="198" data-key="奥地利" href="http://plan.qyer.com/search_0_0_198_0_0_0_1/">奥地利</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="200" data-key="荷兰" href="http://plan.qyer.com/search_0_0_200_0_0_0_1/">荷兰</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="240" data-key="澳大利亚" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/">澳大利亚</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="216" data-key="越南" href="http://plan.qyer.com/search_0_0_216_0_0_0_1/">越南</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="804" data-key="梵蒂冈" href="http://plan.qyer.com/search_0_0_804_0_0_0_1/">梵蒂冈</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="570" data-key="印度尼西亚" href="http://plan.qyer.com/search_0_0_570_0_0_0_1/">印度尼西亚</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="193" data-key="捷克" href="http://plan.qyer.com/search_0_0_193_0_0_0_1/">捷克</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="424" data-key="比利时" href="http://plan.qyer.com/search_0_0_424_0_0_0_1/">比利时</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="446" data-key="菲律宾" href="http://plan.qyer.com/search_0_0_446_0_0_0_1/">菲律宾</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="195" data-key="土耳其" href="http://plan.qyer.com/search_0_0_195_0_0_0_1/">土耳其</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="241" data-key="新西兰" href="http://plan.qyer.com/search_0_0_241_0_0_0_1/">新西兰</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="206" data-key="希腊" href="http://plan.qyer.com/search_0_0_206_0_0_0_1/">希腊</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="238" data-key="加拿大" href="http://plan.qyer.com/search_0_0_238_0_0_0_1/">加拿大</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="208" data-key="俄罗斯" href="http://plan.qyer.com/search_0_0_208_0_0_0_1/">俄罗斯</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="207" data-key="匈牙利" href="http://plan.qyer.com/search_0_0_207_0_0_0_1/">匈牙利</a>
              </div>
      <div class="seting destination">
        <a id="js_placeToggleLink" href="javascript:;" class="moreBtn setMore js_cmd" data-cmd="place_more" data-status="open" data-bn-ipg="planhome-select-city-more">
          更多
        </a>
      </div>
    </div>
    
    <div id="js_selectCountry" class="selectCountry" style="display:none">
      <div class="tab">
        <ul class="fontYaHei">
          <li class="js_cmd current" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country" class="current"> 亚洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 欧洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 非洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 北美洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 南美洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 大洋洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 南极洲 </li>
        </ul>
        <div class="close" data-bn-ipg="planhome-select-continent-close">
          <span class="js_cmd" data-cmd="place_close2"> </span>
        </div>
        <div class="search">
          <input type="text" id="search_city" class="ui2_input" placeholder="搜索你想要去的国家"
          data-bn-ipg="planhome-select-more-searchcountry">
        </div>
      </div>
      <div id="js_continents" class="tabMain"  >
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="11" data-key="中国" href="http://plan.qyer.com/search_0_0_11_0_0_0_1/">中国</a></li>
                    <li><a data-id="215" data-key="泰国" href="http://plan.qyer.com/search_0_0_215_0_0_0_1/">泰国</a></li>
                    <li><a data-id="14" data-key="日本" href="http://plan.qyer.com/search_0_0_14_0_0_0_1/">日本</a></li>
                    <li><a data-id="233" data-key="韩国" href="http://plan.qyer.com/search_0_0_233_0_0_0_1/">韩国</a></li>
                    <li><a data-id="213" data-key="马来西亚" href="http://plan.qyer.com/search_0_0_213_0_0_0_1/">马来西亚</a></li>
                    <li><a data-id="232" data-key="新加坡" href="http://plan.qyer.com/search_0_0_232_0_0_0_1/">新加坡</a></li>
                    <li><a data-id="219" data-key="柬埔寨" href="http://plan.qyer.com/search_0_0_219_0_0_0_1/">柬埔寨</a></li>
                    <li><a data-id="216" data-key="越南" href="http://plan.qyer.com/search_0_0_216_0_0_0_1/">越南</a></li>
                    <li><a data-id="570" data-key="印度尼西亚" href="http://plan.qyer.com/search_0_0_570_0_0_0_1/">印度尼西亚</a></li>
                    <li><a data-id="446" data-key="菲律宾" href="http://plan.qyer.com/search_0_0_446_0_0_0_1/">菲律宾</a></li>
                    <li><a data-id="220" data-key="尼泊尔" href="http://plan.qyer.com/search_0_0_220_0_0_0_1/">尼泊尔</a></li>
                    <li><a data-id="402" data-key="阿联酋" href="http://plan.qyer.com/search_0_0_402_0_0_0_1/">阿联酋</a></li>
                    <li><a data-id="537" data-key="斯里兰卡" href="http://plan.qyer.com/search_0_0_537_0_0_0_1/">斯里兰卡</a></li>
                    <li><a data-id="497" data-key="马尔代夫" href="http://plan.qyer.com/search_0_0_497_0_0_0_1/">马尔代夫</a></li>
                    <li><a data-id="231" data-key="印度" href="http://plan.qyer.com/search_0_0_231_0_0_0_1/">印度</a></li>
                    <li><a data-id="511" data-key="缅甸" href="http://plan.qyer.com/search_0_0_511_0_0_0_1/">缅甸</a></li>
                    <li><a data-id="487" data-key="老挝" href="http://plan.qyer.com/search_0_0_487_0_0_0_1/">老挝</a></li>
                    <li><a data-id="568" data-key="伊朗" href="http://plan.qyer.com/search_0_0_568_0_0_0_1/">伊朗</a></li>
                    <li><a data-id="476" data-key="卡塔尔" href="http://plan.qyer.com/search_0_0_476_0_0_0_1/">卡塔尔</a></li>
                    <li><a data-id="569" data-key="以色列" href="http://plan.qyer.com/search_0_0_569_0_0_0_1/">以色列</a></li>
                    <li><a data-id="572" data-key="约旦" href="http://plan.qyer.com/search_0_0_572_0_0_0_1/">约旦</a></li>
                    <li><a data-id="436" data-key="朝鲜" href="http://plan.qyer.com/search_0_0_436_0_0_0_1/">朝鲜</a></li>
                    <li><a data-id="558" data-key="文莱" href="http://plan.qyer.com/search_0_0_558_0_0_0_1/">文莱</a></li>
                    <li><a data-id="507" data-key="蒙古" href="http://plan.qyer.com/search_0_0_507_0_0_0_1/">蒙古</a></li>
                    <li><a data-id="414" data-key="巴基斯坦" href="http://plan.qyer.com/search_0_0_414_0_0_0_1/">巴基斯坦</a></li>
                    <li><a data-id="488" data-key="黎巴嫩" href="http://plan.qyer.com/search_0_0_488_0_0_0_1/">黎巴嫩</a></li>
                    <li><a data-id="508" data-key="孟加拉国" href="http://plan.qyer.com/search_0_0_508_0_0_0_1/">孟加拉国</a></li>
                    <li><a data-id="532" data-key="沙特阿拉伯" href="http://plan.qyer.com/search_0_0_532_0_0_0_1/">沙特阿拉伯</a></li>
                    <li><a data-id="2041" data-key="巴勒斯坦" href="http://plan.qyer.com/search_0_0_2041_0_0_0_1/">巴勒斯坦</a></li>
                    <li><a data-id="461" data-key="哈萨克斯坦" href="http://plan.qyer.com/search_0_0_461_0_0_0_1/">哈萨克斯坦</a></li>
                    <li><a data-id="433" data-key="不丹" href="http://plan.qyer.com/search_0_0_433_0_0_0_1/">不丹</a></li>
                    <li><a data-id="416" data-key="巴林" href="http://plan.qyer.com/search_0_0_416_0_0_0_1/">巴林</a></li>
                    <li><a data-id="403" data-key="阿曼" href="http://plan.qyer.com/search_0_0_403_0_0_0_1/">阿曼</a></li>
                    <li><a data-id="562" data-key="乌兹别克斯坦" href="http://plan.qyer.com/search_0_0_562_0_0_0_1/">乌兹别克斯坦</a></li>
                    <li><a data-id="564" data-key="叙利亚" href="http://plan.qyer.com/search_0_0_564_0_0_0_1/">叙利亚</a></li>
                    <li><a data-id="481" data-key="科威特" href="http://plan.qyer.com/search_0_0_481_0_0_0_1/">科威特</a></li>
                    <li><a data-id="401" data-key="阿富汗" href="http://plan.qyer.com/search_0_0_401_0_0_0_1/">阿富汗</a></li>
                    <li><a data-id="468" data-key="吉尔吉斯斯坦" href="http://plan.qyer.com/search_0_0_468_0_0_0_1/">吉尔吉斯斯坦</a></li>
                    <li><a data-id="1035" data-key="伊拉克" href="http://plan.qyer.com/search_0_0_1035_0_0_0_1/">伊拉克</a></li>
                    <li><a data-id="544" data-key="塔吉克斯坦" href="http://plan.qyer.com/search_0_0_544_0_0_0_1/">塔吉克斯坦</a></li>
                    <li><a data-id="567" data-key="也门" href="http://plan.qyer.com/search_0_0_567_0_0_0_1/">也门</a></li>
                    <li><a data-id="552" data-key="土库曼斯坦" href="http://plan.qyer.com/search_0_0_552_0_0_0_1/">土库曼斯坦</a></li>
                    <li><a data-id="438" data-key="东帝汶" href="http://plan.qyer.com/search_0_0_438_0_0_0_1/">东帝汶</a></li>
                    <li><a data-id="1425" data-key="英属印度洋领地" href="http://plan.qyer.com/search_0_0_1425_0_0_0_1/">英属印度洋领地</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="186" data-key="法国" href="http://plan.qyer.com/search_0_0_186_0_0_0_1/">法国</a></li>
                    <li><a data-id="189" data-key="意大利" href="http://plan.qyer.com/search_0_0_189_0_0_0_1/">意大利</a></li>
                    <li><a data-id="15" data-key="德国" href="http://plan.qyer.com/search_0_0_15_0_0_0_1/">德国</a></li>
                    <li><a data-id="182" data-key="西班牙" href="http://plan.qyer.com/search_0_0_182_0_0_0_1/">西班牙</a></li>
                    <li><a data-id="13" data-key="英国" href="http://plan.qyer.com/search_0_0_13_0_0_0_1/">英国</a></li>
                    <li><a data-id="524" data-key="瑞士" href="http://plan.qyer.com/search_0_0_524_0_0_0_1/">瑞士</a></li>
                    <li><a data-id="198" data-key="奥地利" href="http://plan.qyer.com/search_0_0_198_0_0_0_1/">奥地利</a></li>
                    <li><a data-id="200" data-key="荷兰" href="http://plan.qyer.com/search_0_0_200_0_0_0_1/">荷兰</a></li>
                    <li><a data-id="804" data-key="梵蒂冈" href="http://plan.qyer.com/search_0_0_804_0_0_0_1/">梵蒂冈</a></li>
                    <li><a data-id="193" data-key="捷克" href="http://plan.qyer.com/search_0_0_193_0_0_0_1/">捷克</a></li>
                    <li><a data-id="424" data-key="比利时" href="http://plan.qyer.com/search_0_0_424_0_0_0_1/">比利时</a></li>
                    <li><a data-id="195" data-key="土耳其" href="http://plan.qyer.com/search_0_0_195_0_0_0_1/">土耳其</a></li>
                    <li><a data-id="206" data-key="希腊" href="http://plan.qyer.com/search_0_0_206_0_0_0_1/">希腊</a></li>
                    <li><a data-id="208" data-key="俄罗斯" href="http://plan.qyer.com/search_0_0_208_0_0_0_1/">俄罗斯</a></li>
                    <li><a data-id="207" data-key="匈牙利" href="http://plan.qyer.com/search_0_0_207_0_0_0_1/">匈牙利</a></li>
                    <li><a data-id="202" data-key="瑞典" href="http://plan.qyer.com/search_0_0_202_0_0_0_1/">瑞典</a></li>
                    <li><a data-id="205" data-key="丹麦" href="http://plan.qyer.com/search_0_0_205_0_0_0_1/">丹麦</a></li>
                    <li><a data-id="523" data-key="葡萄牙" href="http://plan.qyer.com/search_0_0_523_0_0_0_1/">葡萄牙</a></li>
                    <li><a data-id="654" data-key="摩纳哥" href="http://plan.qyer.com/search_0_0_654_0_0_0_1/">摩纳哥</a></li>
                    <li><a data-id="521" data-key="挪威" href="http://plan.qyer.com/search_0_0_521_0_0_0_1/">挪威</a></li>
                    <li><a data-id="448" data-key="芬兰" href="http://plan.qyer.com/search_0_0_448_0_0_0_1/">芬兰</a></li>
                    <li><a data-id="493" data-key="卢森堡" href="http://plan.qyer.com/search_0_0_493_0_0_0_1/">卢森堡</a></li>
                    <li><a data-id="425" data-key="冰岛" href="http://plan.qyer.com/search_0_0_425_0_0_0_1/">冰岛</a></li>
                    <li><a data-id="427" data-key="波兰" href="http://plan.qyer.com/search_0_0_427_0_0_0_1/">波兰</a></li>
                    <li><a data-id="762" data-key="列支敦士登" href="http://plan.qyer.com/search_0_0_762_0_0_0_1/">列支敦士登</a></li>
                    <li><a data-id="538" data-key="斯洛伐克" href="http://plan.qyer.com/search_0_0_538_0_0_0_1/">斯洛伐克</a></li>
                    <li><a data-id="406" data-key="爱尔兰" href="http://plan.qyer.com/search_0_0_406_0_0_0_1/">爱尔兰</a></li>
                    <li><a data-id="407" data-key="爱沙尼亚" href="http://plan.qyer.com/search_0_0_407_0_0_0_1/">爱沙尼亚</a></li>
                    <li><a data-id="482" data-key="克罗地亚" href="http://plan.qyer.com/search_0_0_482_0_0_0_1/">克罗地亚</a></li>
                    <li><a data-id="498" data-key="马耳他" href="http://plan.qyer.com/search_0_0_498_0_0_0_1/">马耳他</a></li>
                    <li><a data-id="785" data-key="圣马力诺" href="http://plan.qyer.com/search_0_0_785_0_0_0_1/">圣马力诺</a></li>
                    <li><a data-id="539" data-key="斯洛文尼亚" href="http://plan.qyer.com/search_0_0_539_0_0_0_1/">斯洛文尼亚</a></li>
                    <li><a data-id="485" data-key="拉脱维亚" href="http://plan.qyer.com/search_0_0_485_0_0_0_1/">拉脱维亚</a></li>
                    <li><a data-id="489" data-key="立陶宛" href="http://plan.qyer.com/search_0_0_489_0_0_0_1/">立陶宛</a></li>
                    <li><a data-id="408" data-key="安道尔" href="http://plan.qyer.com/search_0_0_408_0_0_0_1/">安道尔</a></li>
                    <li><a data-id="495" data-key="罗马尼亚" href="http://plan.qyer.com/search_0_0_495_0_0_0_1/">罗马尼亚</a></li>
                    <li><a data-id="527" data-key="塞尔维亚" href="http://plan.qyer.com/search_0_0_527_0_0_0_1/">塞尔维亚</a></li>
                    <li><a data-id="464" data-key="黑山" href="http://plan.qyer.com/search_0_0_464_0_0_0_1/">黑山</a></li>
                    <li><a data-id="560" data-key="乌克兰" href="http://plan.qyer.com/search_0_0_560_0_0_0_1/">乌克兰</a></li>
                    <li><a data-id="421" data-key="保加利亚" href="http://plan.qyer.com/search_0_0_421_0_0_0_1/">保加利亚</a></li>
                    <li><a data-id="457" data-key="格鲁吉亚" href="http://plan.qyer.com/search_0_0_457_0_0_0_1/">格鲁吉亚</a></li>
                    <li><a data-id="428" data-key="波黑" href="http://plan.qyer.com/search_0_0_428_0_0_0_1/">波黑</a></li>
                    <li><a data-id="566" data-key="亚美尼亚" href="http://plan.qyer.com/search_0_0_566_0_0_0_1/">亚美尼亚</a></li>
                    <li><a data-id="805" data-key="直布罗陀" href="http://plan.qyer.com/search_0_0_805_0_0_0_1/">直布罗陀</a></li>
                    <li><a data-id="404" data-key="阿塞拜疆" href="http://plan.qyer.com/search_0_0_404_0_0_0_1/">阿塞拜疆</a></li>
                    <li><a data-id="530" data-key="塞浦路斯" href="http://plan.qyer.com/search_0_0_530_0_0_0_1/">塞浦路斯</a></li>
                    <li><a data-id="418" data-key="白俄罗斯" href="http://plan.qyer.com/search_0_0_418_0_0_0_1/">白俄罗斯</a></li>
                    <li><a data-id="399" data-key="阿尔巴尼亚" href="http://plan.qyer.com/search_0_0_399_0_0_0_1/">阿尔巴尼亚</a></li>
                    <li><a data-id="501" data-key="马其顿" href="http://plan.qyer.com/search_0_0_501_0_0_0_1/">马其顿</a></li>
                    <li><a data-id="479" data-key="科索沃" href="http://plan.qyer.com/search_0_0_479_0_0_0_1/">科索沃</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="244" data-key="埃及" href="http://plan.qyer.com/search_0_0_244_0_0_0_1/">埃及</a></li>
                    <li><a data-id="517" data-key="南非" href="http://plan.qyer.com/search_0_0_517_0_0_0_1/">南非</a></li>
                    <li><a data-id="513" data-key="摩洛哥" href="http://plan.qyer.com/search_0_0_513_0_0_0_1/">摩洛哥</a></li>
                    <li><a data-id="483" data-key="肯尼亚" href="http://plan.qyer.com/search_0_0_483_0_0_0_1/">肯尼亚</a></li>
                    <li><a data-id="503" data-key="毛里求斯" href="http://plan.qyer.com/search_0_0_503_0_0_0_1/">毛里求斯</a></li>
                    <li><a data-id="546" data-key="坦桑尼亚" href="http://plan.qyer.com/search_0_0_546_0_0_0_1/">坦桑尼亚</a></li>
                    <li><a data-id="405" data-key="埃塞俄比亚" href="http://plan.qyer.com/search_0_0_405_0_0_0_1/">埃塞俄比亚</a></li>
                    <li><a data-id="531" data-key="塞舌尔" href="http://plan.qyer.com/search_0_0_531_0_0_0_1/">塞舌尔</a></li>
                    <li><a data-id="550" data-key="突尼斯" href="http://plan.qyer.com/search_0_0_550_0_0_0_1/">突尼斯</a></li>
                    <li><a data-id="400" data-key="阿尔及利亚" href="http://plan.qyer.com/search_0_0_400_0_0_0_1/">阿尔及利亚</a></li>
                    <li><a data-id="573" data-key="赞比亚" href="http://plan.qyer.com/search_0_0_573_0_0_0_1/">赞比亚</a></li>
                    <li><a data-id="474" data-key="津巴布韦" href="http://plan.qyer.com/search_0_0_474_0_0_0_1/">津巴布韦</a></li>
                    <li><a data-id="559" data-key="乌干达" href="http://plan.qyer.com/search_0_0_559_0_0_0_1/">乌干达</a></li>
                    <li><a data-id="516" data-key="纳米比亚" href="http://plan.qyer.com/search_0_0_516_0_0_0_1/">纳米比亚</a></li>
                    <li><a data-id="520" data-key="尼日利亚" href="http://plan.qyer.com/search_0_0_520_0_0_0_1/">尼日利亚</a></li>
                    <li><a data-id="496" data-key="马达加斯加" href="http://plan.qyer.com/search_0_0_496_0_0_0_1/">马达加斯加</a></li>
                    <li><a data-id="471" data-key="加纳" href="http://plan.qyer.com/search_0_0_471_0_0_0_1/">加纳</a></li>
                    <li><a data-id="541" data-key="苏丹" href="http://plan.qyer.com/search_0_0_541_0_0_0_1/">苏丹</a></li>
                    <li><a data-id="486" data-key="莱索托" href="http://plan.qyer.com/search_0_0_486_0_0_0_1/">莱索托</a></li>
                    <li><a data-id="409" data-key="安哥拉" href="http://plan.qyer.com/search_0_0_409_0_0_0_1/">安哥拉</a></li>
                    <li><a data-id="514" data-key="莫桑比克" href="http://plan.qyer.com/search_0_0_514_0_0_0_1/">莫桑比克</a></li>
                    <li><a data-id="492" data-key="留尼汪" href="http://plan.qyer.com/search_0_0_492_0_0_0_1/">留尼汪</a></li>
                    <li><a data-id="494" data-key="卢旺达" href="http://plan.qyer.com/search_0_0_494_0_0_0_1/">卢旺达</a></li>
                    <li><a data-id="576" data-key="中非共和国" href="http://plan.qyer.com/search_0_0_576_0_0_0_1/">中非共和国</a></li>
                    <li><a data-id="452" data-key="刚果民主共和国" href="http://plan.qyer.com/search_0_0_452_0_0_0_1/">刚果民主共和国</a></li>
                    <li><a data-id="475" data-key="喀麦隆" href="http://plan.qyer.com/search_0_0_475_0_0_0_1/">喀麦隆</a></li>
                    <li><a data-id="431" data-key="博茨瓦纳" href="http://plan.qyer.com/search_0_0_431_0_0_0_1/">博茨瓦纳</a></li>
                    <li><a data-id="480" data-key="科特迪瓦" href="http://plan.qyer.com/search_0_0_480_0_0_0_1/">科特迪瓦</a></li>
                    <li><a data-id="529" data-key="塞内加尔" href="http://plan.qyer.com/search_0_0_529_0_0_0_1/">塞内加尔</a></li>
                    <li><a data-id="491" data-key="利比亚" href="http://plan.qyer.com/search_0_0_491_0_0_0_1/">利比亚</a></li>
                    <li><a data-id="451" data-key="刚果" href="http://plan.qyer.com/search_0_0_451_0_0_0_1/">刚果</a></li>
                    <li><a data-id="439" data-key="多哥" href="http://plan.qyer.com/search_0_0_439_0_0_0_1/">多哥</a></li>
                    <li><a data-id="499" data-key="马拉维" href="http://plan.qyer.com/search_0_0_499_0_0_0_1/">马拉维</a></li>
                    <li><a data-id="467" data-key="吉布提" href="http://plan.qyer.com/search_0_0_467_0_0_0_1/">吉布提</a></li>
                    <li><a data-id="423" data-key="贝宁" href="http://plan.qyer.com/search_0_0_423_0_0_0_1/">贝宁</a></li>
                    <li><a data-id="473" data-key="加蓬" href="http://plan.qyer.com/search_0_0_473_0_0_0_1/">加蓬</a></li>
                    <li><a data-id="500" data-key="马里" href="http://plan.qyer.com/search_0_0_500_0_0_0_1/">马里</a></li>
                    <li><a data-id="1062" data-key="西撒哈拉" href="http://plan.qyer.com/search_0_0_1062_0_0_0_1/">西撒哈拉</a></li>
                    <li><a data-id="504" data-key="毛里塔尼亚" href="http://plan.qyer.com/search_0_0_504_0_0_0_1/">毛里塔尼亚</a></li>
                    <li><a data-id="437" data-key="赤道几内亚" href="http://plan.qyer.com/search_0_0_437_0_0_0_1/">赤道几内亚</a></li>
                    <li><a data-id="540" data-key="斯威士兰" href="http://plan.qyer.com/search_0_0_540_0_0_0_1/">斯威士兰</a></li>
                    <li><a data-id="435" data-key="布隆迪" href="http://plan.qyer.com/search_0_0_435_0_0_0_1/">布隆迪</a></li>
                    <li><a data-id="469" data-key="几内亚" href="http://plan.qyer.com/search_0_0_469_0_0_0_1/">几内亚</a></li>
                    <li><a data-id="574" data-key="乍得" href="http://plan.qyer.com/search_0_0_574_0_0_0_1/">乍得</a></li>
                    <li><a data-id="853" data-key="南苏丹" href="http://plan.qyer.com/search_0_0_853_0_0_0_1/">南苏丹</a></li>
                    <li><a data-id="519" data-key="尼日尔" href="http://plan.qyer.com/search_0_0_519_0_0_0_1/">尼日尔</a></li>
                    <li><a data-id="1061" data-key="佛得角" href="http://plan.qyer.com/search_0_0_1061_0_0_0_1/">佛得角</a></li>
                    <li><a data-id="490" data-key="利比里亚" href="http://plan.qyer.com/search_0_0_490_0_0_0_1/">利比里亚</a></li>
                    <li><a data-id="420" data-key="索马里" href="http://plan.qyer.com/search_0_0_420_0_0_0_1/">索马里</a></li>
                    <li><a data-id="434" data-key="布基纳法索" href="http://plan.qyer.com/search_0_0_434_0_0_0_1/">布基纳法索</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="236" data-key="美国" href="http://plan.qyer.com/search_0_0_236_0_0_0_1/">美国</a></li>
                    <li><a data-id="238" data-key="加拿大" href="http://plan.qyer.com/search_0_0_238_0_0_0_1/">加拿大</a></li>
                    <li><a data-id="515" data-key="墨西哥" href="http://plan.qyer.com/search_0_0_515_0_0_0_1/">墨西哥</a></li>
                    <li><a data-id="458" data-key="古巴" href="http://plan.qyer.com/search_0_0_458_0_0_0_1/">古巴</a></li>
                    <li><a data-id="413" data-key="巴哈马" href="http://plan.qyer.com/search_0_0_413_0_0_0_1/">巴哈马</a></li>
                    <li><a data-id="426" data-key="波多黎各" href="http://plan.qyer.com/search_0_0_426_0_0_0_1/">波多黎各</a></li>
                    <li><a data-id="417" data-key="巴拿马" href="http://plan.qyer.com/search_0_0_417_0_0_0_1/">巴拿马</a></li>
                    <li><a data-id="454" data-key="哥斯达黎加" href="http://plan.qyer.com/search_0_0_454_0_0_0_1/">哥斯达黎加</a></li>
                    <li><a data-id="565" data-key="牙买加" href="http://plan.qyer.com/search_0_0_565_0_0_0_1/">牙买加</a></li>
                    <li><a data-id="506" data-key="美属维尔京群岛" href="http://plan.qyer.com/search_0_0_506_0_0_0_1/">美属维尔京群岛</a></li>
                    <li><a data-id="555" data-key="危地马拉" href="http://plan.qyer.com/search_0_0_555_0_0_0_1/">危地马拉</a></li>
                    <li><a data-id="477" data-key="开曼群岛" href="http://plan.qyer.com/search_0_0_477_0_0_0_1/">开曼群岛</a></li>
                    <li><a data-id="430" data-key="伯利兹" href="http://plan.qyer.com/search_0_0_430_0_0_0_1/">伯利兹</a></li>
                    <li><a data-id="440" data-key="多米尼加共和国" href="http://plan.qyer.com/search_0_0_440_0_0_0_1/">多米尼加共和国</a></li>
                    <li><a data-id="465" data-key="洪都拉斯" href="http://plan.qyer.com/search_0_0_465_0_0_0_1/">洪都拉斯</a></li>
                    <li><a data-id="462" data-key="海地" href="http://plan.qyer.com/search_0_0_462_0_0_0_1/">海地</a></li>
                    <li><a data-id="1382" data-key="荷属圣马丁" href="http://plan.qyer.com/search_0_0_1382_0_0_0_1/">荷属圣马丁</a></li>
                    <li><a data-id="1383" data-key="法属圣马丁" href="http://plan.qyer.com/search_0_0_1383_0_0_0_1/">法属圣马丁</a></li>
                    <li><a data-id="419" data-key="百慕大" href="http://plan.qyer.com/search_0_0_419_0_0_0_1/">百慕大</a></li>
                    <li><a data-id="411" data-key="巴巴多斯" href="http://plan.qyer.com/search_0_0_411_0_0_0_1/">巴巴多斯</a></li>
                    <li><a data-id="525" data-key="萨尔瓦多" href="http://plan.qyer.com/search_0_0_525_0_0_0_1/">萨尔瓦多</a></li>
                    <li><a data-id="548" data-key="特克斯和凯科斯群岛" href="http://plan.qyer.com/search_0_0_548_0_0_0_1/">特克斯和凯科斯群岛</a></li>
                    <li><a data-id="535" data-key="圣卢西亚" href="http://plan.qyer.com/search_0_0_535_0_0_0_1/">圣卢西亚</a></li>
                    <li><a data-id="549" data-key="特立尼达和多巴哥" href="http://plan.qyer.com/search_0_0_549_0_0_0_1/">特立尼达和多巴哥</a></li>
                    <li><a data-id="518" data-key="尼加拉瓜" href="http://plan.qyer.com/search_0_0_518_0_0_0_1/">尼加拉瓜</a></li>
                    <li><a data-id="410" data-key="安提瓜和巴布达" href="http://plan.qyer.com/search_0_0_410_0_0_0_1/">安提瓜和巴布达</a></li>
                    <li><a data-id="432" data-key="阿鲁巴" href="http://plan.qyer.com/search_0_0_432_0_0_0_1/">阿鲁巴</a></li>
                    <li><a data-id="534" data-key="圣基茨和尼维斯" href="http://plan.qyer.com/search_0_0_534_0_0_0_1/">圣基茨和尼维斯</a></li>
                    <li><a data-id="571" data-key="英属维尔京群岛" href="http://plan.qyer.com/search_0_0_571_0_0_0_1/">英属维尔京群岛</a></li>
                    <li><a data-id="441" data-key="多米尼克" href="http://plan.qyer.com/search_0_0_441_0_0_0_1/">多米尼克</a></li>
                    <li><a data-id="455" data-key="格林纳达" href="http://plan.qyer.com/search_0_0_455_0_0_0_1/">格林纳达</a></li>
                    <li><a data-id="1419" data-key="库拉索" href="http://plan.qyer.com/search_0_0_1419_0_0_0_1/">库拉索</a></li>
                    <li><a data-id="1380" data-key="马提尼克" href="http://plan.qyer.com/search_0_0_1380_0_0_0_1/">马提尼克</a></li>
                    <li><a data-id="1295" data-key="瓜德罗普" href="http://plan.qyer.com/search_0_0_1295_0_0_0_1/">瓜德罗普</a></li>
                    <li><a data-id="1416" data-key="安圭拉" href="http://plan.qyer.com/search_0_0_1416_0_0_0_1/">安圭拉</a></li>
                    <li><a data-id="1432" data-key="波内赫" href="http://plan.qyer.com/search_0_0_1432_0_0_0_1/">波内赫</a></li>
                    <li><a data-id="536" data-key="圣文森特和格林纳丁斯" href="http://plan.qyer.com/search_0_0_536_0_0_0_1/">圣文森特和格林纳丁斯</a></li>
                    <li><a data-id="1417" data-key="圣巴泰勒米岛" href="http://plan.qyer.com/search_0_0_1417_0_0_0_1/">圣巴泰勒米岛</a></li>
                    <li><a data-id="1421" data-key="萨巴岛" href="http://plan.qyer.com/search_0_0_1421_0_0_0_1/">萨巴岛</a></li>
                    <li><a data-id="1418" data-key="蒙塞拉特岛" href="http://plan.qyer.com/search_0_0_1418_0_0_0_1/">蒙塞拉特岛</a></li>
                    <li><a data-id="1420" data-key="圣尤斯特歇斯" href="http://plan.qyer.com/search_0_0_1420_0_0_0_1/">圣尤斯特歇斯</a></li>
                    <li><a data-id="1381" data-key="圣皮埃尔和密克隆群岛" href="http://plan.qyer.com/search_0_0_1381_0_0_0_1/">圣皮埃尔和密克隆群岛</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="242" data-key="巴西" href="http://plan.qyer.com/search_0_0_242_0_0_0_1/">巴西</a></li>
                    <li><a data-id="509" data-key="秘鲁" href="http://plan.qyer.com/search_0_0_509_0_0_0_1/">秘鲁</a></li>
                    <li><a data-id="243" data-key="阿根廷" href="http://plan.qyer.com/search_0_0_243_0_0_0_1/">阿根廷</a></li>
                    <li><a data-id="575" data-key="智利" href="http://plan.qyer.com/search_0_0_575_0_0_0_1/">智利</a></li>
                    <li><a data-id="429" data-key="玻利维亚" href="http://plan.qyer.com/search_0_0_429_0_0_0_1/">玻利维亚</a></li>
                    <li><a data-id="453" data-key="哥伦比亚" href="http://plan.qyer.com/search_0_0_453_0_0_0_1/">哥伦比亚</a></li>
                    <li><a data-id="443" data-key="厄瓜多尔" href="http://plan.qyer.com/search_0_0_443_0_0_0_1/">厄瓜多尔</a></li>
                    <li><a data-id="557" data-key="委内瑞拉" href="http://plan.qyer.com/search_0_0_557_0_0_0_1/">委内瑞拉</a></li>
                    <li><a data-id="561" data-key="乌拉圭" href="http://plan.qyer.com/search_0_0_561_0_0_0_1/">乌拉圭</a></li>
                    <li><a data-id="415" data-key="巴拉圭" href="http://plan.qyer.com/search_0_0_415_0_0_0_1/">巴拉圭</a></li>
                    <li><a data-id="1293" data-key="苏里南" href="http://plan.qyer.com/search_0_0_1293_0_0_0_1/">苏里南</a></li>
                    <li><a data-id="449" data-key="福克兰群岛（马尔维纳斯群岛）" href="http://plan.qyer.com/search_0_0_449_0_0_0_1/">福克兰群岛（马尔维纳斯群岛）</a></li>
                    <li><a data-id="460" data-key="圭亚那" href="http://plan.qyer.com/search_0_0_460_0_0_0_1/">圭亚那</a></li>
                    <li><a data-id="1292" data-key="法属圭亚那" href="http://plan.qyer.com/search_0_0_1292_0_0_0_1/">法属圭亚那</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="240" data-key="澳大利亚" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/">澳大利亚</a></li>
                    <li><a data-id="241" data-key="新西兰" href="http://plan.qyer.com/search_0_0_241_0_0_0_1/">新西兰</a></li>
                    <li><a data-id="422" data-key="北马里亚纳群岛" href="http://plan.qyer.com/search_0_0_422_0_0_0_1/">北马里亚纳群岛</a></li>
                    <li><a data-id="447" data-key="斐济" href="http://plan.qyer.com/search_0_0_447_0_0_0_1/">斐济</a></li>
                    <li><a data-id="522" data-key="帕劳" href="http://plan.qyer.com/search_0_0_522_0_0_0_1/">帕劳</a></li>
                    <li><a data-id="1072" data-key="关岛" href="http://plan.qyer.com/search_0_0_1072_0_0_0_1/">关岛</a></li>
                    <li><a data-id="545" data-key="法属波利尼西亚" href="http://plan.qyer.com/search_0_0_545_0_0_0_1/">法属波利尼西亚</a></li>
                    <li><a data-id="554" data-key="瓦努阿图" href="http://plan.qyer.com/search_0_0_554_0_0_0_1/">瓦努阿图</a></li>
                    <li><a data-id="806" data-key="艾普罗菲尔" href="http://plan.qyer.com/search_0_0_806_0_0_0_1/">艾普罗菲尔</a></li>
                    <li><a data-id="484" data-key="库克群岛" href="http://plan.qyer.com/search_0_0_484_0_0_0_1/">库克群岛</a></li>
                    <li><a data-id="563" data-key="新喀里多尼亚" href="http://plan.qyer.com/search_0_0_563_0_0_0_1/">新喀里多尼亚</a></li>
                    <li><a data-id="412" data-key="巴布亚新几内亚" href="http://plan.qyer.com/search_0_0_412_0_0_0_1/">巴布亚新几内亚</a></li>
                    <li><a data-id="547" data-key="汤加" href="http://plan.qyer.com/search_0_0_547_0_0_0_1/">汤加</a></li>
                    <li><a data-id="526" data-key="萨摩亚" href="http://plan.qyer.com/search_0_0_526_0_0_0_1/">萨摩亚</a></li>
                    <li><a data-id="543" data-key="所罗门群岛" href="http://plan.qyer.com/search_0_0_543_0_0_0_1/">所罗门群岛</a></li>
                    <li><a data-id="510" data-key="密克罗尼西亚联邦" href="http://plan.qyer.com/search_0_0_510_0_0_0_1/">密克罗尼西亚联邦</a></li>
                    <li><a data-id="502" data-key="马绍尔群岛" href="http://plan.qyer.com/search_0_0_502_0_0_0_1/">马绍尔群岛</a></li>
                    <li><a data-id="505" data-key="美属萨摩亚" href="http://plan.qyer.com/search_0_0_505_0_0_0_1/">美属萨摩亚</a></li>
                    <li><a data-id="1064" data-key="纽埃" href="http://plan.qyer.com/search_0_0_1064_0_0_0_1/">纽埃</a></li>
                    <li><a data-id="551" data-key="图瓦卢" href="http://plan.qyer.com/search_0_0_551_0_0_0_1/">图瓦卢</a></li>
                    <li><a data-id="466" data-key="基里巴斯" href="http://plan.qyer.com/search_0_0_466_0_0_0_1/">基里巴斯</a></li>
                    <li><a data-id="1027" data-key="瑙鲁" href="http://plan.qyer.com/search_0_0_1027_0_0_0_1/">瑙鲁</a></li>
                    <li><a data-id="553" data-key="瓦利斯群岛和富图纳群岛" href="http://plan.qyer.com/search_0_0_553_0_0_0_1/">瓦利斯群岛和富图纳群岛</a></li>
                    <li><a data-id="1428" data-key="皮特凯恩群岛" href="http://plan.qyer.com/search_0_0_1428_0_0_0_1/">皮特凯恩群岛</a></li>
                    <li><a data-id="1063" data-key="托克劳" href="http://plan.qyer.com/search_0_0_1063_0_0_0_1/">托克劳</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="760" data-key="南极" href="http://plan.qyer.com/search_0_0_760_0_0_0_1/">南极</a></li>
                    <li><a data-id="1762" data-key="南乔治亚岛和南桑威奇群岛" href="http://plan.qyer.com/search_0_0_1762_0_0_0_1/">南乔治亚岛和南桑威奇群岛</a></li>
                    <li><a data-id="1446" data-key="太空" href="http://plan.qyer.com/search_0_0_1446_0_0_0_1/">太空</a></li>
                    <li><a data-id="1431" data-key="法属南部领土" href="http://plan.qyer.com/search_0_0_1431_0_0_0_1/">法属南部领土</a></li>
                    <li><a data-id="1430" data-key="布韦岛" href="http://plan.qyer.com/search_0_0_1430_0_0_0_1/">布韦岛</a></li>
                        </ul>
              </div>
    </div>

      <div  id="js_cityList" class="items clearfix" style="display:none;">
          <strong class="title">
              前往城市:
          </strong>
          <div class="list clearfix">
          </div>

          <div class="selectdiv clearfix" style="display:none;" >
          </div>

          <div class="subbtn" style="display:none;">
              <input type="button" class="ui_button js_cmd" id="selectCitysOKBtn" data-cmd="goPage" data-type="accept" value="确定" data-bn-ipg="planhome-select-city-confirm">
              <input type="button" class="ui_button_cancel js_cmd" data-cmd="city_select_close" data-type="cancel" value="取消" data-bn-ipg="planhome-select-city-cancel"> 
          </div>


          <div class="seting destination">
              <a href="javascript:;" class="moreBtn setMore js_cmd" data-cmd="city_more" data-status="close" data-bn-ipg="planhome-select-city-more">
                  更多
              </a>
              <a href="javascript:;" class="setSelect js_cmd" data-cmd="city_select" data-bn-ipg="planhome-select-city-multipleselect">
                  多选
              </a>
          </div>
      </div>
    
        <div class="items clearfix times">
      <strong class="title">
        出行时间:
      </strong>
      <div id="js_startTime" class="list clearfix">
                <a data-bn-ipg="planhome-select-month1" data-id="1" data-key="1" href="http://plan.qyer.com/search_1_0_0_0_0_0_1/">一月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="2" data-key="2" href="http://plan.qyer.com/search_2_0_0_0_0_0_1/">二月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="3" data-key="3" href="http://plan.qyer.com/search_3_0_0_0_0_0_1/">三月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="4" data-key="4" href="http://plan.qyer.com/search_4_0_0_0_0_0_1/">四月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="5" data-key="5" href="http://plan.qyer.com/search_5_0_0_0_0_0_1/">五月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="6" data-key="6" href="http://plan.qyer.com/search_6_0_0_0_0_0_1/">六月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="7" data-key="7" href="http://plan.qyer.com/search_7_0_0_0_0_0_1/">七月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="8" data-key="8" href="http://plan.qyer.com/search_8_0_0_0_0_0_1/">八月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="9" data-key="9" href="http://plan.qyer.com/search_9_0_0_0_0_0_1/">九月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="10" data-key="10" href="http://plan.qyer.com/search_10_0_0_0_0_0_1/">十月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="11" data-key="11" href="http://plan.qyer.com/search_11_0_0_0_0_0_1/">十一月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="12" data-key="12" href="http://plan.qyer.com/search_12_0_0_0_0_0_1/">十二月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="13" data-key="13" href="http://plan.qyer.com/search_13_0_0_0_0_0_1/">新年</a>
                <a data-bn-ipg="planhome-select-month1" data-id="14" data-key="14" href="http://plan.qyer.com/search_14_0_0_0_0_0_1/">春节</a>
                <a data-bn-ipg="planhome-select-month1" data-id="15" data-key="15" href="http://plan.qyer.com/search_15_0_0_0_0_0_1/">清明</a>
                <a data-bn-ipg="planhome-select-month1" data-id="16" data-key="16" href="http://plan.qyer.com/search_16_0_0_0_0_0_1/">劳动节</a>
                <a data-bn-ipg="planhome-select-month1" data-id="17" data-key="17" href="http://plan.qyer.com/search_17_0_0_0_0_0_1/">端午</a>
                <a data-bn-ipg="planhome-select-month1" data-id="18" data-key="18" href="http://plan.qyer.com/search_18_0_0_0_0_0_1/">中秋</a>
                <a data-bn-ipg="planhome-select-month1" data-id="19" data-key="19" href="http://plan.qyer.com/search_19_0_0_0_0_0_1/">国庆</a>
              </div>
      <div class="seting">
        <a href="javascript:;" class="moreBtn setMore js_cmd" data-cmd="time_more" data-status="close" data-bn-ipg="planhome-select-city-more">
          更多
        </a>
      </div>
    </div>
            <div class="items clearfix">
      <strong class="title">
        出行天数:
      </strong>
      <div class="list clearfix">
                <a data-bn-ipg="planhome-select-days1" data-id="1001" data-key="1001" href="http://plan.qyer.com/search_0_0_0_0_1001_0_1/">3天及以下</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1002" data-key="1002" href="http://plan.qyer.com/search_0_0_0_0_1002_0_1/">4天至7天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1003" data-key="1003" href="http://plan.qyer.com/search_0_0_0_0_1003_0_1/">8天至14天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1004" data-key="1004" href="http://plan.qyer.com/search_0_0_0_0_1004_0_1/">14天至20天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1005" data-key="1005" href="http://plan.qyer.com/search_0_0_0_0_1005_0_1/">20天以上</a>
              </div>
      <div class="seting">
      </div>
    </div>
    
        <div class="items clearfix">
      <strong class="title">
        出发城市:
      </strong>
          <div id="js_placeList" class="list clearfix">
                      <a data-bn-ipg="planhome-select-country1" data-id="11593" data-key="北京" href="http://plan.qyer.com/search_0_11593_0_0_0_0_1/">北京</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11595" data-key="上海" href="http://plan.qyer.com/search_0_11595_0_0_0_0_1/">上海</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11808" data-key="广州" href="http://plan.qyer.com/search_0_11808_0_0_0_0_1/">广州</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="12189" data-key="深圳" href="http://plan.qyer.com/search_0_12189_0_0_0_0_1/">深圳</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11596" data-key="重庆" href="http://plan.qyer.com/search_0_11596_0_0_0_0_1/">重庆</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11800" data-key="成都" href="http://plan.qyer.com/search_0_11800_0_0_0_0_1/">成都</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11690" data-key="杭州" href="http://plan.qyer.com/search_0_11690_0_0_0_0_1/">杭州</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="50" data-key="香港" href="http://plan.qyer.com/search_0_50_0_0_0_0_1/">香港</a>
              </div>
    </div>
    

        <div class="items clearfix">
      <strong class="title">
        行程主题:
      </strong>
      <div id="js_planTopic_links" class="list clearfix">
            <a data-bn-ipg="planhome-select-tag1" data-id="1" data-key="1" href="http://plan.qyer.com/search_0_0_0_0_0_1_1/">美食</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="2" data-key="2" href="http://plan.qyer.com/search_0_0_0_0_0_2_1/">人文</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="3" data-key="3" href="http://plan.qyer.com/search_0_0_0_0_0_3_1/">购物</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="4" data-key="4" href="http://plan.qyer.com/search_0_0_0_0_0_4_1/">游园观光</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="5" data-key="5" href="http://plan.qyer.com/search_0_0_0_0_0_5_1/">娱乐休闲</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="6" data-key="6" href="http://plan.qyer.com/search_0_0_0_0_0_6_1/">沙滩海岛</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="7" data-key="7" href="http://plan.qyer.com/search_0_0_0_0_0_7_1/">户外</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="8" data-key="8" href="http://plan.qyer.com/search_0_0_0_0_0_8_1/">自然风光</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="9" data-key="9" href="http://plan.qyer.com/search_0_0_0_0_0_9_1/">自驾</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="10" data-key="10" href="http://plan.qyer.com/search_0_0_0_0_0_10_1/">蜜月</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="11" data-key="11" href="http://plan.qyer.com/search_0_0_0_0_0_11_1/">亲子</a>
            </div>

          <div id="js_planTopic_more" class="list clearfix" style="display:none;">
            <label data-key="1"><input type="checkbox">美食</label>
            <label data-key="2"><input type="checkbox">人文</label>
            <label data-key="3"><input type="checkbox">购物</label>
            <label data-key="4"><input type="checkbox">游园观光</label>
            <label data-key="5"><input type="checkbox">娱乐休闲</label>
            <label data-key="6"><input type="checkbox">沙滩海岛</label>
            <label data-key="7"><input type="checkbox">户外</label>
            <label data-key="8"><input type="checkbox">自然风光</label>
            <label data-key="9"><input type="checkbox">自驾</label>
            <label data-key="10"><input type="checkbox">蜜月</label>
            <label data-key="11"><input type="checkbox">亲子</label>
                </div>

      <div id="js_planTopic_subbtn" class="subbtn" style="display: none;">
        <input type="button" class="ui_button js_cmd" id="selectPlanTopicOKBtn" data-cmd="goPage" data-type="accept" value="确定" data-bn-ipg="planhome-select-city-confirm">
        <input type="button" class="ui_button_cancel js_cmd" data-cmd="planType_close" data-type="cancel" value="取消"data-bn-ipg="planhome-select-city-cancel"> 
          </div>

      <div class="seting">
        <a id="js_moreTopic" href="javascript:;" class="setSelect js_cmd" data-cmd="planType_more" data-bn-ipg="planhome-select-city-multipleselect">
          多选
        </a>
      </div>
    </div>
            <div class="items clearfix noneborder">
      <strong class="title">
        精华等级:
      </strong>
      <div id="essence_list" class="list clearfix"></div>
      <div class="seting">
      </div>
    </div>
      </div>

  <!-- 首页行程列表 -->
  <div class="ind_lists">
    <div class="seting">
      <!-- 排序 -->
      <div class="sort  ">
        <a href="javascript://" class="current">默认排序</a> |  
        <a href="javascript://" class="view">浏览次数最多</a> |  
        <a href="javascript://" class="view">复制次数最多</a>
      </div>

      <!-- 搜索 -->
      <div class="search">
        <span>150个行程</span>
        <input type="text" id="search_plan" value="" class="ui2_input" placeholder="在当前结果下搜索" />
              </div>
    </div>

    <!-- 行程无内容 -->
    
    <!-- 行程列表 -->
    <div class="lists clearfix">
      <div class="list">
        <!-- 行程列表内容 -->
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FhBzBTZVI3CmgNOQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-1">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/17d/18/1912309/index/325x240" title="高尔夫蔻蔻的捷克行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>16</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-27 出发</dt>
                  <dd>高尔夫蔻蔻的捷克行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>南宁·深圳·香港·多哈·布拉格·捷克克鲁姆洛夫·萨尔茨堡·哈尔施塔特·维也纳·布达佩斯·卡罗维发利</p>
                </div>
                <div class="number">
                  <span class="icon1">70</span>　|　<span class="icon2">2</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10761847" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/838069" target="_blank" class="name" data-bn-ipg="planhome-plan-username">高尔夫蔻蔻</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI9Cm8NPQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-2">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/117/35/1866581/index/325x240" title="Archie92的日本行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>8</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-15 出发</dt>
                  <dd>Archie92的日本行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>北京·大阪·京都·宇治市·奈良</p>
                </div>
                <div class="number">
                  <span class="icon1">50</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486233" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/7946623" target="_blank" class="name" data-bn-ipg="planhome-plan-username">Archie92</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FvBzNTZlI9Cm8NPQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-3">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/488/42/RUFdRhgFZQ/index/325x240" title="轧米机的老婆的日本行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>7</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-04 出发</dt>
                  <dd>轧米机的老婆的日本行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>上海·名古屋·伊势市·鸟羽市·三重县</p>
                </div>
                <div class="number">
                  <span class="icon1">29</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10952233" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9515039" target="_blank" class="name" data-bn-ipg="planhome-plan-username">轧米机的老婆</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYVI2CmgNOw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-4">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/212/61/Q0hXRBsPZw/index/325x240" title="pjy798的荷兰行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>9</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-10-02 出发</dt>
                  <dd>pjy798的荷兰行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>香港·斯德哥尔摩·马尔默·哥本哈根·阿姆斯特丹·代尔夫特·埃因霍温·乌得勒支·上海</p>
                </div>
                <div class="number">
                  <span class="icon1">19</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11485945" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/4077579" target="_blank" class="name" data-bn-ipg="planhome-plan-username">pjy798</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBzBTZ1I6Cm0NPg/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-5">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/110/dc/1876682/index/325x240" title="思思的美国行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>11</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-04 出发</dt>
                  <dd>思思的美国行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>北京·拉斯维加斯·大峡谷国家公园·盐湖城·黄石国家公园·洛杉矶</p>
                </div>
                <div class="number">
                  <span class="icon1">12</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11463510" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9641604" target="_blank" class="name" data-bn-ipg="planhome-plan-username">user_0u8cCp6OwZ</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI9CmQNOQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-6">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/155/04/1957179/index/325x240" title="半颗小柠檬的希腊行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>8</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-30 出发</dt>
                  <dd>半颗小柠檬的希腊行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>上海·雅典·扎金索斯·圣托里尼</p>
                </div>
                <div class="number">
                  <span class="icon1">25</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486287" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9630440" target="_blank" class="name" data-bn-ipg="planhome-plan-username">半颗小柠檬</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI6CmkNOQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-7">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/1eb/20/1829497/index/325x240" title="user_mAJ7enxkl的西班牙葡萄牙行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>15</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-10-25 出发</dt>
                  <dd>user_mAJ7enxkl的西班牙葡萄牙行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>成都·巴塞罗那·马德里·里斯本·波尔图</p>
                </div>
                <div class="number">
                  <span class="icon1">14</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486557" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9646663" target="_blank" class="name" data-bn-ipg="planhome-plan-username">user_mAJ7enxkl</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FuBzVTbVI6CmsNPg/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-8">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/485/74/RUFQRR4GZw/index/325x240" title="GiroroCheryl的英国行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>15</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-03 出发</dt>
                  <dd>GiroroCheryl的英国行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong>
                </div>
                                <div class="plan">
                  <p>上海·伦敦·贝尔法斯特·温莎</p>
                </div>
                <div class="number">
                  <span class="icon1">35</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10839570" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/5900767" target="_blank" class="name" data-bn-ipg="planhome-plan-username">GiroroCheryl</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20JZFFlBzNTY1I7Cm4/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-9">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/1c8/8e/1915680/index/325x240" title="zhanjan2006的英国行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>17</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-03 出发</dt>
                  <dd>zhanjan2006的英国行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>上海·伦敦·剑桥·爱丁堡·因弗尼斯</p>
                </div>
                <div class="number">
                  <span class="icon1">61</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9735742" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9163839" target="_blank" class="name" data-bn-ipg="planhome-plan-username">zhanjan2006</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI6CmgNPQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-10">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/12a/85/1847329/index/325x240" title="user_mAJ7enxkl的西班牙葡萄牙行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>15</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-10-25 出发</dt>
                  <dd>user_mAJ7enxkl的西班牙葡萄牙行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>成都·巴塞罗那·马德里·里斯本·波尔图</p>
                </div>
                <div class="number">
                  <span class="icon1">21</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486543" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9646663" target="_blank" class="name" data-bn-ipg="planhome-plan-username">user_mAJ7enxkl</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI6Cm4NOg/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-11">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/183/22/1872173/index/325x240" title="angelakent的日本行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>12</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-05 出发</dt>
                  <dd>angelakent的日本行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>广州·东京·大阪</p>
                </div>
                <div class="number">
                  <span class="icon1">20</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486524" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/8213948" target="_blank" class="name" data-bn-ipg="planhome-plan-username">angelakent</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFmBz9TZVI7CmUNNw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-12">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/213/26/Q0hWQBwOZg/index/325x240" title="新加坡之旅" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>7</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-10-22 出发</dt>
                  <dd>新加坡之旅</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>北京·新加坡</p>
                </div>
                <div class="number">
                  <span class="icon1">24</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11091499" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/1445705" target="_blank" class="name" data-bn-ipg="planhome-plan-username">zp0510</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI9CmQNNw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-13">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/659/27/R0xcQB0HYA/index/325x240" title="wssunn的荷兰行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>11</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-05 出发</dt>
                  <dd>wssunn的荷兰行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>上海·阿姆斯特丹</p>
                </div>
                <div class="number">
                  <span class="icon1">19</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486289" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9646574" target="_blank" class="name" data-bn-ipg="planhome-plan-username">wssunn</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFiBz5TYlI7CmQNOw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-14">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/1d9/3c/1828410/index/325x240" title="user_mAJ7enxkl的西班牙葡萄牙行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>15</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-10-25 出发</dt>
                  <dd>user_mAJ7enxkl的西班牙葡萄牙行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>成都·巴塞罗那·马德里·里斯本·波尔图</p>
                </div>
                <div class="number">
                  <span class="icon1">16</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11486485" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9646663" target="_blank" class="name" data-bn-ipg="planhome-plan-username">user_mAJ7enxkl</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFlBz5TYFI-CmsNPQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-15">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/596/21/REBTQBsFYA/index/325x240" title="粒云儿的行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>6</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-30 出发</dt>
                  <dd>粒云儿的行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>深圳·香港·台中市·垦丁·高雄市</p>
                </div>
                <div class="number">
                  <span class="icon1">13</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11384173" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9281145" target="_blank" class="name" data-bn-ipg="planhome-plan-username">粒云儿</a>
          </div>
              </div>
    </div>

    <!-- 翻页 -->
    <div class="pages clearfix">
      <!-- 翻页公用样式 -->
      <div class="ui_page"><a data-bn-ipg="pages-3" data-ra_arg="ra_null|1" data-page="1" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/" class='ui_page_item ui_page_item_current'>1</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|2" data-page="2" href="http://plan.qyer.com/search_0_0_0_0_0_0_2/" class='ui_page_item'>2</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|3" data-page="3" href="http://plan.qyer.com/search_0_0_0_0_0_0_3/" class='ui_page_item'>3</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|4" data-page="4" href="http://plan.qyer.com/search_0_0_0_0_0_0_4/" class='ui_page_item'>4</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|5" data-page="5" href="http://plan.qyer.com/search_0_0_0_0_0_0_5/" class='ui_page_item'>5</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|6" data-page="6" href="http://plan.qyer.com/search_0_0_0_0_0_0_6/" class='ui_page_item'>6</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|7" data-page="7" href="http://plan.qyer.com/search_0_0_0_0_0_0_7/" class='ui_page_item'>7</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|8" data-page="8" href="http://plan.qyer.com/search_0_0_0_0_0_0_8/" class='ui_page_item'>8</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|9" data-page="9" href="http://plan.qyer.com/search_0_0_0_0_0_0_9/" class='ui_page_item'>9</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|10" data-page="10" href="http://plan.qyer.com/search_0_0_0_0_0_0_10/" class='ui_page_item'>10</a>
<a data-bn-ipg="pages-5" data-ra_arg="ra_null|2" data-page="2" href="http://plan.qyer.com/search_0_0_0_0_0_0_2/" class='ui_page_item ui_page_next' title="下一页">下一页</a>
</div>
    </div>
  </div>
            <!--ad-->
      <div class="ad_zone advertising" style="width:980px;height:130px;" id="zoneid-17" data-countries="" data-areas=""></div>
      <!--/ad-->
      

  <!-- 1.5新增列表 -->
  <div class="bot_list  clearfix">
    
    <dl>
      <dt>热门国家路线</dt>
              <dd><a href="http://plan.qyer.com/search_0_0_215_0_0_0_1/">泰国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_14_0_0_0_1/">日本旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_186_0_0_0_1/">法国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_189_0_0_0_1/">意大利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_233_0_0_0_1/">韩国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_213_0_0_0_1/">马来西亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_236_0_0_0_1/">美国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_15_0_0_0_1/">德国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_232_0_0_0_1/">新加坡旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_182_0_0_0_1/">西班牙旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_0_0_13_0_0_0_1/">英国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_524_0_0_0_1/">瑞士旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_219_0_0_0_1/">柬埔寨旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_198_0_0_0_1/">奥地利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_200_0_0_0_1/">荷兰旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_240_0_0_0_1/">澳大利亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_216_0_0_0_1/">越南旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_804_0_0_0_1/">梵蒂冈旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_570_0_0_0_1/">印度尼西亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_193_0_0_0_1/">捷克旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_0_0_424_0_0_0_1/">比利时旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_446_0_0_0_1/">菲律宾旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_195_0_0_0_1/">土耳其旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_241_0_0_0_1/">新西兰旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_206_0_0_0_1/">希腊旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_238_0_0_0_1/">加拿大旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_208_0_0_0_1/">俄罗斯旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_207_0_0_0_1/">匈牙利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_202_0_0_0_1/">瑞典旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_220_0_0_0_1/">尼泊尔旅游线路</a></dd>
          </dl>
  
    <dl>
      <dt>热门主题线路</dt>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_1_1/">美食旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_2_1/">人文旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_3_1/">购物旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_4_1/">游园观光旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_6_1/">沙滩海岛旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_8_1/">自然风光旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_9_1/">自驾旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_10_1/">蜜月旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_11_1/">亲子旅游线路</a></dd>
          </dl>
  
    <dl>
      <dt>热门季节线路</dt>
              <dd><a href="http://plan.qyer.com/search_1_0_0_0_0_0_1/">一月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_2_0_0_0_0_0_1/">二月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_3_0_0_0_0_0_1/">三月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_4_0_0_0_0_0_1/">四月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_5_0_0_0_0_0_1/">五月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_6_0_0_0_0_0_1/">六月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_7_0_0_0_0_0_1/">七月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_8_0_0_0_0_0_1/">八月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_9_0_0_0_0_0_1/">九月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_10_0_0_0_0_0_1/">十月出发旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_11_0_0_0_0_0_1/">十一月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_12_0_0_0_0_0_1/">十二月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_13_0_0_0_0_0_1/">新年出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_14_0_0_0_0_0_1/">春节出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_15_0_0_0_0_0_1/">清明出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_16_0_0_0_0_0_1/">劳动节出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_17_0_0_0_0_0_1/">端午出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_18_0_0_0_0_0_1/">中秋出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_19_0_0_0_0_0_1/">国庆出发旅游线路</a></dd>
          </dl>
  </div>

  <!-- 全站底部 -->
    <div style="display: none;">http://plan.qyer.com/search_0_0_195_0_0_0_1/?cityid=8918</div>
<div class="qyer_footer">
	<div class="topline"></div>
	<div class="content">
		<p class="nav">
			<a href="//www.qyer.com/htmlpages/about.html" target="_blank" rel="nofollow" data-bn-ipg="foot-about-1">穷游简介</a>
			<a href="//www.qyer.com/partner/" target="_blank" rel="nofollow" data-bn-ipg="foot-about-3">合作伙伴</a>
			<a href="//www.qyer.com/job/" target="_blank" rel="nofollow" data-bn-ipg="foot-join-1">加入我们</a>
			<a href="//site.qyer.com/tyro/" target="_blank" rel="nofollow" data-bn-ipg="foot-help-1">新手上路</a>
			<a href="//bbs.qyer.com/forum-10-1.html" target="_blank" rel="nofollow" data-bn-ipg="foot-help-2">使用帮助</a>
			<a href="//www.qyer.com/sitemap.html" target="_blank" data-bn-ipg="foot-help-4">网站地图</a>
			<a href="//www.qyer.com/htmlpages/member.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-1">会员条款</a>
			<a href="//www.qyer.com/htmlpages/bbsguide.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-2">社区指南</a>
			<a href="//www.qyer.com/htmlpages/copyright.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-3">版权声明</a>
			<a href="//www.qyer.com/htmlpages/exemption.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-4">免责声明</a>
			<a href="//www.qyer.com/htmlpages/contact.html" target="_blank" rel="nofollow" data-bn-ipg="foot-about-2">联系我们</a>
		</p>
		<p class="info">
			2004-2017 &copy; 穷游网&reg;  qyer.com All rights reserved. Version v5.57  京ICP备12003524号  京公网安备11010102001935号  京ICP证140673号
			<a target="_blank" style="color:inherit;" href="//static.qyer.com/images/yyzz.jpg">营业执照</a>
			<a target="_blank" style="color:inherit;" href="//static.qyer.com/images/jyxkz.jpg">经营许可证</a>
		</p>
    
        <!--友情链接模块-->
        
	</div>
</div>



<script>
        var script   = document.createElement("script");
        script.type  = "text/javascript";
        script.async = true;
        script.src   = "//static.qyer.com/qyer_ui_frame/m/js/dist/base_beacon_ga.js";
        document.getElementsByTagName("head")[0].appendChild(script);
</script>
  <!-- /全站底部 -->

  <!-- 底部公用 -->
  <!--div class="qr-code-fixed" style="cursor:pointer">
    <a href="javascript:;" alt="关闭">关闭</a>
  </div-->

  <!--创建新的行程 更多选择-->
  <ul class="createFun createFun2 fontYaHei" id="createBtnMore">
    <li><a data-bn-ipg="planhome-1-createplan-bymyself" href="/create" target="_blank">自己制定</a></li>
    <li><a data-bn-ipg="planhome-1-createplan-createforme" href="/smartcreate/" target="_blank">帮我制定</a></li>
  </ul>
  <!--/创建新的行程 更多选择-->

  <!--loading 弹层-->
  <div class="plan-dialog plan-dialog-loading" style="display:none;">
    <div class="plan-dialog-bg"></div>
    <div class="plan-dialog-icon">
      <img src="//common3.qyerstatic.com/plan/new/project/web/plan/img/loadingding.gif">
      <i>行程复制中...</i>
    </div>
  </div>
  <!--/loading 弹层-->


  <script src="//common1.qyerstatic.com/plan/desktop/home/js/footer.e45492a2144a472068720915eb851bf0.js"></script>
</body>
</html>


'''

testpa = re.compile(u'\s*<!DOCTYPE html>(.*)<body>(.*)</body>.*',flags=re.DOTALL)
#这个表达式只能找到1个
testpa1 = re.compile(u'<div id="js_continents" class="tabMain"  >.*(?:<ul .*>(.*)</ul>\s*){7}.*<div  id="js_cityList',re.DOTALL)
#res = testpa1.search(test)#search函数查找匹配的字符串,直到找到第一个匹配就返回，找到后返回_sre.SRE_Match对象，该对象有group()函数
#r = testpa1.match(test)#match函数从字符串头匹配，匹配不上返回None，找到后返回_sre.SRE_Match对象，
#findall函数直接返回一个列表
#finditer函数返回迭代器
#rr = testpa.match(test)
#print(rr.group(1))
#这里用到了非贪婪方式,默认是贪婪的，下面的正则表达式如果没有?,是贪婪的。将直接匹配到文本的最后一个</ul>.但是加上?之后，按最近的来。
#非贪婪方式的使用方式就是把问号加在表示不定次数后面。
newtest = '''

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="keywords" content="去澳大利亚旅游行程,到澳大利亚推荐旅游线路,到澳大利亚旅游计划">
  <meta name="description" content="到澳大利亚最佳旅游线路推荐,到澳大利亚自由行旅游线路定制,出发去澳大利亚最佳旅游线路推荐及详细旅游行程安排">
  <meta name="google-site-verification"
        content="DVVM1p1HEm8vE1wVOQ9UjcKP--pNAsg_pleTU5TkFaM">
  <title>到澳大利亚旅游线路 - 穷游行程助手</title>
  <link rel="shortcut icon" href="//www.qyer.com/favicon.ico">
  <link rel="stylesheet" href="//common2.qyerstatic.com/plan/desktop/home/css/style.61bf817d75b39188df4010786f85adc3.css">
  <script>
    window.QYER = {
      uid: [0][0] || 0
    };
    window._RATrack = window._RATrack||{
      'platform': 'web',
      'channel':'plan',
      'page_type':'list',
      'ugc_type':'plan_search',
      'ugc_content':''
    };
  </script>
  
<script>
  window.__pageData__ = {
    citys:[
          ],
      level:[
            {text:'一级精华',url:'http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&elite=1'},
            {text:'二级精华',url:'http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&elite=2'},
            {text:'三级精华',url:'http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&elite=3'},
          ],
    urlParameter:{
      startTime:'0',
      place:'240',
      datCount:'0',
      topic:'0',
      city:'6606',
      essence:'0',
      order:'0',
      page:'0',
      kw:'0'
    },
    t :1502175116
    //1468209600
  };
</script>
<style type="text/css">
  .q-layer-header .logo{width: auto!important;}
</style>

  <script src="//common1.qyerstatic.com/plan/desktop/shared/js/header.8ca03cdbf7c946554afe9b49f686ef20.js"></script>
</head>
<body>
  

      






        

<style type="text/css">
.zpui-head-ad { position: relative; z-index: 2; }
.zpui-head-ad .bg { display: block; height: 60px; width: 100%; background: url(//static.qyer.com/other/ad/20170808/web.jpg) center top no-repeat; }
.zpui-head-ad .close { position: absolute; display: block; cursor: pointer; background: url(//static.qyer.com/other/ad/20160512/web-ad-close.png) center center no-repeat; left: 50%; top: 50%; width: 30px; height: 30px; margin-left: 440px; margin-top: -15px; }
</style>

<div id="zpui-head-ad" class="zpui-head-ad">
	<a href="//z.qyer.com/zt/20170808/?campaign=tonglan&category=20170808" target="_blank" class="bg"></a>
	<span id="zpui-head-ad-close" class="close"></span>
</div>

<script type="text/javascript">
(function() {
	function setCookie(name, value) {
		var exp = new Date();
		exp.setTime(exp.getTime() + 86400000);
		document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString() + ";path=/;domain=qyer.com";
	};
	function getCookie(objName){
		var arrStr = document.cookie.split("; ");
		for(var i = 0;i < arrStr.length;i ++){
			var temp = arrStr[i].split("=");
			if(temp[0] == objName) return unescape(temp[1]);
	   } 
	}
	document.getElementById("zpui-head-ad-close").onclick = function(){
		if($){$("#zpui-head-ad").slideUp(200); }
		else{document.getElementById("zpui-head-ad").style.display="none";}
		setCookie("qy_topad", 1);
	}
})(); 
</script>
<style>
    .tip_passport_bindmobile{height: 40px; line-height: 40px; background-color: rgb(224, 241, 223); font-size: 14px; padding-left: 28px; position: relative; margin-top: -40px;transition:All .3s ease; -webkit-transition:All .3s ease; -moz-transition:All .3s ease; -o-transition:All .3s ease;color:#323232;}
    .tip_passport_bindmobile a{color: #323232; text-decoration: underline;}
    .tip_passport_bindmobile img{width:12px;height:12px;position: absolute; top: 15px; right: 17px; cursor: pointer; }

    .tip_passport_bindmobile_masker{position:fixed;top:0;left:0;width:100%;height:100%;background-image:url(//static.qyer.com/models/common/images/bg_255_255_255_0.7.png);z-index:2000;display: none; }
    .tip_passport_bindmobile_dialog{box-sizing: border-box; width: 340px; height: 180px; border: solid 1px rgb(192, 192, 192); background-color: rgb(255, 255, 255); box-shadow: 0 0 10px #ccc; position: absolute; top: 50%; left: 50%; margin: -90px 0 0 -170px; padding: 30px 20px 0 20px; } 
    .tip_passport_bindmobile_dialog_title{font-size: 18px;color: #323232;text-align: center;margin-bottom: 5px; } 
    .tip_passport_bindmobile_dialog_text{font-size: 14px;color: #959595;}
    .tip_passport_bindmobile_dialog_btn{width:84px;height:28px;line-height:28px;display:inline-block;font-size:14px;color:rgb(50,50,50);text-decoration:none !important;margin-top:15px;background-color:rgb(236,236,236);border:solid 1px rgb(192,192,192);cursor:pointer;border-radius:3px;}
    .tip_passport_bindmobile_dialog_btn:hover{background-color:rgb(243,243,243);}
    .tip_passport_bindmobile_dialog_btnBind{margin-left:20px; background-color:rgb(59,160,92); border:solid 1px rgb(59,160,92); color:#fff; }
    .tip_passport_bindmobile_dialog_btnBind:hover{background-color:rgb(71,197,113); border:solid 1px rgb(71,197,113); }
    .tip_passport_bindmobile_dialog_close{position:absolute;top:16px;right:16px;cursor:pointer;}
</style>
<div id="tip_passport_bindmobile" class="tip_passport_bindmobile">
	<span>
		穷游网将实行手机绑定实名制，为了您的帐号安全请及时绑定手机号。
    	<a target="_blank" href="//bbs.qyer.com/thread-2779523-1.html">查看详细说明</a>
	</span>
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpBRjUzNThGRDU3QkQxMUU3QjUyQ0M1QkZCNDUzNkFCOCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpBRjUzNThGRTU3QkQxMUU3QjUyQ0M1QkZCNDUzNkFCOCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkFGNTM1OEZCNTdCRDExRTdCNTJDQzVCRkI0NTM2QUI4IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkFGNTM1OEZDNTdCRDExRTdCNTJDQzVCRkI0NTM2QUI4Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Lb1GqgAAAKlJREFUeNqckkEOwiAQRQc8GFvO0AULjNF4IKMx7aILz9AlHMdDGPyYT0MomzrJD014bwJMVQjhLSIL4o0xH+lUjPGAZUKsJuyQmRs9eCazZMEjL2RopQoeyHiVUmo3RuRE54kcCbt85J9QdXsQuFO4sMG53G8VKCksN4JC8Qp4hbTsrP+OtOvSGFz7dK506zyr05zgBs7Fb1fNacqCLZPs/RqVlBn7FWAASJhkb97XPw8AAAAASUVORK5CYII=" />
</div>
<div id="tip_passport_bindmobile_masker" class="tip_passport_bindmobile_masker">
    <div class="tip_passport_bindmobile_dialog">
        <h5 class="tip_passport_bindmobile_dialog_title">帐号安全提示</h5>
        <p class="tip_passport_bindmobile_dialog_text">穷游网将实行手机绑定实名制，为了您的帐号安全，请及时绑定手机号。</p>
        <div style="text-align:center;"> 
            <a class="tip_passport_bindmobile_dialog_btn" href="//bbs.qyer.com/thread-2779523-1.html" target="_blank" >查看说明</a>
            <a class="tip_passport_bindmobile_dialog_btn tip_passport_bindmobile_dialog_btnBind"  href="//passport.qyer.com/account/mobile/bind" target="_blank" >立即绑定</a>
        </div>
        <img id="tip_passport_bindmobile_dialog_close" class="tip_passport_bindmobile_dialog_close" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpBNTMyODU3OTU5OEExMUU3QTgwMUVFNzYzN0YwQkI1NSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpBNTMyODU3QTU5OEExMUU3QTgwMUVFNzYzN0YwQkI1NSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkE1MzI4NTc3NTk4QTExRTdBODAxRUU3NjM3RjBCQjU1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkE1MzI4NTc4NTk4QTExRTdBODAxRUU3NjM3RjBCQjU1Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+jb9fzQAAAKlJREFUeNqckkEOwiAQRQc8GFvO0AULjNF4IKMx7aILz9AlHMdDGPyYT0MomzrJD014bwJMVQjhLSIL4o0xH+lUjPGAZUKsJuyQmRs9eCazZMEjL2RopQoeyHiVUmo3RuRE54kcCbt85J9QdXsQuFO4sMG53G8VKCksN4JC8Qp4hbTsrP+OtOvSGFz7dK506zyr05zgBs7Fb1fNacqCLZPs/RqVlBn7FWAASJhkb97XPw8AAAAASUVORK5CYII=" />
    </div>
</div>
<script>
    (function(){

        function setCookie(name, value,time) {
            var exp = new Date();
            exp.setTime(exp.getTime() + (time||259200000));
            document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString() + ";path=/;domain=qyer.com";
        };
        function getCookie(objName){
            var arrStr = document.cookie.split("; ");
            for(var i = 0;i < arrStr.length;i ++){
                var temp = arrStr[i].split("=");
                if(temp[0] == objName) return unescape(temp[1]);
           } 
        }

        window.__userStatusCallBack = function (data) {

            // 显示通栏
            (function(){
                var isShowTopTip = data.uid 
                            && data.userinfo.bind_phone!=1 
                            && getCookie('tip_passport_bindmobile')!="1"
                            && !/^https?:\/\/qyer\.com/gi.test(location.href)
                            ;
                // 显示顶部提示
				var $dom = $('#tip_passport_bindmobile');
                if(isShowTopTip){
                    $dom.css('marginTop','0').find('img').click(function(){
                        $dom.css('marginTop','-40px');
                        setCookie('tip_passport_bindmobile',1);
						setTimeout(function(){
                            $dom.remove()
                        },500);
                    })
                }else{
					$dom.remove()
				}
            })();


            // 增加 UGC 监听，关键操作出现绑定账号提示
            (function(){
                if(data.uid && data.userinfo.bind_phone!=1 ){
                    // modal 关闭事件
                    $('#tip_passport_bindmobile_dialog_close').on('click',function(){
                        $('#tip_passport_bindmobile_masker').remove();
                        setCookie('tip_passport_ugc_bindmobile',1);
                    });

                    // 代理全局 mousedown 事件，判断用户行为，进行绑定弹窗提示
                    var filter = [
                        '[data-bn-ipg=index-head-userdrop-poicomment]', // 写点评
                        '.cfsub.cn-pub', // 写帖子
                        '.ask_askhelp_btn', // 提问
                        '[data-bn-ipg=planhome-createplan]', // 创建行程-自己制定
                        '[data-bn-ipg=planhome-1-createplan-bymyself]', // 创建行程-自己制定
                        '[data-bn-ipg=planhome-1-createplan-createforme]', // 创建行程-帮我制定
                        '#addPhoto.ui-button.btn-default-full.btn-upload', // 上传图片
                    ].join(',')
                    $(document.body).on('mousedown',filter,function(){
                        if( getCookie('tip_passport_ugc_bindmobile') != '1' ){
                            $('#tip_passport_bindmobile_masker').show();
                            return false;
                        }
                    });
                }
            })();

        }
    })();
</script>

<script>
	window.QYER={uid:[0][0]||0};

	window._RATrack = window._RATrack||{
	 	'platform':'web',
 		'channel':'plan',
	 	'page_type':'list',
 		'ugc_type':'plan_search',
	 	'ugc_content':''
	};
</script>

<link href="//static.qyer.com/models/common/component/headfoot/dist/headerfoot_black.min.css"  rel="stylesheet" />
<script src="//static.qyer.com/models/common/component/headfoot/dist/headerfoot_black.min.js" async="async"></script>




<div class="q-layer-header">
    <div class="header-inner">
        <a data-bn-ipg="head-logo" href="//www.qyer.com"><img class="logo" src="//static.qyer.com/models/common/component/headfoot/icon/logo_116x36.png" width="58" height="18" /></a>
        <div class="nav">
            <ul class="nav-ul">
                <li class="nav-list "><a class="nav-span" href="//place.qyer.com/" data-bn-ipg="head-nav-place" title="穷游目的地">目的地</a></li>
                <li class="nav-list "><a class="nav-span" href="//guide.qyer.com/" data-bn-ipg="head-nav-guide" title="穷游锦囊">锦囊</a></li>
                <li class="nav-list nav-list-plan nav-list-selected">
                    <a class="nav-span" href="//plan.qyer.com/" data-bn-ipg="head-nav-plan" title="穷游行程助手">行程助手</a>
                </li>
                <li class="nav-list nav-list-layer  ">
                    <a class="nav-span" href="//bbs.qyer.com/" data-bn-ipg="head-nav-community" title="穷游论坛">社区<i class="iconfont icon-jiantouxia"></i></a>
                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li class="nav-list-layer">
                                <a href="//bbs.qyer.com" data-bn-ipg="head-nav-bbs" title="穷游论坛"><i class="iconfont icon-bbs1"></i> 旅行论坛 <i class="iconfont icon-jiantouyou"></i></a>
                                <div class="q-layer q-layer-section">
                                    <div class="q-layer">
                                        <div class="section-title">
                                            <a class="more" href="//bbs.qyer.com">全部版块<i class="iconfont icon-jiantouyou"></i></a>
                                            <span>热门版块</span>
                                        </div>


                                                                                                                           <dl class="section-item">
                                             <dt>兴趣小组</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-2" href="//bbs.qyer.com/forum-2-1.html">结伴同游</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-3" href="//bbs.qyer.com/forum-3-1.html">签证</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-22" href="//bbs.qyer.com/forum-22-1.html">旅行摄影</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-88" href="//bbs.qyer.com/forum-88-1.html">潜水俱乐部</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-122" href="//bbs.qyer.com/forum-122-1.html">带孩子旅行</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-49" href="//bbs.qyer.com/forum-49-1.html">明信片</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-100" href="//bbs.qyer.com/forum-100-1.html">旅行购物</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游欧洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-14" href="//bbs.qyer.com/forum-14-1.html">法国/摩纳哥</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-12" href="//bbs.qyer.com/forum-12-1.html">德国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-16" href="//bbs.qyer.com/forum-16-1.html">英国/爱尔兰</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-15" href="//bbs.qyer.com/forum-15-1.html">瑞士/列支敦士登</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-162" href="//bbs.qyer.com/forum-162-1.html">土耳其</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-25" href="//bbs.qyer.com/forum-25-1.html">挪威/瑞典/芬兰/丹麦/冰岛</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-13" href="//bbs.qyer.com/forum-13-1.html">意大利/梵蒂冈/圣马力诺/马耳他</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游亚洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-52" href="//bbs.qyer.com/forum-52-1.html">台湾</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-57" href="//bbs.qyer.com/forum-57-1.html">日本</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-106" href="//bbs.qyer.com/forum-106-1.html">泰国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-164" href="//bbs.qyer.com/forum-164-1.html">新加坡</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-165" href="//bbs.qyer.com/forum-165-1.html">斯里兰卡</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-163" href="//bbs.qyer.com/forum-163-1.html">香港/澳门</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-108" href="//bbs.qyer.com/forum-108-1.html">马来西亚/文莱</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-175" href="//bbs.qyer.com/forum-175-1.html">柬埔寨</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-104" href="//bbs.qyer.com/forum-104-1.html">马尔代夫</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-177" href="//bbs.qyer.com/forum-177-1.html">缅甸</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-59" href="//bbs.qyer.com/forum-59-1.html">伊朗</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-103" href="//bbs.qyer.com/forum-103-1.html">印度/孟加拉</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游美洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-54" href="//bbs.qyer.com/forum-54-1.html">加拿大</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-53" href="//bbs.qyer.com/forum-53-1.html">美国</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-168" href="//bbs.qyer.com/forum-168-1.html">中美</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-55" href="//bbs.qyer.com/forum-55-1.html">南美/南极</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游大洋洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-56" href="//bbs.qyer.com/forum-56-1.html">澳大利亚</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-83" href="//bbs.qyer.com/forum-83-1.html">新西兰</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-178" href="//bbs.qyer.com/forum-178-1.html">太平洋海岛</a>
                                                                                              </dd>
                                         </dl>
                                                                                  <dl class="section-item">
                                             <dt>穷游非洲</dt>
                                             <dd>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-173" href="//bbs.qyer.com/forum-173-1.html">东非地区</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-174" href="//bbs.qyer.com/forum-174-1.html">非洲海岛</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-86" href="//bbs.qyer.com/forum-86-1.html">北非地区</a>
                                                                                                  <a data-bn-ipg="index-head-bbs-hotboard-60" href="//bbs.qyer.com/forum-60-1.html">非洲其他国家</a>
                                                                                              </dd>
                                         </dl>
                                         

                                    </div>
                                </div>
                            </li>
                            <li><a href="//ask.qyer.com/" data-bn-ipg="head-nav-ask" title="旅行问答"><i class="iconfont icon-ask1"></i> 旅行问答</a></li>
                            <li><a href="//jne.qyer.com/" data-bn-ipg="head-nav-qlab" title="JNE旅行生活美学" target="_blank"><i class="iconfont icon-jne1"></i> JNE旅行生活美学</a></li>
                            <li><a href="//zt.qyer.com/" data-bn-ipg="head-nav-zt" title="特别策划" target="_blank"><i class="iconfont icon-zt"></i> 特别策划</a></li>
                            <li><a href="//rt.qyer.com/" data-bn-ipg="head-nav-rt" title="负责任的旅行" target="_blank"><i class="iconfont icon-rt1"></i> 负责任的旅行</a></li>
                        </ul>
                    </div>
                </li>

                <li class="nav-list nav-list-layer nav-list-zuishijie ">
                    <a class="nav-span" href="//z.qyer.com/" data-bn-ipg="head-nav-lastminute" title="穷游商城">穷游商城<i class="iconfont icon-jiantouxia"></i></a>
                    <div class="gif">
                        <img class="gif1" src="//static.qyer.com/models/common/component/headfoot/icon/gif.gif" height="19" width="44" >
                    </div>

                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li><a href="//z.qyer.com/package/" data-bn-ipg="head-nav-package" target="_blank" title="机酒自由行"><i class="iconfont icon-package"></i> 机酒自由行</a></li>
                            <li><a href="//z.qyer.com/local/" data-bn-ipg="head-nav-local" target="_blank" title="当地玩乐"><i class="iconfont icon-local"></i> 当地玩乐</a></li>
                            <li><a href="//z.qyer.com/visa/" data-bn-ipg="head-nav-visa" target="_blank" title="签证"><i class="iconfont icon-visa1"></i> 签证</a></li>
                            <li><a href="//z.qyer.com/cruise/" data-bn-ipg="head-nav-cruise" target="_blank" title="邮轮"><i class="iconfont icon-cruise"></i> 邮轮</a></li>
                            <li><a href="//z.qyer.com/explore/" data-bn-ipg="head-nav-explore" target="_blank" title="深度旅行"><i class="iconfont icon-explore"></i> 深度旅行</a></li>
                            <li><a href="//bx.qyer.com/" data-bn-ipg="head-nav-insure" target="_blank" title="保险"><i class="iconfont icon-bx"></i> 保险</a></li>
                            <li><a href="//z.qyer.com/travelgroup" data-bn-ipg="head-nav-travelgroup" target="_blank" title="私人订制"><i class="iconfont icon-travelgroup"></i> 私人定制</a></li>
                        </ul>
                    </div>
                </li>

                <li class="nav-list "><a class="nav-span" href="//flight.qyer.com/" data-bn-ipg="head-nav-plane" title="机票">机票</a></li>

                <li class="nav-list "><a class="nav-span" href="//hotel.qyer.com/" data-bn-ipg="head-nav-hotel" title="穷游酒店">酒店</a></li>

                <li class="nav-list nav-list-layer nav-list-yuding">
                    <span class="nav-span">预订<i class="iconfont icon-jiantouxia"></i></span>
                    <div class="q-layer q-layer-nav q-layer-arrow">
                        <ul>
                            <li><a href="//www.qyer.com/hoteldeal/" data-bn-ipg="head-nav-hoteldeal" title="特价酒店"><i class="iconfont icon-hoteldeal"></i> 特价酒店</a></li>
                            <li><a href="//www.qyer.com/goto.php?url=https%3A%2F%2Fwww.airbnbchina.cn%2F%3Faf%3D104561116%26c%3DRESERVATION" data-bn-ipg="head-nav-airbnb" title="爱彼迎" target="_blank"><i class="iconfont icon-airbnb1"></i> 爱彼迎</a></li>
                            <li><a href="//www.qyer.com/shop/" data-bn-ipg="head-nav-shop" title="华人旅馆"><i class="iconfont icon-shop"></i> 华人旅馆</a></li>
                            <li><a href="//z.qyer.com/car/?utm_source=c03729731-pc&utm_medium=partner&utm_campaign=entry&utm_term=qyer_nav" data-bn-ipg="head-nav-car" title="租车"><i class="iconfont icon-car"></i> 租车</a></li>
                        </ul>
                    </div>
                </li>
                <!-- <li class="nav-list"><a class="nav-span icon-phone-a" href="//app.qyer.com"><i class="iconfont icon-phone"></i>手机穷游</a></li> -->
            </ul>
        </div>
        <div class="fun">
            <div id="siteSearch" class="nav-search">
                <form action="//search.qyer.com/index" method="get">
                    <input class="txt" name="wd" type="text" autocomplete="off">
                    <button class="btn" type="submit"><i class="iconfont icon-sousuo"></i><span>搜索</span></button>
                </form>
            </div>
            <div id="js_qyer_header_userStatus" class="status">
              <div class="login show">
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606" rel="noflow" data-bn-ipg="index-head-un-qq" data-type="qq"><i class="iconfont icon-qq"></i></a>
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606" rel="noflow" data-bn-ipg="index-head-un-weibo" data-type="weibo"><i class="iconfont icon-weibo"></i></a>
                    <a class="otherlogin-link" href="javascript:;" url="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606" rel="noflow" data-bn-ipg="index-head-un-wechat" data-type="weixin"><i class="iconfont icon-weixin"></i></a>

                    <a href="https://passport.qyer.com/register/mobile?refer=http://plan.qyer.com%2Fsearch_0_0_240_0_0_0_1%2F%3Fcityid%3D6606" data-bn-ipg="index-head-un-register">注册</a>
                    <a href="https://passport.qyer.com/login?refer=http://plan.qyer.com%2Fsearch_0_0_240_0_0_0_1%2F%3Fcityid%3D6606" data-bn-ipg="index-head-un-login">登录</a>
              </div>
            </div>
        </div>
    </div>
</div>

<!--token:d41d8cd98f00b204e9800998ecf8427e-->  
  <!-- <div id="updateTip" style="position: absolute; top: 57px; left:0; right:0; background-color: #ffffe4; border: solid 1px #ffd992; text-align: center; height: 53px; line-height: 53px; font-size: 18px; color: #323232; padding: 0 20px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;z-index:100000;max-width:1024px;margin:0 auto;">
      因维护升级，7.24日23点至次日6点（北京时间），行程助手可能出现服务异常，抱歉带来不便。
      <div style="position: absolute; right: 9px; top: -10px; font-size: 12px; cursor: pointer; font-weight: bold; color: #6d6d66; " onclick="$('#updateTip').remove()" >X</div>
  </div> -->

      <!--面包屑 -->
    <div class="qyer_head_crumbg">
      <div class="qyer_head_crumb">
        <span class="text"><a href="//www.qyer.com/" data-bn-ipg = "bgimg-bc-index">穷游</a></span>
        <span class="space">&gt;</span>
        <span class="text"><a href="//plan.qyer.com/" data-bn-ipg = 'bgimg-bc-plan'>行程助手</a></span>
        <span class="space">&gt;</span>
        <h1 class="current">搜索行程</h1>
      </div>
    </div>
    <!--面包屑 -->
  
  <!-- 首页筛选 -->
  <div class="ind_sifter">
        <div class="items clearfix" style="display: ;">
      <strong class="title">
        已选条件:
      </strong>
      <div class="ylist clearfix">
                <span class="tag" data-type="countryName" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/" data-val="澳大利亚">目的地：<strong>澳大利亚</strong><a class="clearfilter" href="http://plan.qyer.com/search_0_0_0_0_0_0_1/" data-bn-ipg="planhome-select-delete"></a></span>
                <span class="tag" data-type="countryName" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/" data-val="北领地">城市：<strong>北领地</strong><a class="clearfilter" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/" data-bn-ipg="planhome-select-delete"></a></span>
              </div>
    </div>
    
    

    
    <div id="js_selectCountry" class="selectCountry" style="display:none">
      <div class="tab">
        <ul class="fontYaHei">
          <li class="js_cmd current" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country" class="current"> 亚洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 欧洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 非洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 北美洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 南美洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 大洋洲 </li>
          <li class="js_cmd" data-cmd="change_continents" data-bn-ipg="planhome-select-continent1-country"> 南极洲 </li>
        </ul>
        <div class="close" data-bn-ipg="planhome-select-continent-close">
          <span class="js_cmd" data-cmd="place_close2"> </span>
        </div>
        <div class="search">
          <input type="text" id="search_city" class="ui2_input" placeholder="搜索你想要去的国家"
          data-bn-ipg="planhome-select-more-searchcountry">
        </div>
      </div>
      <div id="js_continents" class="tabMain"  >
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="11" data-key="中国" href="http://plan.qyer.com/search_0_0_11_0_0_0_1/?cityid=6606">中国</a></li>
                    <li><a data-id="215" data-key="泰国" href="http://plan.qyer.com/search_0_0_215_0_0_0_1/?cityid=6606">泰国</a></li>
                    <li><a data-id="14" data-key="日本" href="http://plan.qyer.com/search_0_0_14_0_0_0_1/?cityid=6606">日本</a></li>
                    <li><a data-id="233" data-key="韩国" href="http://plan.qyer.com/search_0_0_233_0_0_0_1/?cityid=6606">韩国</a></li>
                    <li><a data-id="213" data-key="马来西亚" href="http://plan.qyer.com/search_0_0_213_0_0_0_1/?cityid=6606">马来西亚</a></li>
                    <li><a data-id="232" data-key="新加坡" href="http://plan.qyer.com/search_0_0_232_0_0_0_1/?cityid=6606">新加坡</a></li>
                    <li><a data-id="219" data-key="柬埔寨" href="http://plan.qyer.com/search_0_0_219_0_0_0_1/?cityid=6606">柬埔寨</a></li>
                    <li><a data-id="216" data-key="越南" href="http://plan.qyer.com/search_0_0_216_0_0_0_1/?cityid=6606">越南</a></li>
                    <li><a data-id="570" data-key="印度尼西亚" href="http://plan.qyer.com/search_0_0_570_0_0_0_1/?cityid=6606">印度尼西亚</a></li>
                    <li><a data-id="446" data-key="菲律宾" href="http://plan.qyer.com/search_0_0_446_0_0_0_1/?cityid=6606">菲律宾</a></li>
                    <li><a data-id="220" data-key="尼泊尔" href="http://plan.qyer.com/search_0_0_220_0_0_0_1/?cityid=6606">尼泊尔</a></li>
                    <li><a data-id="402" data-key="阿联酋" href="http://plan.qyer.com/search_0_0_402_0_0_0_1/?cityid=6606">阿联酋</a></li>
                    <li><a data-id="537" data-key="斯里兰卡" href="http://plan.qyer.com/search_0_0_537_0_0_0_1/?cityid=6606">斯里兰卡</a></li>
                    <li><a data-id="497" data-key="马尔代夫" href="http://plan.qyer.com/search_0_0_497_0_0_0_1/?cityid=6606">马尔代夫</a></li>
                    <li><a data-id="231" data-key="印度" href="http://plan.qyer.com/search_0_0_231_0_0_0_1/?cityid=6606">印度</a></li>
                    <li><a data-id="511" data-key="缅甸" href="http://plan.qyer.com/search_0_0_511_0_0_0_1/?cityid=6606">缅甸</a></li>
                    <li><a data-id="487" data-key="老挝" href="http://plan.qyer.com/search_0_0_487_0_0_0_1/?cityid=6606">老挝</a></li>
                    <li><a data-id="568" data-key="伊朗" href="http://plan.qyer.com/search_0_0_568_0_0_0_1/?cityid=6606">伊朗</a></li>
                    <li><a data-id="476" data-key="卡塔尔" href="http://plan.qyer.com/search_0_0_476_0_0_0_1/?cityid=6606">卡塔尔</a></li>
                    <li><a data-id="569" data-key="以色列" href="http://plan.qyer.com/search_0_0_569_0_0_0_1/?cityid=6606">以色列</a></li>
                    <li><a data-id="572" data-key="约旦" href="http://plan.qyer.com/search_0_0_572_0_0_0_1/?cityid=6606">约旦</a></li>
                    <li><a data-id="436" data-key="朝鲜" href="http://plan.qyer.com/search_0_0_436_0_0_0_1/?cityid=6606">朝鲜</a></li>
                    <li><a data-id="558" data-key="文莱" href="http://plan.qyer.com/search_0_0_558_0_0_0_1/?cityid=6606">文莱</a></li>
                    <li><a data-id="507" data-key="蒙古" href="http://plan.qyer.com/search_0_0_507_0_0_0_1/?cityid=6606">蒙古</a></li>
                    <li><a data-id="414" data-key="巴基斯坦" href="http://plan.qyer.com/search_0_0_414_0_0_0_1/?cityid=6606">巴基斯坦</a></li>
                    <li><a data-id="488" data-key="黎巴嫩" href="http://plan.qyer.com/search_0_0_488_0_0_0_1/?cityid=6606">黎巴嫩</a></li>
                    <li><a data-id="508" data-key="孟加拉国" href="http://plan.qyer.com/search_0_0_508_0_0_0_1/?cityid=6606">孟加拉国</a></li>
                    <li><a data-id="532" data-key="沙特阿拉伯" href="http://plan.qyer.com/search_0_0_532_0_0_0_1/?cityid=6606">沙特阿拉伯</a></li>
                    <li><a data-id="2041" data-key="巴勒斯坦" href="http://plan.qyer.com/search_0_0_2041_0_0_0_1/?cityid=6606">巴勒斯坦</a></li>
                    <li><a data-id="461" data-key="哈萨克斯坦" href="http://plan.qyer.com/search_0_0_461_0_0_0_1/?cityid=6606">哈萨克斯坦</a></li>
                    <li><a data-id="433" data-key="不丹" href="http://plan.qyer.com/search_0_0_433_0_0_0_1/?cityid=6606">不丹</a></li>
                    <li><a data-id="416" data-key="巴林" href="http://plan.qyer.com/search_0_0_416_0_0_0_1/?cityid=6606">巴林</a></li>
                    <li><a data-id="403" data-key="阿曼" href="http://plan.qyer.com/search_0_0_403_0_0_0_1/?cityid=6606">阿曼</a></li>
                    <li><a data-id="562" data-key="乌兹别克斯坦" href="http://plan.qyer.com/search_0_0_562_0_0_0_1/?cityid=6606">乌兹别克斯坦</a></li>
                    <li><a data-id="564" data-key="叙利亚" href="http://plan.qyer.com/search_0_0_564_0_0_0_1/?cityid=6606">叙利亚</a></li>
                    <li><a data-id="481" data-key="科威特" href="http://plan.qyer.com/search_0_0_481_0_0_0_1/?cityid=6606">科威特</a></li>
                    <li><a data-id="401" data-key="阿富汗" href="http://plan.qyer.com/search_0_0_401_0_0_0_1/?cityid=6606">阿富汗</a></li>
                    <li><a data-id="468" data-key="吉尔吉斯斯坦" href="http://plan.qyer.com/search_0_0_468_0_0_0_1/?cityid=6606">吉尔吉斯斯坦</a></li>
                    <li><a data-id="1035" data-key="伊拉克" href="http://plan.qyer.com/search_0_0_1035_0_0_0_1/?cityid=6606">伊拉克</a></li>
                    <li><a data-id="544" data-key="塔吉克斯坦" href="http://plan.qyer.com/search_0_0_544_0_0_0_1/?cityid=6606">塔吉克斯坦</a></li>
                    <li><a data-id="567" data-key="也门" href="http://plan.qyer.com/search_0_0_567_0_0_0_1/?cityid=6606">也门</a></li>
                    <li><a data-id="552" data-key="土库曼斯坦" href="http://plan.qyer.com/search_0_0_552_0_0_0_1/?cityid=6606">土库曼斯坦</a></li>
                    <li><a data-id="438" data-key="东帝汶" href="http://plan.qyer.com/search_0_0_438_0_0_0_1/?cityid=6606">东帝汶</a></li>
                    <li><a data-id="1425" data-key="英属印度洋领地" href="http://plan.qyer.com/search_0_0_1425_0_0_0_1/?cityid=6606">英属印度洋领地</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="186" data-key="法国" href="http://plan.qyer.com/search_0_0_186_0_0_0_1/?cityid=6606">法国</a></li>
                    <li><a data-id="189" data-key="意大利" href="http://plan.qyer.com/search_0_0_189_0_0_0_1/?cityid=6606">意大利</a></li>
                    <li><a data-id="15" data-key="德国" href="http://plan.qyer.com/search_0_0_15_0_0_0_1/?cityid=6606">德国</a></li>
                    <li><a data-id="182" data-key="西班牙" href="http://plan.qyer.com/search_0_0_182_0_0_0_1/?cityid=6606">西班牙</a></li>
                    <li><a data-id="13" data-key="英国" href="http://plan.qyer.com/search_0_0_13_0_0_0_1/?cityid=6606">英国</a></li>
                    <li><a data-id="524" data-key="瑞士" href="http://plan.qyer.com/search_0_0_524_0_0_0_1/?cityid=6606">瑞士</a></li>
                    <li><a data-id="198" data-key="奥地利" href="http://plan.qyer.com/search_0_0_198_0_0_0_1/?cityid=6606">奥地利</a></li>
                    <li><a data-id="200" data-key="荷兰" href="http://plan.qyer.com/search_0_0_200_0_0_0_1/?cityid=6606">荷兰</a></li>
                    <li><a data-id="804" data-key="梵蒂冈" href="http://plan.qyer.com/search_0_0_804_0_0_0_1/?cityid=6606">梵蒂冈</a></li>
                    <li><a data-id="193" data-key="捷克" href="http://plan.qyer.com/search_0_0_193_0_0_0_1/?cityid=6606">捷克</a></li>
                    <li><a data-id="424" data-key="比利时" href="http://plan.qyer.com/search_0_0_424_0_0_0_1/?cityid=6606">比利时</a></li>
                    <li><a data-id="195" data-key="土耳其" href="http://plan.qyer.com/search_0_0_195_0_0_0_1/?cityid=6606">土耳其</a></li>
                    <li><a data-id="206" data-key="希腊" href="http://plan.qyer.com/search_0_0_206_0_0_0_1/?cityid=6606">希腊</a></li>
                    <li><a data-id="208" data-key="俄罗斯" href="http://plan.qyer.com/search_0_0_208_0_0_0_1/?cityid=6606">俄罗斯</a></li>
                    <li><a data-id="207" data-key="匈牙利" href="http://plan.qyer.com/search_0_0_207_0_0_0_1/?cityid=6606">匈牙利</a></li>
                    <li><a data-id="202" data-key="瑞典" href="http://plan.qyer.com/search_0_0_202_0_0_0_1/?cityid=6606">瑞典</a></li>
                    <li><a data-id="205" data-key="丹麦" href="http://plan.qyer.com/search_0_0_205_0_0_0_1/?cityid=6606">丹麦</a></li>
                    <li><a data-id="523" data-key="葡萄牙" href="http://plan.qyer.com/search_0_0_523_0_0_0_1/?cityid=6606">葡萄牙</a></li>
                    <li><a data-id="654" data-key="摩纳哥" href="http://plan.qyer.com/search_0_0_654_0_0_0_1/?cityid=6606">摩纳哥</a></li>
                    <li><a data-id="521" data-key="挪威" href="http://plan.qyer.com/search_0_0_521_0_0_0_1/?cityid=6606">挪威</a></li>
                    <li><a data-id="448" data-key="芬兰" href="http://plan.qyer.com/search_0_0_448_0_0_0_1/?cityid=6606">芬兰</a></li>
                    <li><a data-id="493" data-key="卢森堡" href="http://plan.qyer.com/search_0_0_493_0_0_0_1/?cityid=6606">卢森堡</a></li>
                    <li><a data-id="425" data-key="冰岛" href="http://plan.qyer.com/search_0_0_425_0_0_0_1/?cityid=6606">冰岛</a></li>
                    <li><a data-id="427" data-key="波兰" href="http://plan.qyer.com/search_0_0_427_0_0_0_1/?cityid=6606">波兰</a></li>
                    <li><a data-id="762" data-key="列支敦士登" href="http://plan.qyer.com/search_0_0_762_0_0_0_1/?cityid=6606">列支敦士登</a></li>
                    <li><a data-id="538" data-key="斯洛伐克" href="http://plan.qyer.com/search_0_0_538_0_0_0_1/?cityid=6606">斯洛伐克</a></li>
                    <li><a data-id="406" data-key="爱尔兰" href="http://plan.qyer.com/search_0_0_406_0_0_0_1/?cityid=6606">爱尔兰</a></li>
                    <li><a data-id="407" data-key="爱沙尼亚" href="http://plan.qyer.com/search_0_0_407_0_0_0_1/?cityid=6606">爱沙尼亚</a></li>
                    <li><a data-id="482" data-key="克罗地亚" href="http://plan.qyer.com/search_0_0_482_0_0_0_1/?cityid=6606">克罗地亚</a></li>
                    <li><a data-id="498" data-key="马耳他" href="http://plan.qyer.com/search_0_0_498_0_0_0_1/?cityid=6606">马耳他</a></li>
                    <li><a data-id="785" data-key="圣马力诺" href="http://plan.qyer.com/search_0_0_785_0_0_0_1/?cityid=6606">圣马力诺</a></li>
                    <li><a data-id="539" data-key="斯洛文尼亚" href="http://plan.qyer.com/search_0_0_539_0_0_0_1/?cityid=6606">斯洛文尼亚</a></li>
                    <li><a data-id="485" data-key="拉脱维亚" href="http://plan.qyer.com/search_0_0_485_0_0_0_1/?cityid=6606">拉脱维亚</a></li>
                    <li><a data-id="489" data-key="立陶宛" href="http://plan.qyer.com/search_0_0_489_0_0_0_1/?cityid=6606">立陶宛</a></li>
                    <li><a data-id="408" data-key="安道尔" href="http://plan.qyer.com/search_0_0_408_0_0_0_1/?cityid=6606">安道尔</a></li>
                    <li><a data-id="495" data-key="罗马尼亚" href="http://plan.qyer.com/search_0_0_495_0_0_0_1/?cityid=6606">罗马尼亚</a></li>
                    <li><a data-id="527" data-key="塞尔维亚" href="http://plan.qyer.com/search_0_0_527_0_0_0_1/?cityid=6606">塞尔维亚</a></li>
                    <li><a data-id="464" data-key="黑山" href="http://plan.qyer.com/search_0_0_464_0_0_0_1/?cityid=6606">黑山</a></li>
                    <li><a data-id="560" data-key="乌克兰" href="http://plan.qyer.com/search_0_0_560_0_0_0_1/?cityid=6606">乌克兰</a></li>
                    <li><a data-id="421" data-key="保加利亚" href="http://plan.qyer.com/search_0_0_421_0_0_0_1/?cityid=6606">保加利亚</a></li>
                    <li><a data-id="457" data-key="格鲁吉亚" href="http://plan.qyer.com/search_0_0_457_0_0_0_1/?cityid=6606">格鲁吉亚</a></li>
                    <li><a data-id="428" data-key="波黑" href="http://plan.qyer.com/search_0_0_428_0_0_0_1/?cityid=6606">波黑</a></li>
                    <li><a data-id="566" data-key="亚美尼亚" href="http://plan.qyer.com/search_0_0_566_0_0_0_1/?cityid=6606">亚美尼亚</a></li>
                    <li><a data-id="805" data-key="直布罗陀" href="http://plan.qyer.com/search_0_0_805_0_0_0_1/?cityid=6606">直布罗陀</a></li>
                    <li><a data-id="404" data-key="阿塞拜疆" href="http://plan.qyer.com/search_0_0_404_0_0_0_1/?cityid=6606">阿塞拜疆</a></li>
                    <li><a data-id="530" data-key="塞浦路斯" href="http://plan.qyer.com/search_0_0_530_0_0_0_1/?cityid=6606">塞浦路斯</a></li>
                    <li><a data-id="418" data-key="白俄罗斯" href="http://plan.qyer.com/search_0_0_418_0_0_0_1/?cityid=6606">白俄罗斯</a></li>
                    <li><a data-id="399" data-key="阿尔巴尼亚" href="http://plan.qyer.com/search_0_0_399_0_0_0_1/?cityid=6606">阿尔巴尼亚</a></li>
                    <li><a data-id="501" data-key="马其顿" href="http://plan.qyer.com/search_0_0_501_0_0_0_1/?cityid=6606">马其顿</a></li>
                    <li><a data-id="479" data-key="科索沃" href="http://plan.qyer.com/search_0_0_479_0_0_0_1/?cityid=6606">科索沃</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="244" data-key="埃及" href="http://plan.qyer.com/search_0_0_244_0_0_0_1/?cityid=6606">埃及</a></li>
                    <li><a data-id="517" data-key="南非" href="http://plan.qyer.com/search_0_0_517_0_0_0_1/?cityid=6606">南非</a></li>
                    <li><a data-id="513" data-key="摩洛哥" href="http://plan.qyer.com/search_0_0_513_0_0_0_1/?cityid=6606">摩洛哥</a></li>
                    <li><a data-id="483" data-key="肯尼亚" href="http://plan.qyer.com/search_0_0_483_0_0_0_1/?cityid=6606">肯尼亚</a></li>
                    <li><a data-id="503" data-key="毛里求斯" href="http://plan.qyer.com/search_0_0_503_0_0_0_1/?cityid=6606">毛里求斯</a></li>
                    <li><a data-id="546" data-key="坦桑尼亚" href="http://plan.qyer.com/search_0_0_546_0_0_0_1/?cityid=6606">坦桑尼亚</a></li>
                    <li><a data-id="405" data-key="埃塞俄比亚" href="http://plan.qyer.com/search_0_0_405_0_0_0_1/?cityid=6606">埃塞俄比亚</a></li>
                    <li><a data-id="531" data-key="塞舌尔" href="http://plan.qyer.com/search_0_0_531_0_0_0_1/?cityid=6606">塞舌尔</a></li>
                    <li><a data-id="550" data-key="突尼斯" href="http://plan.qyer.com/search_0_0_550_0_0_0_1/?cityid=6606">突尼斯</a></li>
                    <li><a data-id="400" data-key="阿尔及利亚" href="http://plan.qyer.com/search_0_0_400_0_0_0_1/?cityid=6606">阿尔及利亚</a></li>
                    <li><a data-id="573" data-key="赞比亚" href="http://plan.qyer.com/search_0_0_573_0_0_0_1/?cityid=6606">赞比亚</a></li>
                    <li><a data-id="474" data-key="津巴布韦" href="http://plan.qyer.com/search_0_0_474_0_0_0_1/?cityid=6606">津巴布韦</a></li>
                    <li><a data-id="559" data-key="乌干达" href="http://plan.qyer.com/search_0_0_559_0_0_0_1/?cityid=6606">乌干达</a></li>
                    <li><a data-id="516" data-key="纳米比亚" href="http://plan.qyer.com/search_0_0_516_0_0_0_1/?cityid=6606">纳米比亚</a></li>
                    <li><a data-id="520" data-key="尼日利亚" href="http://plan.qyer.com/search_0_0_520_0_0_0_1/?cityid=6606">尼日利亚</a></li>
                    <li><a data-id="496" data-key="马达加斯加" href="http://plan.qyer.com/search_0_0_496_0_0_0_1/?cityid=6606">马达加斯加</a></li>
                    <li><a data-id="471" data-key="加纳" href="http://plan.qyer.com/search_0_0_471_0_0_0_1/?cityid=6606">加纳</a></li>
                    <li><a data-id="541" data-key="苏丹" href="http://plan.qyer.com/search_0_0_541_0_0_0_1/?cityid=6606">苏丹</a></li>
                    <li><a data-id="486" data-key="莱索托" href="http://plan.qyer.com/search_0_0_486_0_0_0_1/?cityid=6606">莱索托</a></li>
                    <li><a data-id="409" data-key="安哥拉" href="http://plan.qyer.com/search_0_0_409_0_0_0_1/?cityid=6606">安哥拉</a></li>
                    <li><a data-id="514" data-key="莫桑比克" href="http://plan.qyer.com/search_0_0_514_0_0_0_1/?cityid=6606">莫桑比克</a></li>
                    <li><a data-id="492" data-key="留尼汪" href="http://plan.qyer.com/search_0_0_492_0_0_0_1/?cityid=6606">留尼汪</a></li>
                    <li><a data-id="494" data-key="卢旺达" href="http://plan.qyer.com/search_0_0_494_0_0_0_1/?cityid=6606">卢旺达</a></li>
                    <li><a data-id="576" data-key="中非共和国" href="http://plan.qyer.com/search_0_0_576_0_0_0_1/?cityid=6606">中非共和国</a></li>
                    <li><a data-id="452" data-key="刚果民主共和国" href="http://plan.qyer.com/search_0_0_452_0_0_0_1/?cityid=6606">刚果民主共和国</a></li>
                    <li><a data-id="475" data-key="喀麦隆" href="http://plan.qyer.com/search_0_0_475_0_0_0_1/?cityid=6606">喀麦隆</a></li>
                    <li><a data-id="431" data-key="博茨瓦纳" href="http://plan.qyer.com/search_0_0_431_0_0_0_1/?cityid=6606">博茨瓦纳</a></li>
                    <li><a data-id="480" data-key="科特迪瓦" href="http://plan.qyer.com/search_0_0_480_0_0_0_1/?cityid=6606">科特迪瓦</a></li>
                    <li><a data-id="529" data-key="塞内加尔" href="http://plan.qyer.com/search_0_0_529_0_0_0_1/?cityid=6606">塞内加尔</a></li>
                    <li><a data-id="491" data-key="利比亚" href="http://plan.qyer.com/search_0_0_491_0_0_0_1/?cityid=6606">利比亚</a></li>
                    <li><a data-id="451" data-key="刚果" href="http://plan.qyer.com/search_0_0_451_0_0_0_1/?cityid=6606">刚果</a></li>
                    <li><a data-id="499" data-key="马拉维" href="http://plan.qyer.com/search_0_0_499_0_0_0_1/?cityid=6606">马拉维</a></li>
                    <li><a data-id="439" data-key="多哥" href="http://plan.qyer.com/search_0_0_439_0_0_0_1/?cityid=6606">多哥</a></li>
                    <li><a data-id="467" data-key="吉布提" href="http://plan.qyer.com/search_0_0_467_0_0_0_1/?cityid=6606">吉布提</a></li>
                    <li><a data-id="423" data-key="贝宁" href="http://plan.qyer.com/search_0_0_423_0_0_0_1/?cityid=6606">贝宁</a></li>
                    <li><a data-id="473" data-key="加蓬" href="http://plan.qyer.com/search_0_0_473_0_0_0_1/?cityid=6606">加蓬</a></li>
                    <li><a data-id="500" data-key="马里" href="http://plan.qyer.com/search_0_0_500_0_0_0_1/?cityid=6606">马里</a></li>
                    <li><a data-id="1062" data-key="西撒哈拉" href="http://plan.qyer.com/search_0_0_1062_0_0_0_1/?cityid=6606">西撒哈拉</a></li>
                    <li><a data-id="504" data-key="毛里塔尼亚" href="http://plan.qyer.com/search_0_0_504_0_0_0_1/?cityid=6606">毛里塔尼亚</a></li>
                    <li><a data-id="437" data-key="赤道几内亚" href="http://plan.qyer.com/search_0_0_437_0_0_0_1/?cityid=6606">赤道几内亚</a></li>
                    <li><a data-id="540" data-key="斯威士兰" href="http://plan.qyer.com/search_0_0_540_0_0_0_1/?cityid=6606">斯威士兰</a></li>
                    <li><a data-id="435" data-key="布隆迪" href="http://plan.qyer.com/search_0_0_435_0_0_0_1/?cityid=6606">布隆迪</a></li>
                    <li><a data-id="469" data-key="几内亚" href="http://plan.qyer.com/search_0_0_469_0_0_0_1/?cityid=6606">几内亚</a></li>
                    <li><a data-id="574" data-key="乍得" href="http://plan.qyer.com/search_0_0_574_0_0_0_1/?cityid=6606">乍得</a></li>
                    <li><a data-id="853" data-key="南苏丹" href="http://plan.qyer.com/search_0_0_853_0_0_0_1/?cityid=6606">南苏丹</a></li>
                    <li><a data-id="519" data-key="尼日尔" href="http://plan.qyer.com/search_0_0_519_0_0_0_1/?cityid=6606">尼日尔</a></li>
                    <li><a data-id="1061" data-key="佛得角" href="http://plan.qyer.com/search_0_0_1061_0_0_0_1/?cityid=6606">佛得角</a></li>
                    <li><a data-id="490" data-key="利比里亚" href="http://plan.qyer.com/search_0_0_490_0_0_0_1/?cityid=6606">利比里亚</a></li>
                    <li><a data-id="420" data-key="索马里" href="http://plan.qyer.com/search_0_0_420_0_0_0_1/?cityid=6606">索马里</a></li>
                    <li><a data-id="434" data-key="布基纳法索" href="http://plan.qyer.com/search_0_0_434_0_0_0_1/?cityid=6606">布基纳法索</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="236" data-key="美国" href="http://plan.qyer.com/search_0_0_236_0_0_0_1/?cityid=6606">美国</a></li>
                    <li><a data-id="238" data-key="加拿大" href="http://plan.qyer.com/search_0_0_238_0_0_0_1/?cityid=6606">加拿大</a></li>
                    <li><a data-id="515" data-key="墨西哥" href="http://plan.qyer.com/search_0_0_515_0_0_0_1/?cityid=6606">墨西哥</a></li>
                    <li><a data-id="458" data-key="古巴" href="http://plan.qyer.com/search_0_0_458_0_0_0_1/?cityid=6606">古巴</a></li>
                    <li><a data-id="413" data-key="巴哈马" href="http://plan.qyer.com/search_0_0_413_0_0_0_1/?cityid=6606">巴哈马</a></li>
                    <li><a data-id="426" data-key="波多黎各" href="http://plan.qyer.com/search_0_0_426_0_0_0_1/?cityid=6606">波多黎各</a></li>
                    <li><a data-id="417" data-key="巴拿马" href="http://plan.qyer.com/search_0_0_417_0_0_0_1/?cityid=6606">巴拿马</a></li>
                    <li><a data-id="454" data-key="哥斯达黎加" href="http://plan.qyer.com/search_0_0_454_0_0_0_1/?cityid=6606">哥斯达黎加</a></li>
                    <li><a data-id="565" data-key="牙买加" href="http://plan.qyer.com/search_0_0_565_0_0_0_1/?cityid=6606">牙买加</a></li>
                    <li><a data-id="506" data-key="美属维尔京群岛" href="http://plan.qyer.com/search_0_0_506_0_0_0_1/?cityid=6606">美属维尔京群岛</a></li>
                    <li><a data-id="555" data-key="危地马拉" href="http://plan.qyer.com/search_0_0_555_0_0_0_1/?cityid=6606">危地马拉</a></li>
                    <li><a data-id="477" data-key="开曼群岛" href="http://plan.qyer.com/search_0_0_477_0_0_0_1/?cityid=6606">开曼群岛</a></li>
                    <li><a data-id="430" data-key="伯利兹" href="http://plan.qyer.com/search_0_0_430_0_0_0_1/?cityid=6606">伯利兹</a></li>
                    <li><a data-id="440" data-key="多米尼加共和国" href="http://plan.qyer.com/search_0_0_440_0_0_0_1/?cityid=6606">多米尼加共和国</a></li>
                    <li><a data-id="465" data-key="洪都拉斯" href="http://plan.qyer.com/search_0_0_465_0_0_0_1/?cityid=6606">洪都拉斯</a></li>
                    <li><a data-id="462" data-key="海地" href="http://plan.qyer.com/search_0_0_462_0_0_0_1/?cityid=6606">海地</a></li>
                    <li><a data-id="1382" data-key="荷属圣马丁" href="http://plan.qyer.com/search_0_0_1382_0_0_0_1/?cityid=6606">荷属圣马丁</a></li>
                    <li><a data-id="1383" data-key="法属圣马丁" href="http://plan.qyer.com/search_0_0_1383_0_0_0_1/?cityid=6606">法属圣马丁</a></li>
                    <li><a data-id="419" data-key="百慕大" href="http://plan.qyer.com/search_0_0_419_0_0_0_1/?cityid=6606">百慕大</a></li>
                    <li><a data-id="411" data-key="巴巴多斯" href="http://plan.qyer.com/search_0_0_411_0_0_0_1/?cityid=6606">巴巴多斯</a></li>
                    <li><a data-id="525" data-key="萨尔瓦多" href="http://plan.qyer.com/search_0_0_525_0_0_0_1/?cityid=6606">萨尔瓦多</a></li>
                    <li><a data-id="548" data-key="特克斯和凯科斯群岛" href="http://plan.qyer.com/search_0_0_548_0_0_0_1/?cityid=6606">特克斯和凯科斯群岛</a></li>
                    <li><a data-id="535" data-key="圣卢西亚" href="http://plan.qyer.com/search_0_0_535_0_0_0_1/?cityid=6606">圣卢西亚</a></li>
                    <li><a data-id="549" data-key="特立尼达和多巴哥" href="http://plan.qyer.com/search_0_0_549_0_0_0_1/?cityid=6606">特立尼达和多巴哥</a></li>
                    <li><a data-id="518" data-key="尼加拉瓜" href="http://plan.qyer.com/search_0_0_518_0_0_0_1/?cityid=6606">尼加拉瓜</a></li>
                    <li><a data-id="410" data-key="安提瓜和巴布达" href="http://plan.qyer.com/search_0_0_410_0_0_0_1/?cityid=6606">安提瓜和巴布达</a></li>
                    <li><a data-id="534" data-key="圣基茨和尼维斯" href="http://plan.qyer.com/search_0_0_534_0_0_0_1/?cityid=6606">圣基茨和尼维斯</a></li>
                    <li><a data-id="432" data-key="阿鲁巴" href="http://plan.qyer.com/search_0_0_432_0_0_0_1/?cityid=6606">阿鲁巴</a></li>
                    <li><a data-id="571" data-key="英属维尔京群岛" href="http://plan.qyer.com/search_0_0_571_0_0_0_1/?cityid=6606">英属维尔京群岛</a></li>
                    <li><a data-id="441" data-key="多米尼克" href="http://plan.qyer.com/search_0_0_441_0_0_0_1/?cityid=6606">多米尼克</a></li>
                    <li><a data-id="455" data-key="格林纳达" href="http://plan.qyer.com/search_0_0_455_0_0_0_1/?cityid=6606">格林纳达</a></li>
                    <li><a data-id="1419" data-key="库拉索" href="http://plan.qyer.com/search_0_0_1419_0_0_0_1/?cityid=6606">库拉索</a></li>
                    <li><a data-id="1380" data-key="马提尼克" href="http://plan.qyer.com/search_0_0_1380_0_0_0_1/?cityid=6606">马提尼克</a></li>
                    <li><a data-id="1295" data-key="瓜德罗普" href="http://plan.qyer.com/search_0_0_1295_0_0_0_1/?cityid=6606">瓜德罗普</a></li>
                    <li><a data-id="1416" data-key="安圭拉" href="http://plan.qyer.com/search_0_0_1416_0_0_0_1/?cityid=6606">安圭拉</a></li>
                    <li><a data-id="1432" data-key="波内赫" href="http://plan.qyer.com/search_0_0_1432_0_0_0_1/?cityid=6606">波内赫</a></li>
                    <li><a data-id="536" data-key="圣文森特和格林纳丁斯" href="http://plan.qyer.com/search_0_0_536_0_0_0_1/?cityid=6606">圣文森特和格林纳丁斯</a></li>
                    <li><a data-id="1417" data-key="圣巴泰勒米岛" href="http://plan.qyer.com/search_0_0_1417_0_0_0_1/?cityid=6606">圣巴泰勒米岛</a></li>
                    <li><a data-id="1418" data-key="蒙塞拉特岛" href="http://plan.qyer.com/search_0_0_1418_0_0_0_1/?cityid=6606">蒙塞拉特岛</a></li>
                    <li><a data-id="1421" data-key="萨巴岛" href="http://plan.qyer.com/search_0_0_1421_0_0_0_1/?cityid=6606">萨巴岛</a></li>
                    <li><a data-id="1420" data-key="圣尤斯特歇斯" href="http://plan.qyer.com/search_0_0_1420_0_0_0_1/?cityid=6606">圣尤斯特歇斯</a></li>
                    <li><a data-id="1381" data-key="圣皮埃尔和密克隆群岛" href="http://plan.qyer.com/search_0_0_1381_0_0_0_1/?cityid=6606">圣皮埃尔和密克隆群岛</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="242" data-key="巴西" href="http://plan.qyer.com/search_0_0_242_0_0_0_1/?cityid=6606">巴西</a></li>
                    <li><a data-id="509" data-key="秘鲁" href="http://plan.qyer.com/search_0_0_509_0_0_0_1/?cityid=6606">秘鲁</a></li>
                    <li><a data-id="243" data-key="阿根廷" href="http://plan.qyer.com/search_0_0_243_0_0_0_1/?cityid=6606">阿根廷</a></li>
                    <li><a data-id="575" data-key="智利" href="http://plan.qyer.com/search_0_0_575_0_0_0_1/?cityid=6606">智利</a></li>
                    <li><a data-id="429" data-key="玻利维亚" href="http://plan.qyer.com/search_0_0_429_0_0_0_1/?cityid=6606">玻利维亚</a></li>
                    <li><a data-id="453" data-key="哥伦比亚" href="http://plan.qyer.com/search_0_0_453_0_0_0_1/?cityid=6606">哥伦比亚</a></li>
                    <li><a data-id="443" data-key="厄瓜多尔" href="http://plan.qyer.com/search_0_0_443_0_0_0_1/?cityid=6606">厄瓜多尔</a></li>
                    <li><a data-id="557" data-key="委内瑞拉" href="http://plan.qyer.com/search_0_0_557_0_0_0_1/?cityid=6606">委内瑞拉</a></li>
                    <li><a data-id="561" data-key="乌拉圭" href="http://plan.qyer.com/search_0_0_561_0_0_0_1/?cityid=6606">乌拉圭</a></li>
                    <li><a data-id="415" data-key="巴拉圭" href="http://plan.qyer.com/search_0_0_415_0_0_0_1/?cityid=6606">巴拉圭</a></li>
                    <li><a data-id="1293" data-key="苏里南" href="http://plan.qyer.com/search_0_0_1293_0_0_0_1/?cityid=6606">苏里南</a></li>
                    <li><a data-id="449" data-key="福克兰群岛（马尔维纳斯群岛）" href="http://plan.qyer.com/search_0_0_449_0_0_0_1/?cityid=6606">福克兰群岛（马尔维纳斯群岛）</a></li>
                    <li><a data-id="460" data-key="圭亚那" href="http://plan.qyer.com/search_0_0_460_0_0_0_1/?cityid=6606">圭亚那</a></li>
                    <li><a data-id="1292" data-key="法属圭亚那" href="http://plan.qyer.com/search_0_0_1292_0_0_0_1/?cityid=6606">法属圭亚那</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="240" data-key="澳大利亚" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606">澳大利亚</a></li>
                    <li><a data-id="241" data-key="新西兰" href="http://plan.qyer.com/search_0_0_241_0_0_0_1/?cityid=6606">新西兰</a></li>
                    <li><a data-id="422" data-key="北马里亚纳群岛" href="http://plan.qyer.com/search_0_0_422_0_0_0_1/?cityid=6606">北马里亚纳群岛</a></li>
                    <li><a data-id="447" data-key="斐济" href="http://plan.qyer.com/search_0_0_447_0_0_0_1/?cityid=6606">斐济</a></li>
                    <li><a data-id="522" data-key="帕劳" href="http://plan.qyer.com/search_0_0_522_0_0_0_1/?cityid=6606">帕劳</a></li>
                    <li><a data-id="1072" data-key="关岛" href="http://plan.qyer.com/search_0_0_1072_0_0_0_1/?cityid=6606">关岛</a></li>
                    <li><a data-id="545" data-key="法属波利尼西亚" href="http://plan.qyer.com/search_0_0_545_0_0_0_1/?cityid=6606">法属波利尼西亚</a></li>
                    <li><a data-id="554" data-key="瓦努阿图" href="http://plan.qyer.com/search_0_0_554_0_0_0_1/?cityid=6606">瓦努阿图</a></li>
                    <li><a data-id="806" data-key="艾普罗菲尔" href="http://plan.qyer.com/search_0_0_806_0_0_0_1/?cityid=6606">艾普罗菲尔</a></li>
                    <li><a data-id="484" data-key="库克群岛" href="http://plan.qyer.com/search_0_0_484_0_0_0_1/?cityid=6606">库克群岛</a></li>
                    <li><a data-id="563" data-key="新喀里多尼亚" href="http://plan.qyer.com/search_0_0_563_0_0_0_1/?cityid=6606">新喀里多尼亚</a></li>
                    <li><a data-id="412" data-key="巴布亚新几内亚" href="http://plan.qyer.com/search_0_0_412_0_0_0_1/?cityid=6606">巴布亚新几内亚</a></li>
                    <li><a data-id="547" data-key="汤加" href="http://plan.qyer.com/search_0_0_547_0_0_0_1/?cityid=6606">汤加</a></li>
                    <li><a data-id="526" data-key="萨摩亚" href="http://plan.qyer.com/search_0_0_526_0_0_0_1/?cityid=6606">萨摩亚</a></li>
                    <li><a data-id="543" data-key="所罗门群岛" href="http://plan.qyer.com/search_0_0_543_0_0_0_1/?cityid=6606">所罗门群岛</a></li>
                    <li><a data-id="510" data-key="密克罗尼西亚联邦" href="http://plan.qyer.com/search_0_0_510_0_0_0_1/?cityid=6606">密克罗尼西亚联邦</a></li>
                    <li><a data-id="502" data-key="马绍尔群岛" href="http://plan.qyer.com/search_0_0_502_0_0_0_1/?cityid=6606">马绍尔群岛</a></li>
                    <li><a data-id="505" data-key="美属萨摩亚" href="http://plan.qyer.com/search_0_0_505_0_0_0_1/?cityid=6606">美属萨摩亚</a></li>
                    <li><a data-id="1064" data-key="纽埃" href="http://plan.qyer.com/search_0_0_1064_0_0_0_1/?cityid=6606">纽埃</a></li>
                    <li><a data-id="551" data-key="图瓦卢" href="http://plan.qyer.com/search_0_0_551_0_0_0_1/?cityid=6606">图瓦卢</a></li>
                    <li><a data-id="466" data-key="基里巴斯" href="http://plan.qyer.com/search_0_0_466_0_0_0_1/?cityid=6606">基里巴斯</a></li>
                    <li><a data-id="1027" data-key="瑙鲁" href="http://plan.qyer.com/search_0_0_1027_0_0_0_1/?cityid=6606">瑙鲁</a></li>
                    <li><a data-id="553" data-key="瓦利斯群岛和富图纳群岛" href="http://plan.qyer.com/search_0_0_553_0_0_0_1/?cityid=6606">瓦利斯群岛和富图纳群岛</a></li>
                    <li><a data-id="1428" data-key="皮特凯恩群岛" href="http://plan.qyer.com/search_0_0_1428_0_0_0_1/?cityid=6606">皮特凯恩群岛</a></li>
                    <li><a data-id="1063" data-key="托克劳" href="http://plan.qyer.com/search_0_0_1063_0_0_0_1/?cityid=6606">托克劳</a></li>
                        </ul>
                      <ul class="clearfix" style="display:none;">
                    <li><a data-id="760" data-key="南极" href="http://plan.qyer.com/search_0_0_760_0_0_0_1/?cityid=6606">南极</a></li>
                    <li><a data-id="1762" data-key="南乔治亚岛和南桑威奇群岛" href="http://plan.qyer.com/search_0_0_1762_0_0_0_1/?cityid=6606">南乔治亚岛和南桑威奇群岛</a></li>
                    <li><a data-id="1446" data-key="太空" href="http://plan.qyer.com/search_0_0_1446_0_0_0_1/?cityid=6606">太空</a></li>
                    <li><a data-id="1431" data-key="法属南部领土" href="http://plan.qyer.com/search_0_0_1431_0_0_0_1/?cityid=6606">法属南部领土</a></li>
                    <li><a data-id="1430" data-key="布韦岛" href="http://plan.qyer.com/search_0_0_1430_0_0_0_1/?cityid=6606">布韦岛</a></li>
                        </ul>
              </div>
    </div>

      <div  id="js_cityList" class="items clearfix" style="display:none;">
          <strong class="title">
              前往城市:
          </strong>
          <div class="list clearfix">
          </div>

          <div class="selectdiv clearfix" style="display:none;" >
          </div>

          <div class="subbtn" style="display:none;">
              <input type="button" class="ui_button js_cmd" id="selectCitysOKBtn" data-cmd="goPage" data-type="accept" value="确定" data-bn-ipg="planhome-select-city-confirm">
              <input type="button" class="ui_button_cancel js_cmd" data-cmd="city_select_close" data-type="cancel" value="取消" data-bn-ipg="planhome-select-city-cancel"> 
          </div>


          <div class="seting destination">
              <a href="javascript:;" class="moreBtn setMore js_cmd" data-cmd="city_more" data-status="close" data-bn-ipg="planhome-select-city-more">
                  更多
              </a>
              <a href="javascript:;" class="setSelect js_cmd" data-cmd="city_select" data-bn-ipg="planhome-select-city-multipleselect">
                  多选
              </a>
          </div>
      </div>
    
        <div class="items clearfix times">
      <strong class="title">
        出行时间:
      </strong>
      <div id="js_startTime" class="list clearfix">
                <a data-bn-ipg="planhome-select-month1" data-id="1" data-key="1" href="http://plan.qyer.com/search_1_0_240_0_0_0_1/?cityid=6606">一月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="2" data-key="2" href="http://plan.qyer.com/search_2_0_240_0_0_0_1/?cityid=6606">二月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="3" data-key="3" href="http://plan.qyer.com/search_3_0_240_0_0_0_1/?cityid=6606">三月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="4" data-key="4" href="http://plan.qyer.com/search_4_0_240_0_0_0_1/?cityid=6606">四月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="5" data-key="5" href="http://plan.qyer.com/search_5_0_240_0_0_0_1/?cityid=6606">五月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="6" data-key="6" href="http://plan.qyer.com/search_6_0_240_0_0_0_1/?cityid=6606">六月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="7" data-key="7" href="http://plan.qyer.com/search_7_0_240_0_0_0_1/?cityid=6606">七月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="8" data-key="8" href="http://plan.qyer.com/search_8_0_240_0_0_0_1/?cityid=6606">八月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="9" data-key="9" href="http://plan.qyer.com/search_9_0_240_0_0_0_1/?cityid=6606">九月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="10" data-key="10" href="http://plan.qyer.com/search_10_0_240_0_0_0_1/?cityid=6606">十月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="11" data-key="11" href="http://plan.qyer.com/search_11_0_240_0_0_0_1/?cityid=6606">十一月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="12" data-key="12" href="http://plan.qyer.com/search_12_0_240_0_0_0_1/?cityid=6606">十二月</a>
                <a data-bn-ipg="planhome-select-month1" data-id="13" data-key="13" href="http://plan.qyer.com/search_13_0_240_0_0_0_1/?cityid=6606">新年</a>
                <a data-bn-ipg="planhome-select-month1" data-id="14" data-key="14" href="http://plan.qyer.com/search_14_0_240_0_0_0_1/?cityid=6606">春节</a>
                <a data-bn-ipg="planhome-select-month1" data-id="15" data-key="15" href="http://plan.qyer.com/search_15_0_240_0_0_0_1/?cityid=6606">清明</a>
                <a data-bn-ipg="planhome-select-month1" data-id="16" data-key="16" href="http://plan.qyer.com/search_16_0_240_0_0_0_1/?cityid=6606">劳动节</a>
                <a data-bn-ipg="planhome-select-month1" data-id="17" data-key="17" href="http://plan.qyer.com/search_17_0_240_0_0_0_1/?cityid=6606">端午</a>
                <a data-bn-ipg="planhome-select-month1" data-id="18" data-key="18" href="http://plan.qyer.com/search_18_0_240_0_0_0_1/?cityid=6606">中秋</a>
                <a data-bn-ipg="planhome-select-month1" data-id="19" data-key="19" href="http://plan.qyer.com/search_19_0_240_0_0_0_1/?cityid=6606">国庆</a>
              </div>
      <div class="seting">
        <a href="javascript:;" class="moreBtn setMore js_cmd" data-cmd="time_more" data-status="close" data-bn-ipg="planhome-select-city-more">
          更多
        </a>
      </div>
    </div>
            <div class="items clearfix">
      <strong class="title">
        出行天数:
      </strong>
      <div class="list clearfix">
                <a data-bn-ipg="planhome-select-days1" data-id="1001" data-key="1001" href="http://plan.qyer.com/search_0_0_240_0_1001_0_1/?cityid=6606">3天及以下</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1002" data-key="1002" href="http://plan.qyer.com/search_0_0_240_0_1002_0_1/?cityid=6606">4天至7天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1003" data-key="1003" href="http://plan.qyer.com/search_0_0_240_0_1003_0_1/?cityid=6606">8天至14天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1004" data-key="1004" href="http://plan.qyer.com/search_0_0_240_0_1004_0_1/?cityid=6606">14天至20天</a>
                <a data-bn-ipg="planhome-select-days1" data-id="1005" data-key="1005" href="http://plan.qyer.com/search_0_0_240_0_1005_0_1/?cityid=6606">20天以上</a>
              </div>
      <div class="seting">
      </div>
    </div>
    
        <div class="items clearfix">
      <strong class="title">
        出发城市:
      </strong>
          <div id="js_placeList" class="list clearfix">
                      <a data-bn-ipg="planhome-select-country1" data-id="11593" data-key="北京" href="http://plan.qyer.com/search_0_11593_240_0_0_0_1/?cityid=6606">北京</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11595" data-key="上海" href="http://plan.qyer.com/search_0_11595_240_0_0_0_1/?cityid=6606">上海</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11808" data-key="广州" href="http://plan.qyer.com/search_0_11808_240_0_0_0_1/?cityid=6606">广州</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="12189" data-key="深圳" href="http://plan.qyer.com/search_0_12189_240_0_0_0_1/?cityid=6606">深圳</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11596" data-key="重庆" href="http://plan.qyer.com/search_0_11596_240_0_0_0_1/?cityid=6606">重庆</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11800" data-key="成都" href="http://plan.qyer.com/search_0_11800_240_0_0_0_1/?cityid=6606">成都</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="11690" data-key="杭州" href="http://plan.qyer.com/search_0_11690_240_0_0_0_1/?cityid=6606">杭州</a>
                      <a data-bn-ipg="planhome-select-country1" data-id="50" data-key="香港" href="http://plan.qyer.com/search_0_50_240_0_0_0_1/?cityid=6606">香港</a>
              </div>
    </div>
    

        <div class="items clearfix">
      <strong class="title">
        行程主题:
      </strong>
      <div id="js_planTopic_links" class="list clearfix">
            <a data-bn-ipg="planhome-select-tag1" data-id="1" data-key="1" href="http://plan.qyer.com/search_0_0_240_0_0_1_1/?cityid=6606">美食</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="2" data-key="2" href="http://plan.qyer.com/search_0_0_240_0_0_2_1/?cityid=6606">人文</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="3" data-key="3" href="http://plan.qyer.com/search_0_0_240_0_0_3_1/?cityid=6606">购物</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="4" data-key="4" href="http://plan.qyer.com/search_0_0_240_0_0_4_1/?cityid=6606">游园观光</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="6" data-key="6" href="http://plan.qyer.com/search_0_0_240_0_0_6_1/?cityid=6606">沙滩海岛</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="7" data-key="7" href="http://plan.qyer.com/search_0_0_240_0_0_7_1/?cityid=6606">户外</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="8" data-key="8" href="http://plan.qyer.com/search_0_0_240_0_0_8_1/?cityid=6606">自然风光</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="9" data-key="9" href="http://plan.qyer.com/search_0_0_240_0_0_9_1/?cityid=6606">自驾</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="10" data-key="10" href="http://plan.qyer.com/search_0_0_240_0_0_10_1/?cityid=6606">蜜月</a>
            <a data-bn-ipg="planhome-select-tag1" data-id="11" data-key="11" href="http://plan.qyer.com/search_0_0_240_0_0_11_1/?cityid=6606">亲子</a>
            </div>

          <div id="js_planTopic_more" class="list clearfix" style="display:none;">
            <label data-key="1"><input type="checkbox">美食</label>
            <label data-key="2"><input type="checkbox">人文</label>
            <label data-key="3"><input type="checkbox">购物</label>
            <label data-key="4"><input type="checkbox">游园观光</label>
            <label data-key="6"><input type="checkbox">沙滩海岛</label>
            <label data-key="7"><input type="checkbox">户外</label>
            <label data-key="8"><input type="checkbox">自然风光</label>
            <label data-key="9"><input type="checkbox">自驾</label>
            <label data-key="10"><input type="checkbox">蜜月</label>
            <label data-key="11"><input type="checkbox">亲子</label>
                </div>

      <div id="js_planTopic_subbtn" class="subbtn" style="display: none;">
        <input type="button" class="ui_button js_cmd" id="selectPlanTopicOKBtn" data-cmd="goPage" data-type="accept" value="确定" data-bn-ipg="planhome-select-city-confirm">
        <input type="button" class="ui_button_cancel js_cmd" data-cmd="planType_close" data-type="cancel" value="取消"data-bn-ipg="planhome-select-city-cancel"> 
          </div>

      <div class="seting">
        <a id="js_moreTopic" href="javascript:;" class="setSelect js_cmd" data-cmd="planType_more" data-bn-ipg="planhome-select-city-multipleselect">
          多选
        </a>
      </div>
    </div>
            <div class="items clearfix noneborder">
      <strong class="title">
        精华等级:
      </strong>
      <div id="essence_list" class="list clearfix"></div>
      <div class="seting">
      </div>
    </div>
      </div>

  <!-- 首页行程列表 -->
  <div class="ind_lists">
    <div class="seting">
      <!-- 排序 -->
      <div class="sort fsort ">
        <a href="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&order=1" class="current">默认排序</a> |  
        <a href="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&order=4" class="">浏览次数最多</a> |  
        <a href="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606&order=3" class="">复制次数最多</a>
      </div>

      <!-- 搜索 -->
      <div class="search">
        <span>264个行程</span>
        <input type="text" id="search_plan" value="" class="ui2_input" placeholder="在当前结果下搜索" />
              </div>
    </div>

    <!-- 行程无内容 -->
    
    <!-- 行程列表 -->
    <div class="lists clearfix">
      <div class="list">
        <!-- 行程列表内容 -->
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2YJZFFmBz9TYFI7Cm4/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-1">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/plan/cover/2015/0913163700/2709442/index/325x240" title="澳大利亚北领地探秘" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>9</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2015-08-10 出发</dt>
                  <dd>澳大利亚北领地探秘</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong>
                </div>
                                <div class="plan">
                  <p>墨尔本·达尔文·卡卡杜国家公园·爱丽斯泉·乌鲁鲁-卡塔曲塔国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">464</span>　|　<span class="icon2">6</span>
                </div>
              </div>
                              <div class="stars">
                  <span class="star"></span><span></span><span></span>
                </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="2709442" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/3144582" target="_blank" class="name" data-bn-ipg="planhome-plan-username">Alex_Czech</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2cJZFFmBzBTY1I2Cms/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-2">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/473/20/RU5WQBoAZg/index/325x240" title="澳大利亚北领地" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>8</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2009-09-05 出发</dt>
                  <dd>澳大利亚北领地</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>自然风光</strong>
                </div>
                                <div class="plan">
                  <p>珀斯·乌鲁鲁-卡塔曲塔国家公园·爱丽斯泉</p>
                </div>
                <div class="number">
                  <span class="icon1">276</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="3706797" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/1125553" target="_blank" class="name" data-bn-ipg="planhome-plan-username">妮儿小盖</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2IJYlFhBzRTZlI9Cms/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-3">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/211/79/Q0hURRMFZQ/index/325x240" title="高翔David的澳大利亚北领地十日游线路" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>9</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2016-06-21 出发</dt>
                  <dd>高翔David的澳大利亚北领地十日游线路</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>达尔文·卡卡杜国家公园·凯瑟琳·滕南特克里克·爱丽斯泉·瓦塔卡国王峡谷国家公园·乌鲁鲁-卡塔曲塔国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">155</span>　|　<span class="icon2">1</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="6172227" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/7127826" target="_blank" class="name" data-bn-ipg="planhome-plan-username">高翔David</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FgBzVTYFI5CmgNOQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-4">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/861/29/SU9UQBMHZQ/index/325x240" title="澳大利亚北领地" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>11</strong>天</div>
                <dl class="fontYaHei">
                  <dt> 出发</dt>
                  <dd>澳大利亚北领地</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>长沙·达尔文·卡卡杜国家公园·凯瑟琳·爱丽斯泉·乌鲁鲁-卡塔曲塔国家公园·瓦塔卡国王峡谷国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">13</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10634647" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/1918536" target="_blank" class="name" data-bn-ipg="planhome-plan-username">leo微胖</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20JZFFmBzFTZlI4Cmw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-5">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/450/7/RUxVQh0PYg/index/325x240" title="澳大利亚东南部自驾游" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>31</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-03-28 出发</dt>
                  <dd>澳大利亚东南部自驾游</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong><strong>自驾</strong>
                </div>
                                <div class="plan">
                  <p>广州·悉尼·麦夸里港·黄金海岸·布里斯班·澳大利亚阳光海岸·班德堡·澳大利亚卡米拉·汤斯维尔·凯恩斯·Conjuboy, 昆士兰州 4816澳大利亚·Winton, 昆士兰州 4735澳大利亚·Boulia, 昆士兰州 4829澳大利亚·Anatye, 北领地 0872澳大利亚·艾利斯斯普林斯 澳大利亚北领地邮政编码: 0870·乌鲁鲁-卡塔曲塔国家公园·Marla, 南澳大利亚州 5724澳大利亚·Glendambo, 南澳大利亚州 5719澳大利亚·阿德莱德·芒特甘比尔 澳大利亚南澳大利亚州邮政编码: 5290·Princetown, 維多利亞省 3269澳大利亚·Wye River, 維多利亞省 3234澳大利亚·Torquay, 維多利亞省 3228澳大利亚·吉朗·阿尔托纳区 澳大利亚維多利亞省邮政编码: 3018·墨尔本·堪培拉</p>
                </div>
                <div class="number">
                  <span class="icon1">42</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9707270" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/3491936" target="_blank" class="name" data-bn-ipg="planhome-plan-username">哈哈达</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FgBz9TY1I2Cm0NOQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-6">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/473/20/RU5WQBoAZg/index/325x240" title="wwwyizhi的澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>12</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-01 出发</dt>
                  <dd>wwwyizhi的澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong>
                </div>
                                <div class="plan">
                  <p>北京·新加坡·墨尔本·乌鲁鲁-卡塔曲塔国家公园·麦克唐奈山脉·爱丽斯泉·达尔文·卡卡杜国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">25</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10697917" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9405457" target="_blank" class="name" data-bn-ipg="planhome-plan-username">wwwyizhi</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFmBzVTYFI-CmUNOg/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-7">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/211/79/Q0hURRMFZQ/index/325x240" title="新加坡、澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>26</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-08-04 出发</dt>
                  <dd>新加坡、澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong>
                </div>
                                <div class="plan">
                  <p>温州·上海·新加坡·达尔文·卡卡杜国家公园·凯瑟琳·Daly Waters·谭宁特溪·爱丽斯泉·瓦塔卡国王峡谷国家公园·尤拉拉·乌鲁鲁-卡塔曲塔国家公园·阿德莱德·袋鼠岛·珀斯</p>
                </div>
                <div class="number">
                  <span class="icon1">47</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11034194" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/3043397" target="_blank" class="name" data-bn-ipg="planhome-plan-username">Kelly67890</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJYlFkBzFTY1I5CmsNOA/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-8">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/1b9/7a/2003842/index/325x240" title="SM6FdEu的澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>37</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-09-10 出发</dt>
                  <dd>SM6FdEu的澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>上海·悉尼·墨尔本·黄金海岸·凯恩斯·布里斯班·大洋路·澳大利亚蓝山·阿波罗小镇·坎贝尔港国家公园·阿德莱德·艾尔利海滩·吉朗·龙恩·沃南布尔·珀斯·圣灵群岛·乌鲁鲁-卡塔曲塔国家公园·爱丽斯泉·袋鼠岛·库兰达·澳大利亚阳光海岸·弗雷泽岛·春溪国家公园·奥古斯塔港·尤拉拉·南澳大利亚州·北领地·西澳大利亚州·新南威尔士州·波奴鲁鲁国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">2</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="11277676" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9600422" target="_blank" class="name" data-bn-ipg="planhome-plan-username">SM6FdEu</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FhBzZTZFI8CmkNNw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-9">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/211/79/Q0hURRMFZQ/index/325x240" title="北领地房车自驾" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>13</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-07-27 出发</dt>
                  <dd>北领地房车自驾</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>自驾</strong>
                </div>
                                <div class="plan">
                  <p>北京·新加坡·达尔文·凯瑟琳·谭宁特溪·爱丽斯泉·瓦塔卡国王峡谷国家公园·乌鲁鲁-卡塔曲塔国家公园·卡卡杜国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">30</span>　|　<span class="icon2">2</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10700359" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9405457" target="_blank" class="name" data-bn-ipg="planhome-plan-username">wwwyizhi</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FhBzBTZVI2Cm0NOA/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-10">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/user/312/11/QkhXQxsHaA/index/325x240" title="hermmy的澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>6</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-07-28 出发</dt>
                  <dd>hermmy的澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong>
                </div>
                                <div class="plan">
                  <p>悉尼·达尔文·卡卡杜国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">39</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10761916" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/2126501" target="_blank" class="name" data-bn-ipg="planhome-plan-username">hermmy</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V2UJY1FhBzZTYVI4CmUNPQ/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-11">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/1034/10/QElWRhsHaU4/index/325x240" title="北领地全程房车" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>12</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-07-27 出发</dt>
                  <dd>北领地全程房车</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="plan">
                  <p>北京·新加坡·达尔文·卡卡杜国家公园·凯瑟琳·谭宁特溪·爱丽斯泉·瓦塔卡国王峡谷国家公园·乌鲁鲁-卡塔曲塔国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">14</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="10705793" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9405457" target="_blank" class="name" data-bn-ipg="planhome-plan-username">wwwyizhi</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20JZVFiBzZTbFI6Cmk/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-12">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/143/73/1967138/index/325x240" title="windy_411的澳大利亚十五日游线路" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>20</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-04-19 出发</dt>
                  <dd>windy_411的澳大利亚十五日游线路</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>沙滩海岛</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>上海·阿德莱德·芭萝莎·汉多夫·袋鼠岛·爱丽斯泉·乌鲁鲁-卡塔曲塔国家公园·卢克索·达尔文·珀斯·涛岛·Rottnest Island·杰拉尔顿·卡尔巴里·玛格丽特河·巴瑟尔顿·波浪岩</p>
                </div>
                <div class="number">
                  <span class="icon1">58</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9640855" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/1364105" target="_blank" class="name" data-bn-ipg="planhome-plan-username">windy_411</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20JZVFjBz9TY1I2Cm8/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-13">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/user/782/57/RkFXRx0CZQ/index/325x240" title="user_vZfWbYi7W9的澳大利亚五十一日游线路" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>51</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-03-17 出发</dt>
                  <dd>user_vZfWbYi7W9的澳大利亚五十一日游线路</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>长沙·悉尼·堪培拉·霍巴特·墨尔本·阿德莱德·珀斯·达尔文·凯恩斯·布里斯班·黄金海岸</p>
                </div>
                <div class="number">
                  <span class="icon1">25</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9659793" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/9144491" target="_blank" class="name" data-bn-ipg="planhome-plan-username">user_vZfWbYi7W9</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20Ja1FgBz9TYlI3Cmw/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-14">
              <div class="img">
                <img class="plan-cover" data-original="https://pic.qyer.com/album/128/9c/2003853/index/325x240" title="涵先生的澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>46</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-11-01 出发</dt>
                  <dd>涵先生的澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>北京·悉尼·墨尔本·黄金海岸·凯恩斯·布里斯班·大洋路·澳大利亚蓝山·阿波罗小镇·坎贝尔港国家公园·阿德莱德·艾尔利海滩·吉朗·龙恩·沃南布尔·珀斯·圣灵群岛·乌鲁鲁-卡塔曲塔国家公园·爱丽斯泉·袋鼠岛·库兰达·澳大利亚阳光海岸·弗雷泽岛·春溪国家公园·奥古斯塔港·尤拉拉·南澳大利亚州·北领地·西澳大利亚州·新南威尔士州·波奴鲁鲁国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">37</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9869680" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/8569012" target="_blank" class="name" data-bn-ipg="planhome-plan-username">涵先生</a>
          </div>
                  <div class="items">
            <a href="//plan.qyer.com/trip/V20Ja1FgBz9TYlI3CmU/" class="link" target ="_blank" data-bn-ipg="planhome-plan-content-15">
              <div class="img">
                <img class="plan-cover" data-original="https://pic1.qyer.com/album/179/d4/2023515/index/325x240" title="涵先生的澳大利亚行程" src="//static.qyer.com/images/plan2/index/poi_310x175.png">
                <!-- 空层，遮罩背景 -->
                <span class="bg"></span>
              </div>
              <div class="title clearfix">
                <div class="day"><strong>42</strong>天</div>
                <dl class="fontYaHei">
                  <dt>2017-11-01 出发</dt>
                  <dd>涵先生的澳大利亚行程</dd>
                </dl>
              </div>
              <div class="content">
                                <div class="tag clearfix">
                  <strong>购物</strong><strong>美食</strong>
                </div>
                                <div class="plan">
                  <p>北京·悉尼·墨尔本·黄金海岸·凯恩斯·布里斯班·大洋路·澳大利亚蓝山·阿波罗小镇·坎贝尔港国家公园·阿德莱德·艾尔利海滩·吉朗·龙恩·沃南布尔·珀斯·圣灵群岛·乌鲁鲁-卡塔曲塔国家公园·爱丽斯泉·袋鼠岛·库兰达·澳大利亚阳光海岸·弗雷泽岛·春溪国家公园·奥古斯塔港·尤拉拉·南澳大利亚州·北领地·西澳大利亚州·新南威尔士州·波奴鲁鲁国家公园</p>
                </div>
                <div class="number">
                  <span class="icon1">39</span>　|　<span class="icon2">0</span>
                </div>
              </div>
                          </a>
            <a href="javascript:;" class="copy" data-pid="9869689" data-bn-ipg="planhome-plan-copy">复制</a>
            <a rel="nofollow" href="//www.qyer.com/u/8569012" target="_blank" class="name" data-bn-ipg="planhome-plan-username">涵先生</a>
          </div>
              </div>
    </div>

    <!-- 翻页 -->
    <div class="pages clearfix">
      <!-- 翻页公用样式 -->
      <div class="ui_page"><a data-bn-ipg="pages-3" data-ra_arg="ra_null|1" data-page="1" href="http://plan.qyer.com/search_0_0_240_0_0_0_1/?cityid=6606" class='ui_page_item ui_page_item_current'>1</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|2" data-page="2" href="http://plan.qyer.com/search_0_0_240_0_0_0_2/?cityid=6606" class='ui_page_item'>2</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|3" data-page="3" href="http://plan.qyer.com/search_0_0_240_0_0_0_3/?cityid=6606" class='ui_page_item'>3</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|4" data-page="4" href="http://plan.qyer.com/search_0_0_240_0_0_0_4/?cityid=6606" class='ui_page_item'>4</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|5" data-page="5" href="http://plan.qyer.com/search_0_0_240_0_0_0_5/?cityid=6606" class='ui_page_item'>5</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|6" data-page="6" href="http://plan.qyer.com/search_0_0_240_0_0_0_6/?cityid=6606" class='ui_page_item'>6</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|7" data-page="7" href="http://plan.qyer.com/search_0_0_240_0_0_0_7/?cityid=6606" class='ui_page_item'>7</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|8" data-page="8" href="http://plan.qyer.com/search_0_0_240_0_0_0_8/?cityid=6606" class='ui_page_item'>8</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|9" data-page="9" href="http://plan.qyer.com/search_0_0_240_0_0_0_9/?cityid=6606" class='ui_page_item'>9</a>
<a data-bn-ipg="pages-3" data-ra_arg="ra_null|10" data-page="10" href="http://plan.qyer.com/search_0_0_240_0_0_0_10/?cityid=6606" class='ui_page_item'>10</a>
<a data-bn-ipg="pages-4" data-ra_arg="ra_null|18" data-page="18" href="http://plan.qyer.com/search_0_0_240_0_0_0_18/?cityid=6606" class='ui_page_item' title="...18">...18</a>
<a data-bn-ipg="pages-5" data-ra_arg="ra_null|2" data-page="2" href="http://plan.qyer.com/search_0_0_240_0_0_0_2/?cityid=6606" class='ui_page_item ui_page_next' title="下一页">下一页</a>
</div>
    </div>
  </div>
            <a href="//plan.qyer.com/create?from=search"
         data-bn-ipg="plan-search-createplan"
         target="_blank"
         style="text-decoration:none"
         class="intro-block-mini">
        <div class="intro-block">
  <p class="intro-block_title">行程助手可以帮我做什么？</p>
  <div>
    <img class="intro-block_img" src="//common3.qyerstatic.com/plan/desktop/shared/img/plan_browser_plan_introduce_1.jpg" width="315" height="265">
    <img class="intro-block_img" src="//common3.qyerstatic.com/plan/desktop/shared/img/plan_browser_plan_introduce_3.jpg" width="313" height="265">
    <img src="//common3.qyerstatic.com/plan/desktop/shared/img/plan_browser_plan_introduce_2.jpg" width="315" height="265">
  </div>
  <div class="intro-block_btn" data-bn-ipg="planview-bottom-ad-createplan">+ 制定我的行程</div>
</div>
      </a>
      

  <!-- 1.5新增列表 -->
  <div class="bot_list  clearfix">
          <dl>
        <dt>相关问题</dt>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/1301998.html">阳朔西街酒店如何?</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2156528.html">北海道直寿し怎么样？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2266409.html">琅勃拉邦金莲花广场宾馆怎么样？有人住过吗？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2384663.html">谁住过鲁昂植物园度假屋，怎么样？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2536514.html">谁住过波尔图林哈 22酒店,是否推荐？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2540146.html">三宝垄橡树翡翠酒店怎么样？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2598000.html">求助：关于芬兰申根签的一些问题</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/2946042.html">哈瓦那海明威故居要门票吗？多少钱？</a></dd>
                  <dd><a target="_blank" href="http://ask.qyer.com/question/3138252.html">打算去土耳其-阿联酋13天，请帮忙看下这个行程？</a></dd>
              </dl>
    
    <dl>
      <dt>热门国家路线</dt>
              <dd><a href="http://plan.qyer.com/search_0_0_215_0_0_0_1/">泰国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_14_0_0_0_1/">日本旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_186_0_0_0_1/">法国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_189_0_0_0_1/">意大利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_233_0_0_0_1/">韩国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_213_0_0_0_1/">马来西亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_236_0_0_0_1/">美国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_15_0_0_0_1/">德国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_232_0_0_0_1/">新加坡旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_182_0_0_0_1/">西班牙旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_0_0_13_0_0_0_1/">英国旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_524_0_0_0_1/">瑞士旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_219_0_0_0_1/">柬埔寨旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_198_0_0_0_1/">奥地利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_200_0_0_0_1/">荷兰旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_240_0_0_0_1/">澳大利亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_216_0_0_0_1/">越南旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_804_0_0_0_1/">梵蒂冈旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_570_0_0_0_1/">印度尼西亚旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_193_0_0_0_1/">捷克旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_0_0_424_0_0_0_1/">比利时旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_446_0_0_0_1/">菲律宾旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_195_0_0_0_1/">土耳其旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_241_0_0_0_1/">新西兰旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_206_0_0_0_1/">希腊旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_238_0_0_0_1/">加拿大旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_208_0_0_0_1/">俄罗斯旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_207_0_0_0_1/">匈牙利旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_202_0_0_0_1/">瑞典旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_220_0_0_0_1/">尼泊尔旅游线路</a></dd>
          </dl>
  
    <dl>
      <dt>热门主题线路</dt>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_1_1/">美食旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_2_1/">人文旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_3_1/">购物旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_4_1/">游园观光旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_6_1/">沙滩海岛旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_8_1/">自然风光旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_9_1/">自驾旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_10_1/">蜜月旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_0_0_0_0_0_11_1/">亲子旅游线路</a></dd>
          </dl>
  
    <dl>
      <dt>热门季节线路</dt>
              <dd><a href="http://plan.qyer.com/search_1_0_0_0_0_0_1/">一月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_2_0_0_0_0_0_1/">二月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_3_0_0_0_0_0_1/">三月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_4_0_0_0_0_0_1/">四月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_5_0_0_0_0_0_1/">五月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_6_0_0_0_0_0_1/">六月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_7_0_0_0_0_0_1/">七月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_8_0_0_0_0_0_1/">八月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_9_0_0_0_0_0_1/">九月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_10_0_0_0_0_0_1/">十月出发旅游线路</a></dd>
          
              <dd><a href="http://plan.qyer.com/search_11_0_0_0_0_0_1/">十一月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_12_0_0_0_0_0_1/">十二月出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_13_0_0_0_0_0_1/">新年出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_14_0_0_0_0_0_1/">春节出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_15_0_0_0_0_0_1/">清明出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_16_0_0_0_0_0_1/">劳动节出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_17_0_0_0_0_0_1/">端午出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_18_0_0_0_0_0_1/">中秋出发旅游线路</a></dd>
              <dd><a href="http://plan.qyer.com/search_19_0_0_0_0_0_1/">国庆出发旅游线路</a></dd>
          </dl>
  </div>

  <!-- 全站底部 -->
    <div style="display: none;"></div>
<div class="qyer_footer">
	<div class="topline"></div>
	<div class="content">
		<p class="nav">
			<a href="//www.qyer.com/htmlpages/about.html" target="_blank" rel="nofollow" data-bn-ipg="foot-about-1">穷游简介</a>
			<a href="//www.qyer.com/partner/" target="_blank" rel="nofollow" data-bn-ipg="foot-about-3">合作伙伴</a>
			<a href="//www.qyer.com/job/" target="_blank" rel="nofollow" data-bn-ipg="foot-join-1">加入我们</a>
			<a href="//site.qyer.com/tyro/" target="_blank" rel="nofollow" data-bn-ipg="foot-help-1">新手上路</a>
			<a href="//bbs.qyer.com/forum-10-1.html" target="_blank" rel="nofollow" data-bn-ipg="foot-help-2">使用帮助</a>
			<a href="//www.qyer.com/sitemap.html" target="_blank" data-bn-ipg="foot-help-4">网站地图</a>
			<a href="//www.qyer.com/htmlpages/member.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-1">会员条款</a>
			<a href="//www.qyer.com/htmlpages/bbsguide.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-2">社区指南</a>
			<a href="//www.qyer.com/htmlpages/copyright.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-3">版权声明</a>
			<a href="//www.qyer.com/htmlpages/exemption.html" target="_blank" rel="nofollow" data-bn-ipg="foot-clause-4">免责声明</a>
			<a href="//www.qyer.com/htmlpages/contact.html" target="_blank" rel="nofollow" data-bn-ipg="foot-about-2">联系我们</a>
		</p>
		<p class="info">
			2004-2017 &copy; 穷游网&reg;  qyer.com All rights reserved. Version v5.57  京ICP备12003524号  京公网安备11010102001935号  京ICP证140673号
			<a target="_blank" style="color:inherit;" href="//static.qyer.com/images/yyzz.jpg">营业执照</a>
			<a target="_blank" style="color:inherit;" href="//static.qyer.com/images/jyxkz.jpg">经营许可证</a>
		</p>
    
        <!--友情链接模块-->
        
	</div>
</div>



<script>
        var script   = document.createElement("script");
        script.type  = "text/javascript";
        script.async = true;
        script.src   = "//static.qyer.com/qyer_ui_frame/m/js/dist/base_beacon_ga.js";
        document.getElementsByTagName("head")[0].appendChild(script);
</script>
  <!-- /全站底部 -->

  <!-- 底部公用 -->
  <!--div class="qr-code-fixed" style="cursor:pointer">
    <a href="javascript:;" alt="关闭">关闭</a>
  </div-->

  <!--创建新的行程 更多选择-->
  <ul class="createFun createFun2 fontYaHei" id="createBtnMore">
    <li><a data-bn-ipg="planhome-1-createplan-bymyself" href="/create" target="_blank">自己制定</a></li>
    <li><a data-bn-ipg="planhome-1-createplan-createforme" href="/smartcreate/" target="_blank">帮我制定</a></li>
  </ul>
  <!--/创建新的行程 更多选择-->

  <!--loading 弹层-->
  <div class="plan-dialog plan-dialog-loading" style="display:none;">
    <div class="plan-dialog-bg"></div>
    <div class="plan-dialog-icon">
      <img src="//common3.qyerstatic.com/plan/new/project/web/plan/img/loadingding.gif">
      <i>行程复制中...</i>
    </div>
  </div>
  <!--/loading 弹层-->


  <script src="//common1.qyerstatic.com/plan/desktop/home/js/footer.e45492a2144a472068720915eb851bf0.js"></script>
</body>
</html>

'''
'''
<a data-bn-ipg="pages-5" data-ra_arg="ra_null|2" data-page="2" href="http://plan.qyer.com/search_0_0_240_0_0_0_2/?cityid=6606" class='ui_page_item ui_page_next' title="下一页">下一页</a>
'''

from scrapy.selector import Selector
def restractUrl():
    from scrapy.selector import Selector
    select = Selector(text=newtest)
    rp1 = select.re('href=\"(http:.*\d)\" class=\"ui_page_item ui_page_next\"')
    print(rp1)


head = '''
<header>
      <h2>D1</h2>
      <div class="text-container vm">
        <div class="vm-inner">
<h3>12月27日<span class="sep">|</span><span class="copy-day" data-id="33871605" data-bn-ipg="planview-day-head-copyday">复制单日行程</span></h3>
    <h4>
        <a href="//place.qyer.com/singapore/" target="_blank" data-bn-ipg="planview-content-city">新加坡&nbsp;Singapore</a>
        <em class="iconfont"></em>
        <a href="//place.qyer.com/siem-reap/" target="_blank" data-bn-ipg="planview-content-city">暹粒&nbsp;Siem Reap</a>
        </h4>
            </div>
          </div>
        </header>
'''
dayDiv = '''
<div class="day" data-day-index="0">
        <!-- 一天的头部 -->
        <header>
          <h2>D1</h2>
          <div class="text-container vm">
            <div class="vm-inner">
                                              <h3>09月27日<span class="sep">|</span><span class="copy-day" data-id="89490142" data-bn-ipg="planview-day-head-copyday">复制单日行程</span></h3>
                            <h4>
                                                                                                <span>上海&nbsp;Shanghai</span>
                                                                              <em class="iconfont"></em>
                                                              <a href="//place.qyer.com/kathmandu/" target="_blank" data-bn-ipg="planview-content-city">加德满都&nbsp;Kathmandu</a>
                                                                    </h4>
            </div>
          </div>
        </header> 

                            
          <!-- 遍历交通 -->
                                <article class="traffic clearfix" data-onedayid="89490142" data-lat="" data-lng="" data-id="415482191" data-pid="11595" data-to_id="415482192" data-to_pid="11799" data-to_lat="25.085682" data-to_lng="102.921852" data-to_traffic_poi_id="205700" data-to_traffic_poi_name="昆明长水国际机场" data-cnname="" data-enname="" data-type="traffic">
        <div class="dotted bottom"></div>
              <figure>
                                                                                                                                                      <img src="//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/traffic_plane.jpg" onerror="this.src='//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/traffic_plane.jpg'">
                              </figure>
    <section>
    <!-- 交通 -->
          <dl class="clearfix">
                  <dt>出发：</dt>
          <dd>
            <span class="ellipsis" title="上海（上海虹桥国际机场）">
              上海
                              （上海虹桥国际机场）
                          </span>
                          <time>
                08:15              </time>
                      </dd>
                          <dt>到达：</dt>
          <dd>
            <span class="ellipsis" title="昆明（昆明长水国际机场）">
              昆明
                              （昆明长水国际机场）
                          </span>
                          <time>
                11:45                              </time>
                      </dd>
              </dl>
      <ul>
        <!-- 花费 -->
                <!-- 备注 -->
                <!-- 距离 -->
        <li>
  <em class="iconfont"></em>
                          <span>距离：1957KM，98%的用户选择了飞机，平均用时3小时。</span>
</li>
      </ul>
    
    <!-- 优选 -->
    
    <!-- 景点 -->
    
    <!-- 酒店 -->
      </section>

</article>

<!-- 点对点交通 -->
<div class="sep" data-status="finish" data-bn-ipg="planview-content-traffic" data-tripmode="">
  <em class="iconfont"></em>
  <span>1771.68km</span>
</div>

<!-- 0 -->
                      <article class="traffic clearfix" data-onedayid="89490142" data-lat="" data-lng="" data-id="417578162" data-pid="11799" data-to_id="417578163" data-to_pid="59" data-to_lat="27.696863" data-to_lng="85.359177" data-to_traffic_poi_id="33836" data-to_traffic_poi_name="特里布万国际机场" data-cnname="" data-enname="" data-type="traffic">
      <div class="dotted top"></div>
        <div class="dotted bottom"></div>
              <figure>
                                                                                                                                                      <img src="//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/traffic_plane.jpg" onerror="this.src='//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/traffic_plane.jpg'">
                              </figure>
    <section>
    <!-- 交通 -->
          <dl class="clearfix">
                  <dt>出发：</dt>
          <dd>
            <span class="ellipsis" title="昆明（昆明长水国际机场）">
              昆明
                              （昆明长水国际机场）
                          </span>
                          <time>
                14:25              </time>
                      </dd>
                          <dt>到达：</dt>
          <dd>
            <span class="ellipsis" title="加德满都（特里布万国际机场）">
              加德满都
                              （特里布万国际机场）
                          </span>
                          <time>
                15:35                              </time>
                      </dd>
              </dl>
      <ul>
        <!-- 花费 -->
                <!-- 备注 -->
                <!-- 距离 -->
        <li>
  <em class="iconfont"></em>
                          <span>距离：3310KM，100%的用户选择了飞机，平均用时3小时。</span>
</li>
      </ul>
    
    <!-- 优选 -->
    
    <!-- 景点 -->
    
    <!-- 酒店 -->
      </section>

</article>

<!-- 点对点交通 -->
<div class="sep" data-status="finish" data-bn-ipg="planview-content-traffic" data-tripmode="driving">
  <em class="iconfont"></em>
  <span>9.29km</span>
</div>

<!-- 1 -->
          
          <!-- 遍历POI -->
                                                            <article class="poi clearfix" data-onedayid="89490142" data-lat="27.702770" data-lng="85.316452" data-id="418262132" data-pid="33818" data-to_id="" data-to_pid="" data-to_lat="" data-to_lng="" data-to_traffic_poi_id="" data-to_traffic_poi_name="" data-cnname="从泰米尔到杜巴广场老城区" data-enname="Thamel - Durbar Square" data-type="poi">
      <div class="dotted top"></div>
        <div class="dotted bottom"></div>
            <a href="http:////place.qyer.com/poi/V2cJYFFuBzdTbA/" target="_blank" data-bn-ipg="planview-content-poi-pic">
        <figure>
                                                                                                            <img src="http://pic1.qyer.com/album/1af/cf/1839264/index/308x240" onerror="this.src='//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/poi_default.jpg'">
                          <figcaption>必去</figcaption>
                      </figure>
      </a>
    <section>
    <!-- 交通 -->
    
    <!-- 优选 -->
    
    <!-- 景点 -->
          <h5 class="ellipsis">
                  <a title="从泰米尔到杜巴广场老城区&nbsp;Thamel - Durbar Square" href="http://place.qyer.com/poi/V2cJYFFuBzdTbA/" target="_blank" data-bn-ipg="planview-content-poi-title">从泰米尔到杜巴广场老城区&nbsp;Thamel - Durbar Square</a>
              </h5>
      <p>
                                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont gray"></em>
                                <span class="green">8.6分</span>
                                    <em class="sep"></em>
          <span>252人点评</span>
                          <span class="right">加德满都景点榜<i class="red">第2位</i></span>
              </p>
      <ul>
        <!-- 花费 -->
                <!-- 时间 -->
                <!-- 备注 -->
              </ul>
              <cite>
          <figure>
            <a href="//www.qyer.com/u/4099134" target="_blank" data-bn-ipg="planview-content-poi-user">
              <img src="http://pic1.qyer.com/avatar/004/09/91/34/1476435876/index/48?v=1476435876" alt="很给力的范范">
            </a>
          </figure>
          <div class="text-container">
            <em>
              <a href="//www.qyer.com/u/4099134" target="_blank" data-bn-ipg="planview-content-poi-user">
                很给力的范范
              </a>
              ：
            </em>
            “小鸟在前面带路，风儿吹向我们”只是“你是风儿我是沙...”尘土飞扬啊尘土飞扬。的确比较落后，但是充满生活气息，对上眼了给你个微笑的是路人，来句“你好”但是不惹人讨厌保持距离跟着在旁边的是商人。很努力生存的人们，琳琅满目的商品。努力讲价，如果看到有妇女背着瓶装水在卖，可以支持一下。电线杆的线看起来很危险啊....到处是狗，鸽子和牛。
          </div>
        </cite>
          
    <!-- 酒店 -->
      </section>

</article>

<!-- 点对点交通 -->
<div class="sep" data-status="finish" data-bn-ipg="planview-content-traffic" data-tripmode="">
  <em class="iconfont"></em>
  <span>1.27km</span>
</div>

<!-- 2 -->
                                                            <article class="poi clearfix" data-onedayid="89490142" data-lat="27.714134" data-lng="85.314835" data-id="418758532" data-pid="86518" data-to_id="" data-to_pid="" data-to_lat="" data-to_lng="" data-to_traffic_poi_id="" data-to_traffic_poi_name="" data-cnname="梦想花园" data-enname="Dream Garden" data-type="poi">
      <div class="dotted top"></div>
        <div class="dotted bottom"></div>
            <a href="http:////place.qyer.com/poi/V2wJZVFjBzdTbA/" target="_blank" data-bn-ipg="planview-content-poi-pic">
        <figure>
                                                                                                            <img src="http://pic1.qyer.com/album/user/1606/57/QE9VRB8AZUw/index/308x240" onerror="this.src='//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/poi_default.jpg'">
                              </figure>
      </a>
    <section>
    <!-- 交通 -->
    
    <!-- 优选 -->
    
    <!-- 景点 -->
          <h5 class="ellipsis">
                  <a title="梦想花园&nbsp;Dream Garden" href="http://place.qyer.com/poi/V2wJZVFjBzdTbA/" target="_blank" data-bn-ipg="planview-content-poi-title">梦想花园&nbsp;Dream Garden</a>
              </h5>
      <p>
                                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont gray"></em>
                                <span class="green">8.4分</span>
                                    <em class="sep"></em>
          <span>62人点评</span>
                          <span class="right">加德满都景点榜<i class="red">第19位</i></span>
              </p>
      <ul>
        <!-- 花费 -->
                <!-- 时间 -->
                <!-- 备注 -->
              </ul>
              <cite>
          <figure>
            <a href="//www.qyer.com/u/1611281" target="_blank" data-bn-ipg="planview-content-poi-user">
              <img src="http://pic1.qyer.com/avatar/001/61/12/81/index/48?v=" alt="FightingDarcy">
            </a>
          </figure>
          <div class="text-container">
            <em>
              <a href="//www.qyer.com/u/1611281" target="_blank" data-bn-ipg="planview-content-poi-user">
                FightingDarcy
              </a>
              ：
            </em>
            说实话是一般般的，还不如我们家楼下的湖岸公园好看一些= =但是这是在加都啊。里面有许多可爱的小松鼠，会跑来跟你抢面包吃。里面还有一家餐厅，东西做得很漂亮，口味一般般。他们会送面包，可以拿来喂小松鼠哈哈哈。
          </div>
        </cite>
          
    <!-- 酒店 -->
      </section>

</article>

<!-- 点对点交通 -->
<div class="sep" data-status="finish">
  <em class="iconfont"></em>
  <span>地理位置信息缺失</span>
</div>

<!-- 3 -->
                                                            <article class="poi clearfix" data-onedayid="89490142" data-lat="" data-lng="" data-id="418759729" data-pid="98682" data-to_id="" data-to_pid="" data-to_lat="" data-to_lng="" data-to_traffic_poi_id="" data-to_traffic_poi_name="" data-cnname="" data-enname="GreenLine" data-type="poi">
      <div class="dotted top"></div>
              <a href="http:////place.qyer.com/poi/V20Ja1FgBz5TZg/" target="_blank" data-bn-ipg="planview-content-poi-pic">
        <figure>
                                                                                                                                              <img src="http://pic.qyer.com/album/user/1580/77/QExdQh0AZEs/index/308x240" onerror="this.src='//common3.qyerstatic.com/plan/mobile/shared/img/default_pic/400x300/poi_traffic.jpg'">
                              </figure>
      </a>
    <section>
    <!-- 交通 -->
    
    <!-- 优选 -->
    
    <!-- 景点 -->
          <h5 class="ellipsis">
                  <a title="&nbsp;GreenLine" href="http://place.qyer.com/poi/V20Ja1FgBz5TZg/" target="_blank" data-bn-ipg="planview-content-poi-title">&nbsp;GreenLine</a>
              </h5>
      <p>
                                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont green"></em>
                    <em class="iconfont gray"></em>
                                <span class="green">8.4分</span>
                                    <em class="sep"></em>
          <span>5人点评</span>
                          <span class="right">加德满都交通榜<i class="red">第9位</i></span>
              </p>
      <ul>
        <!-- 花费 -->
                <!-- 时间 -->
                <!-- 备注 -->
              </ul>
              <cite>
          <figure>
            <a href="//www.qyer.com/u/4876604" target="_blank" data-bn-ipg="planview-content-poi-user">
              <img src="http://pic1.qyer.com/avatar/004/87/66/04/1453113025/index/48?v=1453113030" alt="琳姨">
            </a>
          </figure>
          <div class="text-container">
            <em>
              <a href="//www.qyer.com/u/4876604" target="_blank" data-bn-ipg="planview-content-poi-user">
                琳姨
              </a>
              ：
            </em>
            奇旺没有Greenline直接返回加德满都，但是奇旺为愿意花钱的游客设置了接驳Greenline的专车。由于从博卡拉去奇旺时乘坐那种“Tourests Only”吃了苦头，我们要求换乘Greenline。结果，每人补交20美元，一部舒适的空调公务车把我们几个从奇旺送到吃午餐的地方，让我们在这里吃过免费午餐后，转车上了从博卡拉返程加德满都的Greenline。 <br>
       这一天，在离加德满都不远的山上，路上大塞车，车辆排在险要狭窄的山道上，一部接着一部，延绵十几公里。这一次，我们被堵了差不多三个小时。不幸之中万幸的是：我们换了Greenline！
          </div>
        </cite>
          
    <!-- 酒店 -->
      </section>

</article>

<!-- 点对点交通 -->

<!-- 4 -->
          
          <!-- 遍历酒店 -->
                    
          <!-- 遍历笔记 -->
          
              </div>'''
import re
def restractHeaderInfoForOneDay(headText):
    #提取每一天的头部信息
    info = dict()
    day_index_p = re.compile('<h2>(.*)</h2>')
    date_p = re.compile('<h3>(\w*)<span')
    line_p = re.compile('<a href.*?>(.*?)</a>')#非贪婪形式
    info['date'] = date_p.findall(headText)[0]
    info['day_index'] = day_index_p.findall(headText)[0]
    pos = line_p.findall(headText)
    pos = [filter_text2(filter_text2(x,'&nbsp;'),'\xa0') for x in pos]
    info['line'] = pos
    return info
def filter_text2(text,flag):
    if text.find(flag) is -1:
        return text
    else:
        return text.replace(flag,' ')

'''
@:parameter text 要匹配的文本
@:parameter regex 正则表达式
@:parameter func 对匹配结果处理的函数

@:return the result as a list
'''
def restract(regex, text, func=None ):
    pattern = re.compile(regex,re.S)
    r = pattern.findall(text)
    if func is None:
        return r
    else:
        if callable(func):
            func(r)
        else:
            raise Exception('参数三不可被调用')

def showResult(list):
    for i, item in enumerate(list):
        print(i,item)


def restractPoiArticle(poiText):
    #种类为景点的article
    info = dict()
    posNameRe ='<h5 class="ellipsis".*?<a title="(.*?)"'#景点名
    posNameWithSpanRe = '<h5 class="ellipsis".*?<(?:a|span) title="(.*?)"'
    scoreRe = '>(...)分' #得分
    peopleNumRe = '(\d*)人点评'
    bangNameRe = u'right.*\"(.*)榜'
    rankRe = '第(\d*)位'
    posInfoRe = 'planview-content-poi-user.*</em>(.*?)</div>'
    posName = restract(posNameWithSpanRe, poiText)
    score = restract(scoreRe,poiText)
    peopleNum = restract(peopleNumRe,poiText)
    rankName = restract(bangNameRe,poiText)
    rank = restract(rankRe,poiText)
    posInfo = restract(posInfoRe,poiText)
    if len(posName) is not 0:
        info['posName'] = filter_text2(filter_text2(posName[0],'&nbsp;'),'\xa0')
    else:
        info['posName'] = ''

    if len(score) is not 0:
        info['score'] = score[0]
    else:
        info['score'] = ''

    if len(peopleNum) is not 0:
        info['peopleNumOfCom'] = peopleNum[0]
    else:
        info['peopleNumOfCom'] = ''

    if len(rankName) is not 0:
        info['rankName'] = rankName[0].replace('>','')
    else:
        info['rankName'] = ''

    if len(rank) is not 0:
        info['rank'] = rank[0]
    else:
        info['rank'] = ''

    if len(posInfo) is not 0:
        info['posInfo'] = posInfo[0].strip()
    else:
        info['posInfo'] = ''

    if poiText.find('自定义') is not -1:
        info['type'] = '自定义'

    return info
def restractTrafficeArticle(trafficText):
    #提取traffic信息
    info = dict()
    artrifficRe = '<dd>.*?<span class="ellipsis" title="(.*?)">.*?</span>\s*?(?:<time>\s*(\S*?)\s*</time>)?\s*?</dd>'#提取当天航线信息，飞机和时间
    trifficSuggRe = '<span>(距离.*?)</span>'#建议 距离：1957KM，98%的用户选择了飞机，平均用时3小时。
    info['traffic'] = restract(artrifficRe,trafficText)
    info['sugg'] = restract(trifficSuggRe,trafficText)
    return info
from qx.guojia import hotel
def restractHotelArticle(hotelText):
    info = dict()
    hotelNameRe = '<a title=\"(.*?)\"'
    scoreRe = '用户评分(.*?)分'
    priceRe = '<b class="\w*">(\d*)</b>'
    addressRe = '<li class="place">(.*?)</li>'
    aroundPoiRe = '<b>(.*?)</b>'      #附近景点
    resonOfRecommendRe = '<li class="ellipsis" title="(.*?)">'#推荐理由
    info['hotelName'] = restract(hotelNameRe,hotelText)[0]
    score = restract(scoreRe,hotelText)
    price = restract(priceRe,hotelText)
    addressTemp = restract(addressRe, hotelText)
    info['score'] = score[0] if len(score) is not 0 else ''
    info['price'] = price[0] if len(price) is not 0 else ''
    info['address'] = restract('<a.*?>(.*?)</a>',addressTemp[0]) if len(addressTemp) is not 0 else []
    info['arounfPoi'] = restract(aroundPoiRe,hotelText)
    info['resonOfRecommend'] = restract(resonOfRecommendRe,hotelText)
    return info
def getArtileAsListForOneDay(dayText):
    infoList = []
    articleRe = '<article.*?</article>'#当前Day的所有article
    articleTexts = restract(articleRe, dayText)
    articleInfo = dict()
    for articleText in articleTexts:
        if articleText.find('class="hotel clearfix"') is not -1:
            articleInfo = restractHotelArticle(hotelText=articleText)
        elif articleText.find('class="poi clearfix"') is not -1:
            articleInfo = restractPoiArticle(poiText=articleText)
        elif articleText.find('class="traffic clearfix"') is not -1:
            articleInfo = restractTrafficeArticle(trafficText=articleText)
        infoList.append(articleInfo)
    return infoList
def getDistinceAsListForOneDay(dayText):
    infoList = []
    sepRe = '<div class="sep".*?</div>'#提取Day块的所有行走方式Div
    sepDisRe = '<span>(.*)</span>'
    li = restract(sepRe,dayText)
    for item in li:
        pattern = re.compile(sepDisRe,re.S)
        infoList.append(pattern.findall(item)[0])
    return infoList
def getHeaderAsDict(dayText):
    headerRe = '<header>.*?</header>'
    headerText = restract(headerRe,dayText)[0]
    return restractHeaderInfoForOneDay(headerText)
#提取每一天的信息
def restractDayInfo(dayText):
    infoList = []
    headerInfoDict = getHeaderAsDict(dayText)
    articleList = getArtileAsListForOneDay(dayText)
    distinceList = getDistinceAsListForOneDay(dayText)
    infoList.append(headerInfoDict)
    if len(articleList) is 0:
        infoList.append('当日暂无行程安排')
        return infoList
    for index, distinceinfo in enumerate(distinceList):
        infoList.append(articleList[index])
        infoList.append(distinceinfo)
    infoList.append(articleList[-1])
    return infoList
def restractXCInfo(response):
    from scrapy.selector import Selector
    infoList = []
    select = Selector(response)
    daysText = select.xpath("//div[@class='day']").extract()
    for dayText in  daysText:
        dayInfoList = restractDayInfo(dayText)
        infoList.append(dayInfoList)
        print(dayInfoList)
        print('-------' * 20)
    return infoList
def main():
    articleRe = '<article.*?</article>'#当前Day的所有article
    sepRe = '<div class="sep".*?</div>'#提取Day块的所有行走方式Div
    sepDisRe = '<span>(.*)</span>'
    #种类为traffic的article
    artrifficRe = '<span class="ellipsis" title="(.*?)">.*?<time>\s*(\S*?)\s*</time>'#提取当天航线信息，飞机和时间
    trifficSuggRe = '<span>(距离.*?)</span>'#建议 距离：1957KM，98%的用户选择了飞机，平均用时3小时。
    #种类为景点的article
    posNameRe = 'planview-content-poi-title\">(.*?)</a>'#景点名
    scoreRe = '>(...)分' #得分
    peopleNumRe = '(\d*)人点评'
    bangNameRe = u'right.*\"(.*)榜'
    rankRe = '第(\d*)位'
    posInfoRe = 'planview-content-poi-user.*</em>(.*?)</div>'
    #print(restract('jijiji','nihao')[0])
    from qx.guojia import xingcheng
    restractXCInfo(xingcheng)

    #restract(posInfoRe,text=poi,func=showResult)
    #result = restractPoiArticle(poiText=poi)
    #result = restractTrafficeArticle(traffic)
    #print(result)
    #print(restractHotelArticle(hotel))
#li = restract(sepRe,dayDiv)
 #restractInfoFromResult(list=li,regex=sepDisRe,func=showResult)
#restract(dayDiv, articleRe)
                #restractHeaderInfo()
  #restarctXCInfo()
    #rp2 = p1.search(test)

#p1 = re.compile('<ul class="clearfix" style="display:none;">(.*?)</ul>',re.S) #这个正则表达式会找的7个匹配<ul></ul>
#rp1 = select.re(p1)
#rp2 = p1.search(test)
#print(len(rp2.groups()))#长度为1，search找到第一个就返回
#for i in range(len(rp2.groups())):
 #   print(rp2.group(i))
#rp1 = p1.findall(test)
'''
<tr>
<td>122.192.66.50</td>
<td>808</td>
<td>江苏 </td>
<td>
<div class="graph"><strong class="bar" style="width: 28%; background:#dd0000;"><span></span></strong></div>
</td>
<td>2017-08-15 06:20:45</td>
</tr>'''
from qx.guojia import proxy
list = re.findall('<tr>.*?<td>(.*?)</td>\n<td>(.*?)</td>.*?</tr>',proxy, re.S)
proxys = dict(list[1:-1])
for i in proxys:
    if i == '服务器地址':
        continue
    #print(i,':',proxys.get(i))
    print('\''+':'.join((i,proxys.get(i)))+'\',')
if __name__ == '__main__':
    '''
    import requests
    class Proxy(object):
        proxy = {}

        @staticmethod
        def get_proxy():
            r = requests.request('GET', 'http://cn-proxy.com/')
            print(r.text)

    Proxy.get_proxy()'''

