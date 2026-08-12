%global source0_hash 96c985837152efdd216a93790703823877fdea43a1b9d3a5197a9b94c264be4f

%global framework kross

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for multi-language application scripting

License: LGPL-2.1-or-later AND CC0-1.0
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-static

Requires:       %{name}-core%{_isa} = %{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{version}-%{release}

%description
Kross is a scripting bridge to embed scripting functionality into an
application. It supports QtScript as a scripting interpreter backend.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel >= %{majmin}
Requires:       kf5-kiconthemes-devel >= %{majmin}
Requires:       kf5-kio-devel >= %{majmin}
Requires:       kf5-kparts-devel >= %{majmin}
Requires:       kf5-kwidgetsaddons-devel >= %{majmin}
Requires:       qt5-qtbase-devel
Requires:       qt5-qtscript-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core
Summary:        Non-gui part of the Kross framework
%description    core
Non-gui part of the Kross framework.

%package        ui
Summary:        Gui part of the Kross framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    ui
Gui part of the Kross framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man

%files
# empty

%ldconfig_scriptlets core

%files core -f %{name}.lang
%{_kf5_bindir}/kf5kross
%{_kf5_mandir}/man1/kf5kross.1*
%{_kf5_libdir}/libKF5KrossCore.so.*
%{_kf5_qtplugindir}/krossqts.so
%{_kf5_qtplugindir}/script/krossqtsplugin.so

%ldconfig_scriptlets ui

%files ui
%{_kf5_libdir}/libKF5KrossUi.so.*
%{_kf5_qtplugindir}/krossmoduleforms.so
%{_kf5_qtplugindir}/krossmodulekdetranslation.so

%files devel
%{_kf5_includedir}/kross_version.h
%{_kf5_includedir}/KrossUi/
%{_kf5_includedir}/KrossCore/
%{_kf5_libdir}/libKF5KrossCore.so
%{_kf5_libdir}/libKF5KrossUi.so
%{_kf5_libdir}/cmake/KF5Kross/
%{_kf5_archdatadir}/mkspecs/modules/qt_KrossCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KrossUi.pri

%changelog
%autochangelog
