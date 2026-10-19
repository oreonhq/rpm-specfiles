%global source1_hash 6d41d6559e6f7b2abdb73dc1d28252139a5be1068710d1ad92c84c01c71886d6
%global source0_hash 063ef80460f76d86dc4b033ef04b65b69ba82ee0de410440fe609465e7f5a997
%global framework	kdbusaddons
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:			kf6-%{framework}
Version:		6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:			https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:		kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		qt6-qtbase-devel
%description		devel
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
%find_lang_kf6 kdbusaddons6_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kdbusaddons-devel -f %{oreon_filedir}/kf6-kdbusaddons-devel.list

%changelog

%autochangelog
