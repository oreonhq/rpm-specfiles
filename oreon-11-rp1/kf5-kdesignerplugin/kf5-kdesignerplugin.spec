%global source0_hash e3cf4f848ae51d0489b977ccdb20dc3131d89a076783f336cda4e39e85ba735e

%global framework kdesignerplugin

# uncomment to enable bootstrap mode
#global bootstrap 1

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration module for Qt Designer

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static

# optional requirements
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kplotting-devel >= %{majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-sonnet-devel >= %{majmin}

Obsoletes: kf5-kdesignerplugin-devel < 5.18.0-2
Provides:  kf5-kdesignerplugin-devel = %{version}-%{release}

%description
This framework provides plugins for Qt Designer that allow it to display
the widgets provided by various KDE frameworks, as well as a utility
(kgendesignerplugin) that can be used to generate other such plugins
from ini-style description files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang_kf5 kdesignerplugin5_qt
# manpages
%find_lang %{name}-man --all-name --with-man --without-mo

cat kdesignerplugin5_qt.lang %{name}-man.lang > %{name}.lang

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license COPYING.LIB
%{_kf5_bindir}/kgendesignerplugin
#{_kf5_qtplugindir}/designer/kf5widgets.so
#dir %{_kf5_datadir}/kf5/widgets/
#{_kf5_datadir}/kf5/widgets/*
%{_kf5_mandir}/man1/kgendesignerplugin.1*
# runtime config, no need for -devel pkg
%{_kf5_libdir}/cmake/KF5DesignerPlugin/

%changelog
%autochangelog
