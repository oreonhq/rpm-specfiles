%global source0_hash 154ab23b60070e8f27013c22977f1129425d67d1e8acd6e13010e617811e4cff
%define target avr
Name:           %{target}-binutils
Version:        2.47
Release:        1%{?dist}
Epoch:          1
Summary:        Cross Compiling GNU binutils targeted at avr
License:        GPL-2.0-or-later
URL:            http://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz
Source1:        README.fedora
Patch1: http://distribute.atmel.no/tools/opensource/avr-gcc/binutils-2.20.1/30-binutils-2.20.1-avr-size.patch
Patch2: avr-binutils-config.patch
Patch3:         binutils-2.45-cve-2025-11081.patch
Patch4:         binutils-2.45-cve-2025-11082.patch
Patch5:         binutils-2.45-cve-2025-11083.patch
Provides: bundled(libiberty)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  zlib-devel
# /oreon:deps
%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.

%prep

%setup -q -c
pushd binutils-%{version}
%patch -P1 -p2 -b .avr-size
%patch -P2 -p1 -b .config
%patch -P 3 -p1 -b .cve-2025-11081
%patch -P 4 -p1 -b .cve-2025-11082
%patch -P 5 -p1 -b .cve-2025-11083

# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
pushd libiberty
#autoconf -f
popd
#pushd intl
#autoconf -f
#popd

popd 
cp %{SOURCE1} .

%build

mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS" ../binutils-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --with-system-zlib \
  --target=%{target} --disable-werror --disable-nls
make %{?_smp_mflags}
popd
%check

cd build
%ifnarch s390x
make check
%endif
echo "completed"
%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
