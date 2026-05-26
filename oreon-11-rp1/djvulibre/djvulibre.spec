# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 fcd009ea7654fde5a83600eb80757bd3a76998e47d13c66b54c8db849f8f2edc
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           djvulibre
Version:        3.5.28
Release:        2%{?dist}
Summary:        DjVu viewers, encoders, and libraries
License:        GPL-2.0-or-later
URL:            https://djvu.sourceforge.net/
Source0:        https://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(xt)

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
%oreon_verify_sources
%autosetup -p1


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


%files
%doc README* COPYRIGHT COPYING NEWS doc
%{_bindir}/*
%{_datadir}/djvu
%{_mandir}/man1/*.1*
%{_datadir}/icons/hicolor/*/mimetypes/*

%files libs
%{_libdir}/libdjvulibre.so.21*

%files devel
%{_includedir}/libdjvu/
%{_libdir}/libdjvulibre.so
%{_libdir}/pkgconfig/ddjvuapi.pc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.28-2
- Add DjVu stack for document viewers
