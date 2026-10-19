%global source1_hash 7f6ee75980fe3c06a26bfc51e8c1c412606385641d18d2e3d1a06fdbbe0ce64c
%global source0_hash 2cdb0a2689ab45b907c76c9a01c1dc14855b8e5329ad0a9cf65c1ad64e5fed1b
%define framework prison
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Summary:        KDE Frameworks 6 Tier 1 barcode library
Version:	6.30.0
Release:        1%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:	kf6-filesystem
Requires:	qrencode-libs%{?_isa}
Requires:	libdmtx%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(ZXing)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)
# /oreon:deps
%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
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
%files -n kf6-prison-devel -f %{oreon_filedir}/kf6-prison-devel.list

%changelog

%autochangelog
