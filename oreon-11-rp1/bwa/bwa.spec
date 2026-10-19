%global source0_hash de1b4d4e745c0b7fc3e107b5155a51ac063011d33a5d82696331ecf4bed8d0fd
Name:           bwa
Version:        0.7.17
Release:        18%{?dist}
Summary:        Burrows-Wheeler Alignment tool
License:        GPL-3.0-only
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2
Patch0:         bwa-fix-build-gcc10.patch
Patch1:         bwa-simde.patch
%ifnarch x86_64
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  simde-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

CFLAGS="%{optflags} -O3"
%ifnarch x86_64
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
%oreon_autofiles main

%check

./bwa 2>&1 | grep '^Version: %{version}'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
