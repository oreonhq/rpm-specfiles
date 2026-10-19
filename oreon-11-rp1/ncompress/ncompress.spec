%global source0_hash 96ec931d06ab827fccad377839bfb91955274568392ddecf809e443443aead46
Summary:        Fast compression and decompression utilities
Name: ncompress
Version: 5.0
Release:        1%{?dist}
License: Unlicense
URL: https://github.com/vapier/%{name}
Source0:        https://github.com/vapier/%{name}/archive/refs/tags/v%{version}.tar.gz#/ncompress-5.0.tar.gz
Patch0: ncompress-5.0-make.patch
Patch1: ncompress-5.0-lfs.patch
Patch3: ncompress-5.0-2GB.patch
Patch4: ncompress-5.0-endians.patch
Patch5: ncompress-5.0-memmove.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
# /oreon:deps
%description
The ncompress package contains the compress and uncompress file
compression and decompression utilities, which are compatible with the
original UNIX compress utility (.Z file extensions).  These utilities
can't handle gzipped (.gz file extensions) files, but gzip can handle
compressed files.

Install ncompress if you need compression/decompression utilities
which are compatible with the original UNIX compress utility.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%ifarch sparc m68k armv4l ppc s390 s390x ppc64 sparc64
ARCH_FLAGS="$ARCH_FLAGS -DBYTEORDER=1234"
%endif

%ifarch alpha ia64
ARCH_FLAGS="$ARCH_FLAGS -DNOALLIGN=0"
%endif

%autosetup -n %{name}-%{version} -p2

%build

make CFLAGS="%{optflags} %{?nc_endian} %{?nc_align} %{build_ldflags} -std=gnu17"
%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -p -m755 compress $RPM_BUILD_ROOT/%{_bindir}
ln -sf compress $RPM_BUILD_ROOT/%{_bindir}/uncompress
install -p -m644 compress.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -sf compress.1 $RPM_BUILD_ROOT%{_mandir}/man1/uncompress.1
%oreon_autofiles main

%check

./tests/runtests.sh
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-11
- Prepare for Oreon 11 (RP1)
