%global source0_hash 98417080e742829794584a794995c4a08900d22e11b879cb8cc240323b1f4a4a

%global framework sonnet

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 solution for spell checking

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  zlib-devel
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(libvoikko)

Requires:       kf5-filesystem >= %{majmin}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{version}-%{release}
	
 
%description
KDE Frameworks 5 Tier 1 solution for spell checking.

%package        core
Summary:        Non-gui part of the Sonnet framework
Recommends:	    %{name}-hunspell
%description    core
Non-gui part of the Sonnet framework provides low-level spell checking tools

%package        ui
Summary:        GUI part of the Sonnet framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    ui
GUI part of the Sonnet framework provides widgets with spell checking support.

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

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang_kf5 sonnet5_qt

%files
%doc README.md
%license LICENSES/*.txt

%files core
%{_kf5_libdir}/libKF5SonnetCore.so.*
%{_kf5_bindir}/parsetrigrams
%{_kf5_bindir}/gentrigrams
%{_kf5_qmldir}/org/kde/sonnet/
%{_kf5_datadir}/qlogging-categories5/*categories

%files ui -f sonnet5_qt.lang
%{_kf5_libdir}/libKF5SonnetUi.so.*

%files aspell
%dir %{_kf5_plugindir}/sonnet	
%{_kf5_plugindir}/sonnet/sonnet_aspell.so

%files hunspell
%dir %{_kf5_plugindir}/sonnet	
%{_kf5_plugindir}/sonnet/sonnet_hunspell.so
	
%files hspell
%dir %{_kf5_plugindir}/sonnet
%{_kf5_plugindir}/sonnet/sonnet_hspell.so

%files voikko
%dir %{_kf5_plugindir}/sonnet
%{_kf5_plugindir}/sonnet/sonnet_voikko.so

%files devel
%{_kf5_includedir}/Sonnet/
%{_kf5_includedir}/SonnetCore/
%{_kf5_includedir}/SonnetUi/
%{_kf5_libdir}/libKF5SonnetCore.so
%{_kf5_libdir}/libKF5SonnetUi.so
%{_kf5_libdir}/cmake/KF5Sonnet/
%{_kf5_archdatadir}/mkspecs/modules/qt_SonnetCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_SonnetUi.pri
%{_kf5_qtplugindir}/designer/sonnetui5widgets.so

%changelog
%autochangelog
