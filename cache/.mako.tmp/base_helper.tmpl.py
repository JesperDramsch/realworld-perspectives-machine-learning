# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669217898.7142835
_enable_loop = True
_template_filename = 'themes/maupassant/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_navigation_links', 'html_feedlinks', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_title = context.get('blog_title', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        comment_system = context.get('comment_system', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <link href="/assets/css/theme.css" type="text/css" rel="stylesheet"/>\n    <link href="/assets/css/pure.css" type="text/css" rel="stylesheet"/>\n    <link href="/assets/css/style.css" type="text/css" rel="stylesheet"/>\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <li><a href="')
                __M_writer(str(permalink))
                __M_writer('" class="selected active current nav__item" >')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" class="nav__item">')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 74, "23": 99, "24": 110, "25": 120, "26": 143, "27": 151, "33": 3, "63": 3, "64": 7, "65": 8, "66": 9, "67": 10, "68": 12, "69": 13, "70": 15, "71": 16, "72": 18, "73": 21, "74": 22, "75": 25, "76": 25, "77": 25, "78": 28, "79": 29, "80": 29, "81": 29, "82": 31, "83": 32, "84": 32, "85": 32, "86": 34, "87": 35, "88": 36, "89": 36, "90": 36, "91": 37, "92": 38, "93": 38, "94": 38, "95": 38, "96": 38, "97": 40, "98": 41, "99": 41, "100": 42, "101": 42, "102": 43, "103": 44, "104": 46, "105": 46, "106": 46, "107": 47, "108": 47, "109": 49, "110": 50, "111": 51, "112": 51, "113": 51, "114": 51, "115": 51, "116": 51, "117": 51, "118": 54, "119": 55, "120": 56, "121": 56, "122": 56, "123": 58, "124": 59, "125": 60, "126": 60, "127": 60, "128": 62, "129": 63, "130": 63, "131": 63, "132": 65, "133": 66, "134": 66, "135": 67, "136": 68, "137": 69, "138": 70, "139": 70, "140": 70, "141": 72, "142": 73, "143": 73, "149": 76, "156": 76, "157": 77, "158": 78, "159": 79, "160": 83, "161": 84, "162": 86, "163": 87, "164": 88, "165": 90, "166": 91, "167": 96, "168": 98, "169": 98, "170": 98, "176": 102, "181": 102, "182": 106, "183": 107, "189": 112, "197": 112, "198": 113, "199": 114, "200": 115, "201": 115, "202": 115, "203": 115, "204": 115, "205": 116, "206": 117, "207": 117, "208": 117, "209": 117, "210": 117, "216": 122, "227": 122, "228": 123, "229": 124, "230": 124, "231": 124, "232": 125, "233": 126, "234": 127, "235": 128, "236": 128, "237": 128, "238": 128, "239": 128, "240": 130, "241": 131, "242": 131, "243": 131, "244": 134, "245": 135, "246": 136, "247": 137, "248": 137, "249": 137, "250": 137, "251": 137, "252": 139, "253": 140, "254": 140, "255": 140, "261": 145, "271": 145, "272": 146, "273": 147, "274": 148, "275": 148, "276": 148, "277": 148, "278": 148, "279": 148, "280": 148, "286": 280}}
__M_END_METADATA
"""
