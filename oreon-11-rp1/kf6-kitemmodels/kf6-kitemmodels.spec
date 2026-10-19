%global source1_hash ce46ec88fdca6fd4a04586562ca468403e480b85c484b60cba2d841d0a37e0c7
%global source0_hash f807e5b37aa913d2563ee1a21b2bce7d34495f32f38c7f35f16262d736bdfd55
%global		framework kitemmodels
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with item models
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:	kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Qml)
# /oreon:deps
%description
KDE Frameworks 6 Tier 1 addon with item models.

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kitemmodels-devel -f %{oreon_filedir}/kf6-kitemmodels-devel.list

%changelog

%autochangelog
