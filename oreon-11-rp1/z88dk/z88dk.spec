%global source0_hash d4ada69e8db184b28711a718b82dbf9a7210db4aa9e33a41e2dc43258fd32f0f

%global nightly 20150709
%global _legacy_common_support 1

Name: z88dk
# We use post-release snapshot versioning, because the source code has no idea
# what version it is supposed to be. (README.1st still claims to be from version
# 1.9 when they already released 1.10 and 1.10.1.)
Version: 1.10.1
Release: 33%{?nightly:.%{nightly}cvs}%{?dist}
Summary: A Z80 cross compiler
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License: ClArtistic
URL: http://www.z88dk.org/
%if 0%{?nightly}
Source: http://nightly.z88dk.org/z88dk-%{nightly}.tgz
%else
Source: http://downloads.sourceforge.net/z88dk/z88dk-%{version}.tgz
%endif
Patch0: z88dk-1.10-makefile-usr-share.patch
Patch1: z88dk-1.10-64bit.patch
Patch2: z88dk-1.10-makefile-flags.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libxml2-devel
BuildRequires: perl-generators
# FIXME: sort out the file conflict (#823174)
Conflicts: z80asm

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
# Note: do not use %%{?_smp_mflags} with make because the Makefiles don't support parallel builds
make clean
make
# libs are target libraries, they won't build with host CFLAGS/LDFLAGS
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

%files
%doc doc/*.html doc/*.gif doc/copt.man
%doc doc/compile.txt doc/cpc.txt doc/embedded.txt doc/error.txt doc/farmods.txt
%doc doc/fileio.txt doc/lib3d.txt doc/options.txt doc/packages.txt
%doc doc/platforms.txt doc/retarget.txt doc/stdio.txt doc/ti.txt doc/z80asm.txt
%doc doc/zxscrdrv.txt
%doc EXTENSIONS LICENSE
# Examples might be worth putting in subpackage
%doc examples
%{_bindir}/appmake
%{_bindir}/asmpp.pl
%{_bindir}/copt
%{_bindir}/sccz80
%{_bindir}/z*
%{_datadir}/z88dk/
%{_mandir}/man3z/

%changelog
%autochangelog
