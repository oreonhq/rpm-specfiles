%global source0_hash bfd6ef8d26fb269aea5b90177c5e8c772c829669415e2fa82dbbcf0b206c2f8d

Summary:        Library for generating random numbers using the RDRAND (read random) instruction
Name:           RdRand
Version:        2.1.6
Release:        6%{?dist}
License:        LGPL-2.0-or-later
URL:            https://github.com/jirka-h/%{name}
Source0:        https://github.com/jirka-h/%{name}/archive/%{version}.tar.gz
ExclusiveArch: %{ix86} x86_64
Requires:       openssl
BuildRequires: make libtool
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
%description
RdRand is an instruction for returning random numbers from an Intel on-chip
hardware random number generator.RdRand is available in Ivy Bridge and later
processors.

It uses cascade construction, combining a HW RNG operating at 3Gbps with CSPRNG
with all components sealed on CPU. The entropy source is a meta-stable circuit,
with unpredictable behavior based on thermal noise. The entropy is fed into
a 3:1 compression ratio entropy extractor (whitener) based on AES-CBC-MAC.
Online statistical tests are performed at this stage and only high quality
random data are used as the seed for cryptographically secure SP800-90 AES-CTR
DRBG compliant PRNG.
This generator is producing maximum of 512 128-bit AES blocks before it's
reseeded. According to documentation the 512 blocks is a upper limit for
reseed, in practice it reseeds much more frequently.

%package devel
Summary:        Development files for the RdRand
Requires:       %{name}%{?_isa} = %{version}-%{release}, openssl-devel

%description devel
Headers and shared object symbolic links for the RdRand.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
autoreconf -fi

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
rm -vf $RPM_BUILD_ROOT{%{_libdir}/librdrand.la,%{_libdir}/librdrand.a,%{_libdir}/librdrand/include/rdrandconfig.h}

%ldconfig_scriptlets

%files
%doc README COPYING ChangeLog NEWS
%{_bindir}/rdrand-gen
%{_mandir}/man7/rdrand-gen.7*
%{_libdir}/librdrand.so.*

%files devel
%{_mandir}/man3/librdrand.3*
%{_includedir}/librdrand.h
%{_includedir}/librdrand-aes.h
%{_libdir}/librdrand.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
