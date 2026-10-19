%global source0_hash a7ced37f4102b745ac86d6a70a9da399cc139ff168ba6b8002b4d8d43c900c15
%{?mingw_package_header}
Name:           mingw-libepoxy
Version:        1.5.10
Release:        10%{?dist}
Summary:        MinGW Windows libepoxy library
License:        MIT
URL:            https://github.com/anholt/libepoxy
Source0:        https://github.com/anholt/libepoxy/releases/download/%{version}/libepoxy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  mingw32-angleproject
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  python3
# /oreon:deps
%description
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.

%package -n mingw32-libepoxy
Summary:        MinGW Windows libepoxy library
Requires:       mingw32-angleproject
%description -n mingw32-libepoxy
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.

%package -n mingw64-libepoxy
Summary:        MinGW Windows libepoxy library
Requires:       mingw64-angleproject
%description -n mingw64-libepoxy
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libepoxy-%{version}
%oreon_prep
%build

%mingw_meson -Degl=yes
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-libepoxy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libepoxy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libepoxy -f %{oreon_filedir}/mingw32-libepoxy.list
%files -n mingw64-libepoxy -f %{oreon_filedir}/mingw64-libepoxy.list

%changelog

%autochangelog
