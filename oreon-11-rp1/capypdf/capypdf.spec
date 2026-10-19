%global source0_hash b269a7361252b737f47b744f5329ba63f29af5bd3c46acbf7d4a4e074661f8a1
%global apiver 0
Name:           capypdf
Version:        0.21.0
Release:        1%{?dist}
Summary:        Fully color-managed PDF generation library
License:        Apache-2.0
URL:            https://github.com/jpakkane/capypdf
Source0:        https://github.com/jpakkane/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0001:      0001-Building-devtools-is-now-optional.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
# /oreon:deps
%description
This is a library for generating PDF files. It aims to be very low level.
It does not have its own document model, it merely exposes PDF primitives
directly.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the files for building applications that use
%{name}.

%package -n python3-%{name}
Summary:        Python 3 module for %{name}
BuildRequires:  python3-devel
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description -n python3-%{name}
This package provides the files for building applications that use
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%meson

%build

%meson_build
%install
%meson_install
%oreon_autofiles capypdf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-capypdf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n capypdf-devel -f %{oreon_filedir}/capypdf-devel.list
%files -n python3-capypdf -f %{oreon_filedir}/python3-capypdf.list

%changelog

%autochangelog
