%global source0_hash 0542382c7d1261eb02e2e15e4014c6332d39c75f17e72e59ec02b473b92df066
%global framework ktexteditor
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 with advanced embeddable text editor
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-sonnet-devel
BuildRequires:  kf5-syntax-highlighting-devel
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(libgit2)
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
mkdir -p %{buildroot}%{_kf5_qtplugindir}/ktexteditor
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-ktexteditor-devel -f %{oreon_filedir}/kf5-ktexteditor-devel.list

%changelog

%autochangelog
