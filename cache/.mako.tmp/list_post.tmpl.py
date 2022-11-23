# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669217898.7587912
_enable_loop = True
_template_filename = 'themes/maupassant/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        def content():
            return render_content(context._locals(__M_locals))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        def content():
            return render_content(context)
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<div class="post-archive">\n    <header>\n        <h2>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h2>\n    </header>\n    ')
        __M_writer(str(archive_nav.archive_navigation()))
        __M_writer('\n')
        if posts:
            for post in posts:
                __M_writer('    <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/list_post.tmpl", "uri": "list_post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "42": 2, "43": 3, "48": 19, "54": 5, "66": 5, "67": 8, "68": 8, "69": 10, "70": 10, "71": 11, "72": 12, "73": 13, "74": 13, "75": 13, "76": 13, "77": 13, "78": 15, "79": 16, "80": 16, "81": 16, "82": 18, "88": 82}}
__M_END_METADATA
"""
