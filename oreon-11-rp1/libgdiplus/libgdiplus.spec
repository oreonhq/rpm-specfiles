%global source0_hash 683adb7d99d03f6ee7985173a206a2243f76632682334ced4cae2fcd20c83bc9
%undefine _hardened_build
Name:           libgdiplus
Version:        6.2
Release:        3%{?dist}
Summary:        An Open Source implementation of the GDI+ API
License:        MIT
URL:            https://gitlab.winehq.org/mono/libgdiplus
Source0:        https://dl.winehq.org/mono/sources/libgdiplus/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glib2-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
An Open Source implementation of the GDI+ API, it is part of the Mono 
Project

%package devel
Summary: Development files for libgdiplus
Requires: %{name} = %{version}-%{release}
%description devel
Development files for libgdiplus

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

CFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"

export CFLAGS
export CXXFLAGS

%build

%configure --disable-static --with-pango
make %{?_smp_mflags}
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgdiplus-devel -f %{oreon_filedir}/libgdiplus-devel.list

%changelog

%autochangelog
