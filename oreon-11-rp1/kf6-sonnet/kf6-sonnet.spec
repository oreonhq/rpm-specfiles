%global source0_hash f8dcbba58d3479dfa4922146270f6ecb7ce0d987d82edc59b0c7c27ff965f65a

%global		framework sonnet

%global stable_kf6 stable
%global majmin_ver_kf6 6.27


Name:		kf6-%{framework}
Version:	6.27.0
Release:        1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 solution for spell checking
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# patch out default excluded file list to have it empty
# https://bugs.kde.org/show_bug.cgi?id=482376
Patch0:		sonnet6-default-list.patch

BuildRequires:	appstream
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(libvoikko)


Requires:	kf6-filesystem
Recommends:	%{name}-hunspell

%description
KDE Frameworks 6 Tier 1 solution for spell checking.


%package	aspell
Summary:	aspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	aspell
The %{name}-aspell package contains the aspell spellchecking
plugin for %{name}.

%package	hunspell
Summary:	hunspell plugin for %{name}
Requires:	%{name} = %{version}-%{release}
%description	hunspell
The %{name}-hunspell package contains the hunspell spellchecking
plugin for %{name}.

%package	hspell
Summary:	hspell plugin for %{name}
Supplements:	(%{name} and langpacks-he)
Requires:	%{name} = %{version}-%{release}
Requires:	hunspell-he

%description	hspell
The %{name}-hspell package contains the Hebrew hspell spellchecking
plugin for %{name}.

%package	voikko
Summary:	voikko plugin for %{name}
Supplements:	(%{name} and langpacks-fi)
Requires:	%{name} = %{version}-%{release}
%description	voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 sonnet6_qt

%files -f sonnet6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SonnetCore.so.*
%{_kf6_bindir}/parsetrigrams6
%{_kf6_qmldir}/org/kde/sonnet/
%{_kf6_libdir}/libKF6SonnetUi.so.*

%{_qt6_metatypesdir}/qt6kf6sonnetcore_metatypes.json
%files aspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_aspell.so

%files hunspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hunspell.so

%files hspell
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hspell.so

%files voikko
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_voikko.so


%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/cmake/KF6Sonnet/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_kf6_qtplugindir}/designer/sonnet6widgets.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

