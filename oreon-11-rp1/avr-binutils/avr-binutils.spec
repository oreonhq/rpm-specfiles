%global source0_hash none

%define target avr

Name:           %{target}-binutils
Version:        2.45
Release:        6%{?dist}
Epoch:          1
Summary:        Cross Compiling GNU binutils targeted at %{target}
License:        GPL-2.0-or-later
URL:            http://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz
Source1:        README.fedora
#add widespread options to avr-size: --format=avr -mcu=XX
Patch1: http://distribute.atmel.no/tools/opensource/avr-gcc/binutils-2.20.1/30-binutils-2.20.1-avr-size.patch
Patch2: avr-binutils-config.patch
# from upstream, for == 2.45, rhbz#2400335
Patch3:         binutils-2.45-cve-2025-11081.patch
# from upstream, for == 2.45, rhbz#2400340
Patch4:         binutils-2.45-cve-2025-11082.patch
# from upstream, for == 2.45, rhbz#2400336
Patch5:         binutils-2.45-cve-2025-11083.patch

BuildRequires:  gawk texinfo gcc
#for autoreconf:
BuildRequires:  gettext-devel automake
BuildRequires:  autoconf
BuildRequires: make zlib-devel
Provides: bundled(libiberty)

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
# these are for win targets only
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:

%files
%license binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz

%changelog
%autochangelog
