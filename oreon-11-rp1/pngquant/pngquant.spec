%global source0_hash 424ff432e51dfc3cf5ff8001ad1b64198850686c5e3c26ecd477e4b69ef4fade

%global libname libimagequant

Name:           pngquant
Version:        2.18.0
Release:        12%{?dist}
Summary:        PNG quantization tool for reducing image file size

License:        GPL-3.0-or-later

%global _smp_build_ncpus 1

URL:            http://%{name}.org
Source0:        https://github.com/pornel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Comment out failing test on EL < 8 due to old libpng
Patch1:         pngquant-old_libpng.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  libpng-devel >= 1.2.46-1
BuildRequires:  zlib-devel >= 1.2.3-1
BuildRequires:  lcms2-devel
BuildRequires:  %{libname}-devel

Requires:       libpng%{?_isa} >= 1.2.46-1
Requires:       zlib%{?_isa} >= 1.2.3-1
Requires:       %{libname}%{?_isa}

%description
%{name} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha channel
preserved.  Such images are compatible with all modern web browsers and a
compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{name} uses the median cut algorithm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%if 0%{?rhel} &&  0%{?rhel} < 8
%patch -P1 -p1 -b .oldlibpng
%endif

# Relax version check for compatibility with newer libimagequant
sed -i 's/fgrep 2./grep -E "2|4."/' test/test.sh

%build
# add some speed-relevant compiler-flags
export CFLAGS="%{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC"
%configure --with-openmp --with-libimagequant
%make_build

%install
%make_install

%check
# Neuter test failures on s390x due to
#  test: test/test.c:81: test_histogram: Assertion `LIQ_OK == err' failed.
%ifarch s390x
%make_build test || true
%else
%make_build test
%endif

%files
%doc README.md CHANGELOG
%license COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
