%global source0_hash de1b4d4e745c0b7fc3e107b5155a51ac063011d33a5d82696331ecf4bed8d0fd

Name:           bwa
Version:        0.7.17
Release:        18%{?dist}
Summary:        Burrows-Wheeler Alignment tool

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2
# Fix building against GCC 10.
# https://github.com/lh3/bwa/commit/2a1ae7b6f34a96ea25be007ac9d91e57e9d32284
Patch0:         bwa-fix-build-gcc10.patch
# Enable non-x86_64 CPU architectures with simde.
# https://github.com/lh3/bwa/pull/283
Patch1:         bwa-simde.patch
BuildRequires:  gcc
BuildRequires:  perl-generators
%ifnarch x86_64
BuildRequires:  simde-devel
%endif
BuildRequires:  zlib-devel
BuildRequires: make

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
# Set -O3 for the better performance.
# https://github.com/lh3/bwa/pull/278
CFLAGS="%{optflags} -O3"
%ifnarch x86_64
# See Makefile in the pull request.
# https://github.com/lh3/bwa/pull/283
CFLAGS="${CFLAGS} -DUSE_SIMDE -DSIMDE_ENABLE_NATIVE_ALIASES -fopenmp-simd -DSIMDE_ENABLE_OPENMP"
%endif
%make_build CFLAGS="${CFLAGS}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/bwakit
mkdir -p %{buildroot}/%{_mandir}/man1

install -m 0755 bwa %{buildroot}/%{_bindir}
install -m 0755 qualfa2fq.pl %{buildroot}/%{_bindir}
install -m 0755 xa2multi.pl %{buildroot}/%{_bindir}
install -m 0755 bwakit/* %{buildroot}/%{_datadir}/%{name}/bwakit
install -m 0644 bwa.1 %{buildroot}/%{_mandir}/man1/bwa.1

%check
./bwa 2>&1 | grep '^Version: %{version}'

%files
%doc COPYING NEWS.md README.md README-alt.md
%{_bindir}/bwa
%{_bindir}/qualfa2fq.pl
%{_bindir}/xa2multi.pl
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
