%global source0_hash ee5e457d4cfebe566f94b99e5e3d3cc7f5c79ddb741c2ac2ba2e456f00329644
Name:           djvulibre
Version:        3.5.30
Release:        1%{?dist}
Summary:        DjVu viewers, encoders, and libraries
License:        GPL-2.0-or-later
URL:            https://djvu.sourceforge.net/
Source0:        https://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
%description
DjVu is a web-centric document and image format. This package contains the
DjVuLibre tools and runtime libraries.

%package        libs
Summary:        Runtime libraries for DjVu
%description    libs
Shared libraries for DjVu rendering.

%package        devel
Summary:        Development files for djvulibre
Requires:       djvulibre-libs%{?_isa} = %{version}-%{release}
%description    devel
Headers and pkg-config data for building against djvulibre.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --disable-static \
  --enable-shared \
  --with-tiff
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n djvulibre-libs -f %{oreon_filedir}/djvulibre-libs.list
%files -n djvulibre-devel -f %{oreon_filedir}/djvulibre-devel.list

%changelog

%autochangelog
