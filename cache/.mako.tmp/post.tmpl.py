# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669217898.9203196
_enable_loop = True
_template_filename = 'themes/maupassant/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="post post-page">\n    <h1 class="post-title">')
        __M_writer(filters.html_escape(str(post.title())))
        __M_writer('</h1>\n    <div class="post-content">\n        ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <div class="postpromonav">\n        <nav>\n            ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n            ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n        </nav>\n    </div>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('    <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n    </section>\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    <li>\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "53": 2, "54": 3, "55": 4, "56": 5, "61": 25, "66": 48, "71": 56, "77": 7, "86": 7, "87": 8, "88": 8, "89": 9, "90": 10, "91": 10, "92": 10, "93": 12, "94": 12, "95": 12, "96": 13, "97": 14, "98": 14, "99": 14, "100": 14, "101": 14, "102": 16, "103": 17, "104": 17, "105": 17, "106": 17, "107": 17, "108": 19, "109": 20, "110": 22, "111": 22, "112": 22, "113": 23, "114": 23, "115": 24, "116": 24, "122": 27, "133": 27, "134": 29, "135": 29, "136": 31, "137": 31, "138": 35, "139": 35, "140": 36, "141": 36, "142": 39, "143": 40, "144": 41, "145": 41, "146": 42, "147": 42, "148": 45, "149": 45, "150": 45, "151": 46, "152": 46, "158": 50, "167": 50, "168": 51, "169": 52, "170": 53, "171": 53, "172": 53, "173": 53, "179": 173}}
__M_END_METADATA
"""
