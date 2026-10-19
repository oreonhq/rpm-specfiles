%global source0_hash 154ab23b60070e8f27013c22977f1129425d67d1e8acd6e13010e617811e4cff
%global processor_arch arm
%global target         %{processor_arch}-none-eabi
Name:           %{target}-binutils-cs
Epoch:          1
Version:        2.47
Release:        1%{?dist}
Summary:        GNU Binutils for cross-compilation for arm-none-eabi target
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            http://www.codesourcery.com/sgpp/lite/%{processor_arch}
Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz
Source1:        README.fedora
Patch1:         binutils-2.45-cve-2025-11081.patch
Patch2:         binutils-2.45-cve-2025-11082.patch
Patch3:         binutils-2.45-cve-2025-11083.patch
Provides:       %{target}-binutils = %{version}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cloog
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  ppl-devel
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  zlib-devel
# /oreon:deps
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

pushd libiberty
popd
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
rm    $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
