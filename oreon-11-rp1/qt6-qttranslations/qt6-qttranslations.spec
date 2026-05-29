%global source0_hash none

%global qt_module qttranslations

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

Summary: Qt6 - QtTranslations module
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{qt_version}/submodules/qttranslations-everywhere-src-%{qt_version}.tar.xz
%endif

BuildArch: noarch

BuildRequires: cmake
BuildRequires: ninja-build
## versioning recently dropped, but could do >= %%majmin if needed --rex
BuildRequires: qt6-qtbase-devel
# for lrelease
BuildRequires: qt6-linguist
BuildRequires: qt6-qttools-devel

# help system-config-language and dnf/yum langpacks pull these in
%if 0%{?_qt6:1}
Provides: %{_qt6}-ar = %{version}-%{release}
Provides: %{_qt6}-ca = %{version}-%{release}
Provides: %{_qt6}-cs = %{version}-%{release}
Provides: %{_qt6}-da = %{version}-%{release}
Provides: %{_qt6}-de = %{version}-%{release}
Provides: %{_qt6}-es = %{version}-%{release}
Provides: %{_qt6}-fa = %{version}-%{release}
Provides: %{_qt6}-fi = %{version}-%{release}
Provides: %{_qt6}-fr = %{version}-%{release}
Provides: %{_qt6}-gl = %{version}-%{release}
Provides: %{_qt6}-gd = %{version}-%{release}
Provides: %{_qt6}-he = %{version}-%{release}
Provides: %{_qt6}-hu = %{version}-%{release}
Provides: %{_qt6}-hr = %{version}-%{release}
Provides: %{_qt6}-it = %{version}-%{release}
Provides: %{_qt6}-ja = %{version}-%{release}
Provides: %{_qt6}-ka = %{version}-%{release}
Provides: %{_qt6}-ko = %{version}-%{release}
Provides: %{_qt6}-lg = %{version}-%{release}
Provides: %{_qt6}-lt = %{version}-%{release}
Provides: %{_qt6}-lv = %{version}-%{release}
Provides: %{_qt6}-nl = %{version}-%{release}
Provides: %{_qt6}-nn = %{version}-%{release}
Provides: %{_qt6}-pl = %{version}-%{release}
Provides: %{_qt6}-pt_BR = %{version}-%{release}
Provides: %{_qt6}-pt_PT = %{version}-%{release}
Provides: %{_qt6}-ru = %{version}-%{release}
Provides: %{_qt6}-sk = %{version}-%{release}
Provides: %{_qt6}-sl = %{version}-%{release}
Provides: %{_qt6}-sv = %{version}-%{release}
Provides: %{_qt6}-uk = %{version}-%{release}
Provides: %{_qt6}-zh_CN = %{version}-%{release}
Provides: %{_qt6}-zh_TW = %{version}-%{release}
%endif

%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

# not used currently, since we track locales manually to keep %%files/Provides sync'd -- rex
#find_lang qttranslations --all-name --with-qt --without-mo

%files
%license LICENSES/*
%{_prefix}/lib64/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_datadir}/translations/catalogs.json
%lang(ar) %{_qt6_translationdir}/*_ar.qm
%lang(bg) %{_qt6_translationdir}/*_bg.qm
%lang(ca) %{_qt6_translationdir}/*_ca.qm
%lang(cs) %{_qt6_translationdir}/*_cs.qm
%lang(da) %{_qt6_translationdir}/*_da.qm
%lang(de) %{_qt6_translationdir}/*_de.qm
%lang(es) %{_qt6_translationdir}/*_es.qm
%lang(en) %{_qt6_translationdir}/*_en.qm
%lang(fa) %{_qt6_translationdir}/*_fa.qm
%lang(fi) %{_qt6_translationdir}/*_fi.qm
%lang(fr) %{_qt6_translationdir}/*_fr.qm
%lang(gd) %{_qt6_translationdir}/*_gd.qm
%lang(gl) %{_qt6_translationdir}/*_gl.qm
%lang(he) %{_qt6_translationdir}/*_he.qm
%lang(hu) %{_qt6_translationdir}/*_hu.qm
%lang(hr) %{_qt6_translationdir}/*_hr.qm
%lang(it) %{_qt6_translationdir}/*_it.qm
%lang(ja) %{_qt6_translationdir}/*_ja.qm
%lang(ka) %{_qt6_translationdir}/*_ka.qm
%lang(ko) %{_qt6_translationdir}/*_ko.qm
%lang(lg) %{_qt6_translationdir}/*_lg.qm
%lang(lt) %{_qt6_translationdir}/*_lt.qm
%lang(lv) %{_qt6_translationdir}/*_lv.qm
%lang(nl) %{_qt6_translationdir}/*_nl.qm
%lang(nn) %{_qt6_translationdir}/*_nn.qm
%lang(pl) %{_qt6_translationdir}/*_pl.qm
%lang(pt_BR) %{_qt6_translationdir}/*_pt_BR.qm
%lang(pt_PT) %{_qt6_translationdir}/*_pt_PT.qm
%lang(ru) %{_qt6_translationdir}/*_ru.qm
%lang(sk) %{_qt6_translationdir}/*_sk.qm
%lang(sl) %{_qt6_translationdir}/*_sl.qm
%lang(sv) %{_qt6_translationdir}/*_sv.qm
%lang(tr) %{_qt6_translationdir}/*_tr.qm
%lang(uk) %{_qt6_translationdir}/*_uk.qm
%lang(zh_CN) %{_qt6_translationdir}/*_zh_CN.qm
%lang(zh_TW) %{_qt6_translationdir}/*_zh_TW.qm


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
