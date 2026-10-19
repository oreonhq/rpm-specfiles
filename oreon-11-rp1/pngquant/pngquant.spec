%global source0_hash ddd8889a9c269ba454d0c5e4f7167948d55d77c4570b23f671809fd3a68b6822
%global libname libimagequant
Name:           pngquant
Version:        3.0.3
Release:        1%{?dist}
Summary:        PNG quantization tool for reducing image file size
License:        GPL-3.0-or-later
%global _smp_build_ncpus 1
URL:            http://%{name}.org
Source0:        https://github.com/pornel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         pngquant-old_libpng.patch
Requires:       libpng%{?_isa} >= 1.2.46-1
Requires:       zlib%{?_isa} >= 1.2.3-1
Requires:       %{libname}%{?_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lcms2-devel
BuildRequires:  libimagequant-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{name} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha channel
preserved.  Such images are compatible with all modern web browsers and a
compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{name} uses the median cut algorithm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Relax version check for compatibility with newer libimagequant
sed -i 's/fgrep 2./grep -E "2|4."/' test/test.sh

%build

export CFLAGS="%{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC"
%configure --with-openmp --with-libimagequant
%make_build
%install
%make_install
%oreon_autofiles main

%check

%ifarch s390x
%make_build test || true
%else
%make_build test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
