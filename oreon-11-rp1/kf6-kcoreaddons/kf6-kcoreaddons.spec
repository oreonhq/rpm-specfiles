%global source1_hash 35eb80ccf3f3e1fefe1a19971d86f839c04e01c898f9cb71c8f73d25f20395a8
%global source0_hash cc68fe15beb0fca2036cff8742f468c1345406bf99793fffacbf8f2a3f89bc4b
%global		framework kcoreaddons
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with various classes on top of QtCore
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MPL-1.1 AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6DBusTools)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlTools)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(mount)
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-pyside6-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  systemd-devel
# /oreon:deps
%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package -n python3-%{name}
Summary:    Qt for Python bindings for %{name}
%description -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
%description devel
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
%find_lang_kf6 kcoreaddons6_qt
%find_lang_kf6 kde6_xml_mimetypes
cat *.lang > all.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kf6-kcoreaddons -f %{oreon_filedir}/python3-kf6-kcoreaddons.list
%files -n kf6-kcoreaddons-devel -f %{oreon_filedir}/kf6-kcoreaddons-devel.list

%changelog

%autochangelog
