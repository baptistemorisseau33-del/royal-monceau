window.MF_I18N_APPLY = function (lists) {
  var I = window.MF_I18N || {};
  function n(t) { return (t || '').replace(/’/g, "'").trim(); }
  ['zh', 'ar', 'ru'].forEach(function (L) {
    var D = I[L]; if (!D) return;
    var S = {}; for (var k in (D.stops || {})) S[n(k)] = D.stops[k];
    function st(s) {
      if (!s || !s.fr || !s.en || s[L]) return;
      var x = S[n(s.fr.title)]; if (!x) return;
      var v = Object.assign({}, s.en, { title: x[0], kind: x[1], tease: x[2], teaseLook: x[3], hook: '', look: '' });
      if (x[5]) { v.short = x[4]; v.long = x[5]; v.body = x[4]; } else { v.body = x[4]; delete v.short; delete v.long; }
      s[L] = v;
    }
    lists.forEach(function (A) {
      (A || []).forEach(function (o) {
        if (!o) return;
        if (o.id && D.loops && D.loops[o.id] && !o[L]) o[L] = Object.assign({}, o.en, { title: D.loops[o.id][0], tagline: D.loops[o.id][1] });
        if (o.fr && o.fr.title && !o.stops) st(o);
        (o.stops || []).forEach(st); (o.extra || []).forEach(st);
      });
    });
  });
};
