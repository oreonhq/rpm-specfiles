%global source0_hash 85db5b58c56d16d2cf71fc79078650d1b5c7fbf5305f38fb17fee97016017236faaca29a2495ed52d270a5f2a1fefe6bfee623dea75e9c29bd3fbf96b088f0fb
%global source1_hash 65e14cfa366660dc409ac9a2853da534f262a08bf0d279b507a48feba6df88968bbe113117d1e1adc2e49efff3996f1204f19ceb882a842eef5520418d3ab2b4

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-luatexja
Epoch:          12
Version:        svn79037
Release:        1%{?dist}
Summary:        Typeset Japanese with LuaTeX
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexja.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/luatexja.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-luatexja-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-luatexja-doc <= 11:%{version}
Provides:       tex(lltjcore.sty)
Provides:       tex(lltjdefs.sty)
Provides:       tex(lltjext-251101.sty)
Provides:       tex(lltjext.sty)
Provides:       tex(lltjfont.sty)
Provides:       tex(lltjp-array.sty)
Provides:       tex(lltjp-atbegshi.sty)
Provides:       tex(lltjp-collcell.sty)
Provides:       tex(lltjp-everyshi.sty)
Provides:       tex(lltjp-fancyvrb.sty)
Provides:       tex(lltjp-fontspec.sty)
Provides:       tex(lltjp-footmisc.sty)
Provides:       tex(lltjp-geometry.sty)
Provides:       tex(lltjp-listings.sty)
Provides:       tex(lltjp-microtype.sty)
Provides:       tex(lltjp-preview.sty)
Provides:       tex(lltjp-siunitx.sty)
Provides:       tex(lltjp-stfloats.sty)
Provides:       tex(lltjp-tascmac.sty)
Provides:       tex(lltjp-unicode-math.sty)
Provides:       tex(lltjp-xunicode.sty)
Provides:       tex(ltj-base.sty)
Provides:       tex(ltj-latex.sty)
Provides:       tex(ltj-plain.sty)
Provides:       tex(luatexja-adjust.sty)
Provides:       tex(luatexja-ajmacros.sty)
Provides:       tex(luatexja-compat.sty)
Provides:       tex(luatexja-core.sty)
Provides:       tex(luatexja-fontspec-29e.sty)
Provides:       tex(luatexja-fontspec.sty)
Provides:       tex(luatexja-otf.sty)
Provides:       tex(luatexja-preset.sty)
Provides:       tex(luatexja-ruby.sty)
Provides:       tex(luatexja-zhfonts.sty)
Provides:       tex(luatexja.sty)
Provides:       tex(ltjbk10.clo)
Provides:       tex(ltjbk11.clo)
Provides:       tex(ltjbk12.clo)
Provides:       tex(ltjsize10.clo)
Provides:       tex(ltjsize11.clo)
Provides:       tex(ltjsize12.clo)
Provides:       tex(ltjtbk10.clo)
Provides:       tex(ltjtbk11.clo)
Provides:       tex(ltjtbk12.clo)
Provides:       tex(ltjtsize10.clo)
Provides:       tex(ltjtsize11.clo)
Provides:       tex(ltjtsize12.clo)
Provides:       tex(jfm-CCT.lua)
Provides:       tex(jfm-banjiao.lua)
Provides:       tex(jfm-jis.lua)
Provides:       tex(jfm-kaiming.lua)
Provides:       tex(jfm-min.lua)
Provides:       tex(jfm-mono.lua)
Provides:       tex(jfm-prop.lua)
Provides:       tex(jfm-propv.lua)
Provides:       tex(jfm-propw.lua)
Provides:       tex(jfm-quanjiao.lua)
Provides:       tex(jfm-tmin.lua)
Provides:       tex(jfm-ujis.lua)
Provides:       tex(jfm-ujisv.lua)
Provides:       tex(ltj-adjust.lua)
Provides:       tex(ltj-base.lua)
Provides:       tex(ltj-charrange.lua)
Provides:       tex(ltj-compat.lua)
Provides:       tex(ltj-debug.lua)
Provides:       tex(ltj-direction-20251230.lua)
Provides:       tex(ltj-direction.lua)
Provides:       tex(ltj-inputbuf.lua)
Provides:       tex(ltj-ivd_aj1.lua)
Provides:       tex(ltj-jfmglue.lua)
Provides:       tex(ltj-jfont-20251230.lua)
Provides:       tex(ltj-jfont.lua)
Provides:       tex(ltj-jisx0208.lua)
Provides:       tex(ltj-lineskip.lua)
Provides:       tex(ltj-lotf_aux.lua)
Provides:       tex(ltj-math.lua)
Provides:       tex(ltj-otf.lua)
Provides:       tex(ltj-pretreat.lua)
Provides:       tex(ltj-rmlgbm.lua)
Provides:       tex(ltj-ruby.lua)
Provides:       tex(ltj-setwidth-20251230.lua)
Provides:       tex(ltj-setwidth.lua)
Provides:       tex(ltj-stack.lua)
Provides:       tex(ltj-unicode-ccfix.lua)
Provides:       tex(luatexja.lua)
Provides:       tex(ltj-kinsoku.tex)

%description
Typeset Japanese with LuaTeX.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%doc %{_texmf_main}/doc/luatex/luatexja/
%{_texmf_main}/tex/luatex/luatexja/

%changelog
%autochangelog
