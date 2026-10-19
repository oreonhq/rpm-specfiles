%global source1_hash cfb450233e152714a476de06c5d6b8ebac7d2f8926566f85f48a4147bcc5a994
%global source0_hash dfbfc8af89b3bc68810b094bf87746db87c3eeb35b75caeb1882681ebed563bd
%global		framework ki18n
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        2%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for localization
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND ODbl-1.0
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:	iso-codes
Requires:	kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  python3
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 1 addon for localization.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	gettext
Requires:	python3
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
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-ki18n-devel -f %{oreon_filedir}/kf6-ki18n-devel.list

%changelog

%autochangelog
