%global source0_hash eac0b0f11d35c5f49109e1cad8911ffb45407a469ec3d25e6cbde457c194baca
Name:           scamp
Version:        2.15.0
Release:        1%{?dist}
Summary:        compute astrometric and photometric solutions from sextractor catalogs
License:        GPL-3.0-only
URL:            http://www.astromatic.net/software/scamp
Source0:        https://github.com/astromatic/scamp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: wrong-pointer-i386.patch
Requires:       cdsclient
# oreon:deps
BuildRequires:  automake
BuildRequires:  cdsclient
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  plplot-devel
# /oreon:deps
%description
SCAMP is a program that computes astrometric and photometric solutions from
SExtractor catalogs

%prep
%oreon_prep
%build

sh autogen.sh
%configure --enable-openblas \
  --enable-plplot
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
