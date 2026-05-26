Summary: Fast compression and decompression utilities
Name: ncompress
Version: 5.0
Release: 11%{?dist}
License: Unlicense
URL: https://github.com/vapier/%{name}
Source: https://github.com/vapier/%{name}/archive/refs/tags/v%{version}.tar.gz

# allow to build ncompress
# ~> downstream
Patch0: ncompress-5.0-make.patch

# from dist-git commit 0539779d937
# (praiskup: removed redundant part as -DNOFUNCDEF is defined)
# ~> downstream
Patch1: ncompress-5.0-lfs.patch

# exit when too long filename is given (do not segfault)
# ~> #unknown
# ~> downstream
# Patch2: ncompress-4.2.4.4-filenamelen.patch
# Did not segfault, Prints error 'File name too long'

# permit files > 2GB to be compressed
# ~> #126775
Patch3: ncompress-5.0-2GB.patch

# do not fail to compress on ppc/s390x
# ~> #207001
Patch4: ncompress-5.0-endians.patch

# use memmove instead of memcpy
# ~> 760657
# ~> downstream
Patch5: ncompress-5.0-memmove.patch
# oreon url source checksums begin
%global source0_sha256 96ec931d06ab827fccad377839bfb91955274568392ddecf809e443443aead46
%global source0_file v5.0.tar.gz
# oreon url source checksums end

# silence gcc warnings
# ~> downstream
# Patch6: ncompress-4.2.4.4-silence-gcc.patch
# Fixed with %ld and brackets are included

BuildRequires: make
BuildRequires: gcc
BuildRequires: glibc-devel

%description
The ncompress package contains the compress and uncompress file
compression and decompression utilities, which are compatible with the
original UNIX compress utility (.Z file extensions).  These utilities
can't handle gzipped (.gz file extensions) files, but gzip can handle
compressed files.

Install ncompress if you need compression/decompression utilities
which are compatible with the original UNIX compress utility.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v5.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "96ec931d06ab827fccad377839bfb91955274568392ddecf809e443443aead46" || { echo "oreon: Source0 SHA256 mismatch for v5.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%check
./tests/runtests.sh


%files
%{_bindir}/compress
%{_bindir}/uncompress
%{_mandir}/man1/*
%doc LZW.INFO README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-11
- Prepare for Oreon 11 (RP1)
