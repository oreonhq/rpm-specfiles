%global source0_hash ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: bzip2
Version: 1.0.8
Release: 1%{?dist}
Summary: bzip2/libbzip2, lossless block-sorting data compression
License: bzip2-1.0.6
URL: https://sourceware.org/bzip2/
Source0: https://sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This file is part of bzip2/libbzip2, a program and library for lossless, block-sorting data compression.

%package devel
Summary: bzip2/libbzip2, lossless block-sorting data compression
Requires: bzip2%{?_isa} = %{version}-%{release}
Provides: pkgconfig(bzip2)

%description devel
This file is part of bzip2/libbzip2, a program and library for lossless, block-sorting data compression.

%prep
%oreon_sha256
%autosetup -p1

%build
make -f Makefile-libbz2_so CC=gcc CFLAGS="%{_oreon_cflags} -fPIC"
make CC=gcc CFLAGS="%{_oreon_cflags}" bzip2 bzip2recover

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a bzip2 bzip2recover %{buildroot}%{_bindir}/
ln -sf bzip2 %{buildroot}%{_bindir}/bunzip2
ln -sf bzip2 %{buildroot}%{_bindir}/bzcat
cp -a libbz2.so.1.0.8 %{buildroot}%{_libdir}/
ln -sf libbz2.so.1.0.8 %{buildroot}%{_libdir}/libbz2.so.1.0
ln -sf libbz2.so.1.0 %{buildroot}%{_libdir}/libbz2.so
cp -a bzlib.h %{buildroot}%{_includedir}/
cp -a bzip2.1 %{buildroot}%{_mandir}/man1/
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bunzip2.1
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bzcat.1
ln -sf bzip2.1 %{buildroot}%{_mandir}/man1/bzip2recover.1
cat > %{buildroot}%{_libdir}/pkgconfig/bzip2.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: bzip2
Description: bzip2
Version: %{version}
Libs: -L\${libdir} -lbz2
Cflags: -I\${includedir}
EOF

%files
%license LICENSE
%{_bindir}/bzip2
%{_bindir}/bzip2recover
%{_bindir}/bunzip2
%{_bindir}/bzcat
%{_libdir}/libbz2.so.1.0
%{_libdir}/libbz2.so.1.0.8
%{_mandir}/man1/bzip2.1*
%{_mandir}/man1/bunzip2.1*
%{_mandir}/man1/bzcat.1*
%{_mandir}/man1/bzip2recover.1*

%files devel
%{_includedir}/bzlib.h
%{_libdir}/libbz2.so
%{_libdir}/pkgconfig/bzip2.pc
