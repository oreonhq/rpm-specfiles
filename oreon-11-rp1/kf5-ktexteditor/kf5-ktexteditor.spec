%global framework ktexteditor

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches (lookaside cache)

## upstreamable patches

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  kf5-sonnet-devel >= %{majmin}
BuildRequires:  kf5-syntax-highlighting-devel >= %{majmin}

BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)

BuildRequires:  pkgconfig(libgit2) >= 0.22.0

%if 0%{?fedora}
BuildRequires:  pkgconfig(editorconfig)
%endif

%if 0%{?tests}
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF5::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kparts-devel >= %{majmin}
Requires:       kf5-syntax-highlighting-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

%if %{with kf6_compat}
rm -rf %{buildroot}%{_kf5_datadir}/dbus-1/
rm -rf %{buildroot}%{_kf5_datadir}/polkit-1/
%endif

# create/own dirs
mkdir -p %{buildroot}%{_kf5_qtplugindir}/ktexteditor


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5TextEditor.so.*
%dir %{_kf5_plugindir}/parts/
%{_kf5_plugindir}/parts/katepart.so
%{_kf5_qtplugindir}/ktexteditor/
%{_kf5_datadir}/kservices5/katepart.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/katepart5/
%{_kf5_libexecdir}/kauth/kauth_ktexteditor_helper
%if %{without kf6_compat}
%{_kf5_datadir}/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
%{_kf5_datadir}/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
%{_kf5_datadir}/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
%endif

%files devel
%{_kf5_libdir}/libKF5TextEditor.so
%{_kf5_libdir}/cmake/KF5TextEditor/

%{_kf5_includedir}/KTextEditor/
%{_kf5_archdatadir}/mkspecs/modules/qt_KTextEditor.pri
#
%{_kf5_datadir}/kdevappwizard/templates/ktexteditor-plugin.tar.bz2


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
