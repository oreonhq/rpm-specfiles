%global source0_hash d4ada69e8db184b28711a718b82dbf9a7210db4aa9e33a41e2dc43258fd32f0f
%global nightly 20150709
%global _legacy_common_support 1
Name: z88dk
Version: 1.10.1
Release:        1%{?dist}
Summary:        A Z80 cross compiler
License: ClArtistic
URL: http://www.z88dk.org/
%if 0%{?nightly}
Source0:        http://nightly.%{name}.org/%{name}-%{nightly}.tgz
%else
%endif
Patch0: z88dk-1.10-makefile-usr-share.patch
Patch1: z88dk-1.10-64bit.patch
Patch2: z88dk-1.10-makefile-flags.patch
Conflicts: z80asm
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
z88dk is a Z80 cross compiler capable of generating binary files for a variety
of Z80 based machines (such as the ZX81, Spectrum, Jupiter Ace and some TI
calculators).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n z88dk
# Put files in %%{_datadir}/z88dk rather than /usr/lib/z88dk
# Also support DESTDIR in install-libs
%patch -P0 -p1
# 64-bit fixes
%patch -P1 -p1
# Fix improper use of CFLAGS and LDFLAGS in the makefiles
%patch -P2 -p1
find . -depth -name CVS -type d -exec rm -rf {} \;
# Separate manpages from other docs and fix their permissions
mv doc/netman .
chmod 644 netman/man3z/*
# Fix files with wrong line endings and bad permissions
find doc examples src -type f -exec sed -i -e 's/\r*$//' {} \;
find doc examples src -type f -exec chmod 644 {} \;

%build

export Z80_OZFILES=%{_builddir}/z88dk/lib/
export ZCCCFG=%{_builddir}/z88dk/lib/config/
export PATH=%{_builddir}/z88dk/bin:$PATH
%global build_type_safety_c 0
export CC="gcc -std=gnu89"
export CFLAGS="%{optflags}"
%{?__global_ldflags:export LDFLAGS="%{__global_ldflags}"}
make clean
make
unset CFLAGS
export CFLAGS
unset LDFLAGS
export LDFLAGS
make libs
%install
export Z80_OZFILES=%{_datadir}/z88dk-%{version}/lib/
export ZCCCFG=%{_datadir}/z88dk-%{version}/lib/config/
make install install-libs DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man3z
cp -p netman/man3z/* %{buildroot}%{_mandir}/man3z
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
