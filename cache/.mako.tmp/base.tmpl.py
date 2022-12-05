# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1670264338.05983
_enable_loop = True
_template_filename = 'themes/canterville/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'cover', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        header = _mako_get_namespace(context, 'header')
        base = _mako_get_namespace(context, 'base')
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        footer = _mako_get_namespace(context, 'footer')
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        GHOST_URL = _import_ns.get('GHOST_URL', context.get('GHOST_URL', UNDEFINED))
        TWITTER_URL = _import_ns.get('TWITTER_URL', context.get('TWITTER_URL', UNDEFINED))
        LINKEDIN_URL = _import_ns.get('LINKEDIN_URL', context.get('LINKEDIN_URL', UNDEFINED))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def cover():
            return render_cover(context._locals(__M_locals))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        GITHUB_URL = _import_ns.get('GITHUB_URL', context.get('GITHUB_URL', UNDEFINED))
        WORKSHOP_URL = _import_ns.get('WORKSHOP_URL', context.get('WORKSHOP_URL', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        HUGO_URL = _import_ns.get('HUGO_URL', context.get('HUGO_URL', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body class="nav-closed">\n')
        __M_writer(str(header.html_navigation_links()))
        __M_writer('\n\n<div class="site-wrapper">\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'cover'):
            context['self'].cover(**pageargs)
        

        __M_writer('\n    <main id="content" class="content" role="main">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n    </main>\n    ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n</div>\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_cover(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        TWITTER_URL = _import_ns.get('TWITTER_URL', context.get('TWITTER_URL', UNDEFINED))
        LINKEDIN_URL = _import_ns.get('LINKEDIN_URL', context.get('LINKEDIN_URL', UNDEFINED))
        def cover():
            return render_cover(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        GITHUB_URL = _import_ns.get('GITHUB_URL', context.get('GITHUB_URL', UNDEFINED))
        WORKSHOP_URL = _import_ns.get('WORKSHOP_URL', context.get('WORKSHOP_URL', UNDEFINED))
        HUGO_URL = _import_ns.get('HUGO_URL', context.get('HUGO_URL', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        GHOST_URL = _import_ns.get('GHOST_URL', context.get('GHOST_URL', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'main_index' in pagekind and BANNER_URL :
            __M_writer('    <header class="main-header" style="background-image: url(')
            __M_writer(str(BANNER_URL))
            __M_writer(')">\n')
        elif 'post_page' in pagekind and post.meta('banner'):
            __M_writer('    <header class="main-header" style="background-image: url(')
            __M_writer(str(post.meta('banner')))
            __M_writer(')">\n')
        else:
            __M_writer('    <header class="main-header" style="background-image: url(')
            __M_writer(str(BANNER_URL))
            __M_writer(')">\n')
        __M_writer('        <nav class="main-nav overlay clearfix">\n            <a class="blog-logo" href="')
        __M_writer(str(blog_url))
        __M_writer('"><img src="')
        __M_writer(str(logo_url))
        __M_writer('" alt="Blog Logo" /></a>\n            <a class="menu-button" href="#"><span class="burger">&#9776;</span><span class="word">Menu</span></a>\n        </nav>\n        \n        <div class="vertical">\n            <div class="main-header-content inner">\n')
        if 'post_page' in pagekind:
            if post.meta('github'):
                __M_writer('                <a  href="')
                __M_writer(str(post.meta('github')))
                __M_writer('" target="_blank">\n                    <span class="icon-github" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if post.meta('twitter'):
                __M_writer('                <a class="bloglogo" href="')
                __M_writer(str(post.meta('twitter')))
                __M_writer('"" target="_blank">\n                    <span class="icon-twitter" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if post.meta('linkedin'):
                __M_writer('                <a  href="')
                __M_writer(str(post.meta('linkedin')))
                __M_writer('" target="_blank">\n                    <span class="icon-linkedin" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if post.meta('link'):
                __M_writer('                <a class="bloglogo" href="')
                __M_writer(str(post.meta('link')))
                __M_writer('"" target="_blank">\n                    <span class="icon-link" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
        else:
            if GITHUB_URL:
                __M_writer('                <a  href="')
                __M_writer(str(GITHUB_URL))
                __M_writer('" target="_blank">\n                    <span class="icon-github" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if TWITTER_URL:
                __M_writer('                <a class="bloglogo" href=')
                __M_writer(str(TWITTER_URL))
                __M_writer(' target="_blank">\n                    <span class="icon-twitter" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if LINKEDIN_URL:
                __M_writer('                <a  href="')
                __M_writer(str(LINKEDIN_URL))
                __M_writer('" target="_blank">\n                    <span class="icon-linkedin" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if GHOST_URL:
                __M_writer('                <a class="bloglogo" href=')
                __M_writer(str(GHOST_URL))
                __M_writer(' target="_blank">\n                    <span class="icon-ghost" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if HUGO_URL:
                __M_writer('                <a class="bloglogo" href=')
                __M_writer(str(HUGO_URL))
                __M_writer(' target="_blank">\n                    <span class="icon-hugo" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if WORKSHOP_URL:
                __M_writer('                <a class="bloglogo" href=')
                __M_writer(str(WORKSHOP_URL))
                __M_writer(' target="_blank">\n                    <span class="icon-link" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
        __M_writer('                <h1 class="page-title">')
        __M_writer(str(title))
        __M_writer('</h1>\n                <h2 class="page-description">')
        __M_writer(str(description))
        __M_writer('</h2>\n            </div>\n        </div>\n        <a class="scroll-down icon-arrow-left" href="#content"><span class="hidden">Scroll Down</span></a>\n        \n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 0, "69": 2, "70": 3, "71": 4, "72": 5, "73": 5, "74": 6, "75": 6, "80": 9, "81": 10, "82": 10, "83": 13, "84": 13, "89": 101, "94": 103, "95": 105, "96": 105, "97": 107, "98": 107, "103": 108, "104": 109, "105": 109, "106": 110, "107": 110, "113": 7, "123": 7, "129": 16, "152": 16, "153": 17, "154": 18, "155": 18, "156": 18, "157": 19, "158": 20, "159": 20, "160": 20, "161": 21, "162": 22, "163": 22, "164": 22, "165": 24, "166": 25, "167": 25, "168": 25, "169": 25, "170": 31, "171": 32, "172": 33, "173": 33, "174": 33, "175": 38, "176": 39, "177": 39, "178": 39, "179": 44, "180": 45, "181": 45, "182": 45, "183": 50, "184": 51, "185": 51, "186": 51, "187": 56, "188": 57, "189": 58, "190": 58, "191": 58, "192": 63, "193": 64, "194": 64, "195": 64, "196": 69, "197": 70, "198": 70, "199": 70, "200": 75, "201": 76, "202": 76, "203": 76, "204": 81, "205": 82, "206": 82, "207": 82, "208": 87, "209": 88, "210": 88, "211": 88, "212": 94, "213": 94, "214": 94, "215": 95, "216": 95, "222": 103, "237": 108, "252": 237}}
__M_END_METADATA
"""
