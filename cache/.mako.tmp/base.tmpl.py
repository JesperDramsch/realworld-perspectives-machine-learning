# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669218203.3640919
_enable_loop = True
_template_filename = 'themes/maupassant/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body>\r\n<div class="body_container">\r\n    <div id="header">\r\n        <div class="site-name">\r\n')
        if logo_url:
            __M_writer('            <a id="logo" href="')
            __M_writer(str(blog_url))
            __M_writer('"><img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('"></a>\r\n')
        else:
            __M_writer('                <h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1>\r\n')
        __M_writer('        </div>\r\n\r\n        <div id="nav-menu">\r\n            <div class="bitcron_nav_container">\r\n                <div class="bitcron_nav">\r\n                    <div class="site_nav_wrap">\r\n                        <ul class="site_nav sm sm-base">\r\n                            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\r\n                            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\r\n                        </ul>\r\n                        <div class="clear clear_nav_inline_end"></div>\r\n                    </div>\r\n                </div>\r\n                <div class="clear clear_nav_end"></div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div id="layout">\r\n        <div class="pure-g">\r\n            <div class=" pure-u-24-24 pure-u-sm-24-24 pure-u-md-18-24 pure_cell">\r\n                <div class="content_container">\r\n                    <!--Body content-->\r\n                    <div class="row">\r\n                        ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n                </div>\r\n                <!--End of body content-->\r\n                <div style="clear:both;height:0;"></div>\r\n            </div>\r\n        </div>\r\n\r\n        <!-- Sidebar -->\r\n\r\n        <div class=" pure-u-6-24 pure_cell">\r\n            <div id="sidebar">\r\n                <div class="widget">\r\n                    <div id="search_bar">\r\n')
        if search_form:
            __M_writer('                        ')
            __M_writer(str(search_form))
            __M_writer('\r\n')
        __M_writer('                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div id="footer">\r\n        ')
        __M_writer(str(content_footer))
        __M_writer('\r\n        ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\r\n    </div>\r\n\r\n    <!--FIXME: put these somewhere                            -->\r\n    <!--%if len(translations) > 1:-->\r\n    <!--<li>')
        __M_writer(str(base.html_translations()))
        __M_writer('</li>-->\r\n    <!--%endif-->\r\n    <!--% if show_sourcelink:-->\r\n    <!--')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('-->\r\n    <!--%endif-->\r\n    <link href="/assets/css/duoshuo.css" type="text/css" rel="stylesheet"/>\r\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\r\n    <script>$(\'a.image-reference:not(.islink) img:not(.islink)\').parent().colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\r\n    <!-- fancy dates -->\r\n    <script>\r\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\r\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\r\n    </script>\r\n    <!-- end fancy dates -->\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(body_end))
        __M_writer('\r\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "54": 2, "55": 3, "56": 3, "57": 4, "58": 4, "63": 7, "64": 8, "65": 8, "66": 14, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 15, "73": 15, "74": 16, "75": 17, "76": 17, "77": 17, "78": 19, "79": 26, "80": 26, "81": 27, "82": 27, "83": 42, "84": 42, "89": 43, "90": 56, "91": 57, "92": 57, "93": 57, "94": 59, "95": 65, "96": 65, "97": 66, "98": 66, "99": 71, "100": 71, "105": 74, "106": 77, "107": 77, "108": 81, "109": 81, "110": 82, "111": 82, "112": 82, "113": 82, "118": 85, "119": 86, "120": 86, "121": 87, "122": 87, "128": 5, "136": 5, "142": 43, "155": 74, "168": 85, "181": 168}}
__M_END_METADATA
"""
