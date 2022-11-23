# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669218203.2405715
_enable_loop = True
_template_filename = 'themes/maupassant/templates/page.tmpl'
_template_uri = 'page.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


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

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        math = _mako_get_namespace(context, 'math')
        def content():
            return render_content(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\r\n    <div class="e-content entry-content" itemprop="articleBody text">\r\n    ')
        __M_writer(str(post.text()))
        __M_writer('\r\n    </div>\r\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('        <section class="comments">\r\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\r\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\r\n        </section>\r\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\r\n</article>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/page.tmpl", "uri": "page.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "51": 2, "52": 3, "53": 4, "54": 5, "55": 6, "60": 21, "66": 8, "78": 8, "79": 9, "80": 9, "81": 11, "82": 11, "83": 13, "84": 14, "85": 15, "86": 15, "87": 16, "88": 16, "89": 19, "90": 19, "91": 19, "97": 91}}
__M_END_METADATA
"""
