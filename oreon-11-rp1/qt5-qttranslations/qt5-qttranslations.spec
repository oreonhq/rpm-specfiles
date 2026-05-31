%global source0_hash none

%global qt_module qttranslations

Summary: Qt5 - QtTranslations module
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
BuildArch: noarch

%global _qt5_qmake %{_bindir}/qmake-qt5

## versioning recently dropped, but could do >= %%majmin if needed --rex
BuildRequires: make
BuildRequires: qt5-qtbase-devel
# for lrelease
BuildRequires: qt5-linguist

# help system-config-language and dnf/yum langpacks pull these in
%if 0%{?_qt5:1}
Provides: %{_qt5}-ar = %{version}-%{release}
Provides: %{_qt5}-ca = %{version}-%{release}
Provides: %{_qt5}-cs = %{version}-%{release}
Provides: %{_qt5}-da = %{version}-%{release}
Provides: %{_qt5}-de = %{version}-%{release}
Provides: %{_qt5}-es = %{version}-%{release}
Provides: %{_qt5}-fa = %{version}-%{release}
Provides: %{_qt5}-fi = %{version}-%{release}
Provides: %{_qt5}-fr = %{version}-%{release}
Provides: %{_qt5}-gl = %{version}-%{release}
Provides: %{_qt5}-gd = %{version}-%{release}
Provides: %{_qt5}-he = %{version}-%{release}
Provides: %{_qt5}-hu = %{version}-%{release}
Provides: %{_qt5}-hr = %{version}-%{release}
Provides: %{_qt5}-it = %{version}-%{release}
Provides: %{_qt5}-ja = %{version}-%{release}
Provides: %{_qt5}-ko = %{version}-%{release}
Provides: %{_qt5}-lt = %{version}-%{release}
Provides: %{_qt5}-lv = %{version}-%{release}
Provides: %{_qt5}-nl = %{version}-%{release}
Provides: %{_qt5}-nn = %{version}-%{release}
Provides: %{_qt5}-pl = %{version}-%{release}
Provides: %{_qt5}-pt = %{version}-%{release}
Provides: %{_qt5}-pt_BR = %{version}-%{release}
Provides: %{_qt5}-ru = %{version}-%{release}
Provides: %{_qt5}-sk = %{version}-%{release}
Provides: %{_qt5}-sl = %{version}-%{release}
Provides: %{_qt5}-sv = %{version}-%{release}
Provides: %{_qt5}-uk = %{version}-%{release}
Provides: %{_qt5}-zh_CN = %{version}-%{release}
Provides: %{_qt5}-zh_TW = %{version}-%{release}
%endif

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# not used currently, since we track locales manually to keep %%files/Provides sync'd -- rex
#find_lang qttranslations --all-name --with-qt --without-mo


%files
%license LICENSE.*
%lang(ar) %{_qt5_translationdir}/*_ar.qm
%lang(bg) %{_qt5_translationdir}/*_bg.qm
%lang(ca) %{_qt5_translationdir}/*_ca.qm
%lang(cs) %{_qt5_translationdir}/*_cs.qm
%lang(da) %{_qt5_translationdir}/*_da.qm
%lang(de) %{_qt5_translationdir}/*_de.qm
%lang(es) %{_qt5_translationdir}/*_es.qm
%lang(en) %{_qt5_translationdir}/*_en.qm
%lang(fa) %{_qt5_translationdir}/*_fa.qm
%lang(fi) %{_qt5_translationdir}/*_fi.qm
%lang(fr) %{_qt5_translationdir}/*_fr.qm
%lang(gd) %{_qt5_translationdir}/*_gd.qm
%lang(gl) %{_qt5_translationdir}/*_gl.qm
%lang(he) %{_qt5_translationdir}/*_he.qm
%lang(hu) %{_qt5_translationdir}/*_hu.qm
%lang(hr) %{_qt5_translationdir}/*_hr.qm
%lang(it) %{_qt5_translationdir}/*_it.qm
%lang(ja) %{_qt5_translationdir}/*_ja.qm
%lang(ko) %{_qt5_translationdir}/*_ko.qm
%lang(lt) %{_qt5_translationdir}/*_lt.qm
%lang(lv) %{_qt5_translationdir}/*_lv.qm
%lang(nn) %{_qt5_translationdir}/*_nn.qm
%lang(nl) %{_qt5_translationdir}/*_nl.qm
%lang(pl) %{_qt5_translationdir}/*_pl.qm
%lang(pt) %{_qt5_translationdir}/*_pt_PT.qm
%lang(pt_BR) %{_qt5_translationdir}/*_pt_BR.qm
%lang(ru) %{_qt5_translationdir}/*_ru.qm
%lang(sk) %{_qt5_translationdir}/*_sk.qm
%lang(sl) %{_qt5_translationdir}/*_sl.qm
%lang(sv) %{_qt5_translationdir}/*_sv.qm
%lang(tr) %{_qt5_translationdir}/*_tr.qm
%lang(uk) %{_qt5_translationdir}/*_uk.qm
%lang(zh_CN) %{_qt5_translationdir}/*_zh_CN.qm
%lang(zh_TW) %{_qt5_translationdir}/*_zh_TW.qm


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
