CodeMirrorConfig.stylesheet = "/media/python_field/css/pythoncolors.css";
CodeMirrorConfig.path = "/media/python_field/js/";
CodeMirrorConfig.parserfile = "parsepython.js";
CodeMirrorConfig.height = "dynamic";
CodeMirrorConfig.indentUnit = 4;
CodeMirrorConfig.lineNumbers = true;

var convert_to_CodeMirror = function(obj){
    // alert(obj);
    var id = $(obj).attr('id');
    if (!id.match(/__prefix__/)) {
        // alert(id);
        var editor = CodeMirror.fromTextArea(id);
    }
};

$(document).ready(function(){
    $('.python-code').each(function(i,obj){
        convert_to_CodeMirror($(obj));
    });
});
