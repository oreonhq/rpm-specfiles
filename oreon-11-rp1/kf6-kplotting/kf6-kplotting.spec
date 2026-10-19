%global source1_hash 61eb36e2d0147f667b7388f8c35ebb7b7cd53d4c78fd076af9803f3a935a417d
%global source0_hash f5a67be85c21665e052371301889443196b9de5b3927aff353a3d3e27730dd11
%undefine __cmake_in_source_build
%global framework kplotting
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for plotting
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter
# /oreon:deps
%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
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
%files -n kf6-kplotting-devel -f %{oreon_filedir}/kf6-kplotting-devel.list

%changelog

%autochangelog
