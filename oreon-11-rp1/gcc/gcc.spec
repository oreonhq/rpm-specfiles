%global source0_hash e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gcc
Version: 16.2.0
Release: 1%{?dist}
Summary: GNU Compiler Collection (GCC)
License: GPL-3.0-or-later WITH GCC-exception-3.1
URL: https://gcc.gnu.org/
Source0: https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: mpc-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: glibc-devel
BuildRequires: zlib-devel
BuildRequires: kernel-headers
%endif

%description
This directory contains the GNU Compiler Collection (GCC).

%prep
%oreon_sha256
%autosetup -p1

%build
# fortify flags break this build
unset CFLAGS CXXFLAGS LDFLAGS
mkdir -p %{_builddir}/gcc-build
cd %{_builddir}/gcc-build
%if %{with bootstrap} || 0%{?bootstrap}
%{_builddir}/gcc-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --enable-languages=c \
  --disable-shared \
  --disable-threads \
  --disable-libstdcxx \
  --without-headers \
  --with-newlib \
  --disable-bootstrap \
  --disable-multilib \
  --disable-nls \
  --disable-decimal-float \
  --disable-libgomp \
  --disable-libquadmath \
  --disable-libatomic \
  --disable-libssp \
  --disable-libvtv \
  --disable-libsanitizer \
  --disable-libitm
%else
%{_builddir}/gcc-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --mandir=%{_mandir} \
  --enable-languages=c,c++ \
  --enable-shared \
  --enable-threads=posix \
  --enable-default-pie \
  --with-system-zlib \
  --with-linker-hash-style=gnu \
  --disable-bootstrap \
  --disable-multilib \
  --disable-nls \
  --disable-libsanitizer
%endif
make -s -j%{?_smp_build_ncpus}

%install
cd %{_builddir}/gcc-build
make -s install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.py
find %{buildroot} -name '*.la' -delete

%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
