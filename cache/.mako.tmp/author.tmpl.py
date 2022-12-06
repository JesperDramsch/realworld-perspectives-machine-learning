# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1670341554.713416
_enable_loop = True
_template_filename = 'themes/canterville/templates/author.tmpl'
_template_uri = 'author.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'cover', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def cover():
            return render_cover(context._locals(__M_locals))
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        AUTHOR_DETAILS = _import_ns.get('AUTHOR_DETAILS', context.get('AUTHOR_DETAILS', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'cover'):
            context['self'].cover(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(author, kind, rss_override=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_cover(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        AUTHOR_DETAILS = _import_ns.get('AUTHOR_DETAILS', context.get('AUTHOR_DETAILS', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        def cover():
            return render_cover(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
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
        __M_writer('" alt="Blog Logo" /></a>\n            <a class="menu-button" href="#"><span class="burger">&#9776;</span><span class="word">Menu</span></a>\n        </nav>\n        \n        <div class="vertical">\n            <div class="main-header-content inner">\n            \n')
        for service in ['github', 'linkedin', 'twitter', 'link']:
            if service in AUTHOR_DETAILS.get(author, {}):
                __M_writer('                <a  href="')
                __M_writer(str(AUTHOR_DETAILS[author][service]))
                __M_writer('" target="_blank">\n                    <span class="icon-')
                __M_writer(str(service))
                __M_writer('" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
        __M_writer('                <h1 class="page-title">')
        __M_writer(str(title.replace("Posts", "Talks")))
        __M_writer('</h1>\n                \n            </div>\n        </div>\n        <a class="scroll-down icon-arrow-left" href="#content"><span class="hidden">Scroll Down</span></a>\n        \n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        AUTHOR_DETAILS = _import_ns.get('AUTHOR_DETAILS', context.get('AUTHOR_DETAILS', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        author = _import_ns.get('author', context.get('author', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="authorpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title.replace("Posts","Talks"))))
        __M_writer('</h1>\n')
        if 'image' in AUTHOR_DETAILS.get(author, {}):
            __M_writer('        <img src="')
            __M_writer(str(AUTHOR_DETAILS[author]['image']))
            __M_writer('" alt="')
            __M_writer(str(author))
            __M_writer('" />\n')
        if description:
            __M_writer('            <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        __M_writer('        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(author, kind)))
        __M_writer('\n        </div>\n    </header>\n    <h2>Talks</h2>\n')
        if posts:
            __M_writer('        <ul class="postlist">\n')
            for post in posts:
                __M_writer('                <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/author.tmpl", "uri": "author.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "54": 2, "55": 3, "60": 7, "65": 40, "70": 65, "76": 5, "87": 5, "88": 6, "89": 6, "95": 9, "111": 9, "112": 10, "113": 11, "114": 11, "115": 11, "116": 12, "117": 13, "118": 13, "119": 13, "120": 14, "121": 15, "122": 15, "123": 15, "124": 17, "125": 18, "126": 18, "127": 18, "128": 18, "129": 25, "130": 26, "131": 27, "132": 27, "133": 27, "134": 28, "135": 28, "136": 33, "137": 33, "138": 33, "144": 42, "160": 42, "161": 45, "162": 45, "163": 46, "164": 47, "165": 47, "166": 47, "167": 47, "168": 47, "169": 49, "170": 50, "171": 50, "172": 50, "173": 52, "174": 53, "175": 53, "176": 57, "177": 58, "178": 59, "179": 60, "180": 60, "181": 60, "182": 60, "183": 60, "184": 60, "185": 60, "186": 60, "187": 60, "188": 60, "189": 60, "190": 62, "191": 64, "197": 191}}
__M_END_METADATA
"""
