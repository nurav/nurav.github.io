# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462044391.476447
_enable_loop = True
_template_filename = '/home/vjoshi/envs/nikolaenv/lib64/python3.4/site-packages/nikola/data/themes/base/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def content():
            return render_content(context)
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul>\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('"><i class="icon-folder-open"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html"><i class="icon-file"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('    ')
            __M_writer(str(code))
            __M_writer('\n')
        if source_link:
            __M_writer('    <p class="sourceline"><a href="')
            __M_writer(str(source_link))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"72": 4, "73": 5, "74": 5, "75": 6, "76": 7, "77": 8, "78": 9, "79": 9, "80": 9, "81": 9, "82": 9, "83": 11, "84": 12, "85": 12, "86": 12, "23": 3, "88": 12, "89": 14, "90": 16, "91": 17, "92": 17, "29": 0, "94": 19, "95": 20, "96": 20, "97": 20, "98": 20, "99": 20, "105": 99, "45": 2, "46": 3, "93": 17, "51": 22, "57": 4, "87": 12}, "uri": "listing.tmpl", "source_encoding": "utf-8", "filename": "/home/vjoshi/envs/nikolaenv/lib64/python3.4/site-packages/nikola/data/themes/base/templates/listing.tmpl"}
__M_END_METADATA
"""
