%global source0_hash none

%global processor_arch arm
%global target         %{processor_arch}-none-eabi

Name:           %{target}-binutils-cs
Epoch:          1
Version:        2.45
Release:        3%{?dist}
Summary:        GNU Binutils for cross-compilation for %{target} target
# Most of the sources are licensed under GPLv3+ with these exceptions:
# LGPLv2+ bfd/hosts/x86-64linux.h, include/demangle.h, include/xregex2.h,
# GPLv2+  gprof/cg_print.h
# BSD     gprof/cg_arcs.h, gprof/utils.c, ld/elf-hints-local.h,
# Public Domain libiberty/memmove.c
# Automatically converted from old format: GPLv2+ and GPLv3+ and LGPLv2+ and BSD - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            http://www.codesourcery.com/sgpp/lite/%{processor_arch}

Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz

Source1:        README.fedora
# 3x from upstream for == 2.45
Patch1:         binutils-2.45-cve-2025-11081.patch
Patch2:         binutils-2.45-cve-2025-11082.patch
Patch3:         binutils-2.45-cve-2025-11083.patch
BuildRequires:  gcc flex bison ppl-devel cloog
BuildRequires:  autoconf
BuildRequires:  texinfo texinfo-tex perl-podlators
BuildRequires:  make zlib-devel
Provides:       %{target}-binutils = %{version}

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# ppl-devel is no longer available for 32bit, so we have to skip it too
ExcludeArch:    %{ix86}
%endif

%description
This is a cross-compilation version of GNU Binutils, which can be used to
assemble and link binaries for the %{target} platform.  

Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%prep
%autosetup -p1 -n binutils-%{version}
cp -p %{SOURCE1} .
rm -rf gdb sim

%build
# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
pushd libiberty
#autoconf -f
popd
%if 0%{?fedora} || 0%{?rhel} > 8
[ %{_lto_cflags}x != x ] && %{_fix_broken_configure_for_lto}
%endif

./configure CFLAGS="$RPM_OPT_FLAGS" \
            --target=%{target} \
            --enable-interwork \
            --enable-multilib \
            --enable-plugins \
            --disable-nls \
            --disable-shared \
            --disable-threads \
            --with-gcc --with-gnu-as --with-gnu-ld \
            --with-system-zlib \
            --prefix=%{_prefix} \
            --libdir=%{_libdir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            --with-docdir=share/doc/%{name} \
            --disable-werror \
            --with-pkgversion="Fedora %{version}-%{release}" \
            --with-bugurl="https://bugzilla.redhat.com/"
make %{?_smp_mflags}

%check
%ifnarch s390x
make check
%endif
echo "completed"

%install
make install DESTDIR=$RPM_BUILD_ROOT
# these are for win targets only
rm    $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:

%files
%license COPYING*
%doc ChangeLog README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz

%changelog
%autochangelog
