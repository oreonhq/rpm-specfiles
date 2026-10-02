%global source0_hash 3c861fc762e045c8a02a1b8af265ecc63ec2d945f14b9ceaecfe0a342d97c3d9
%global source1_hash bdc1da4a033280ac752e7d34b0418efaa45bed093235cb88e62ea961752a37f8

#
# crash core analysis suite
#
Summary: Kernel analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
Name: crash
Version: 9.0.3
Release: 1%{?dist}
License: GPL-3.0-only
Source0:        https://github.com/crash-utility/crash/archive/refs/tags/%{version}.tar.gz#/crash-%{version}.tar.gz
Source1: https://mirrors.kernel.org/gnu/gdb/gdb-16.2.tar.gz
URL: https://crash-utility.github.io
ExclusiveOS: Linux
ExclusiveArch: %{ix86} ia64 x86_64 ppc ppc64 s390 s390x %{arm} aarch64 ppc64le riscv64
BuildRequires: ncurses-devel zlib-devel lzo-devel snappy-devel bison wget patch texinfo libzstd-devel
BuildRequires: make gcc gcc-c++
BuildRequires: gmp-devel mpfr-devel
Requires: binutils
Provides: bundled(libiberty)
Provides: bundled(gdb) = 16.2
Patch0: lzo_snappy_zstd.patch
Patch1: crash-9.0.1_build.patch

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%package devel
Requires: %{name} = %{version}, zlib-devel
Summary: kernel crash analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles

%description devel
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -n %{name}-%{version} -q
%patch 0 -p1 -b lzo_snappy_zstd.patch
%patch 1 -p1

%build

cp %{SOURCE1} .
make -j`nproc` RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%make_install
mkdir -p %{buildroot}%{_mandir}/man8
cp -p crash.8 %{buildroot}%{_mandir}/man8/crash.8
mkdir -p %{buildroot}%{_includedir}/crash
chmod 0644 defs.h
cp -p defs.h %{buildroot}%{_includedir}/crash

%files
%{_bindir}/crash
%{_mandir}/man8/crash.8*
%doc README COPYING3

%files devel
%{_includedir}/*

%changelog
%autochangelog
