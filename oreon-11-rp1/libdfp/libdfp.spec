%global source0_hash 9fb50eb15a5d775d4b89598c66e48d6058232faf1bcf040922a291fa63aa8429
Name:		libdfp
Version:	1.0.17
Release:        2%{?dist}
Summary:        Decimal Floating Point C Library
License:	LGPL-2.1-or-later
Url:		https://github.com/libdfp/libdfp
Source0:        https://github.com/libdfp/libdfp/releases/download/%{version}/%{name}-%{version}.tar.gz
%global soname libdfp.so.1
%ifarch ppc ppc64
%global cpu_variants power6
%endif
ExclusiveArch:	aarch64 ppc ppc64 ppc64le s390 s390x x86_64
%if 0%{?cpu_variants:1}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
The "Decimal Floating Point C Library" is an implementation of ISO/IEC
Technical report  "ISO/IEC TR 24732" which describes the C-Language library
routines necessary to provide the C library runtime support for decimal
floating point data types introduced in IEEE 754-2008, namely _Decimal32,
_Decimal64, and _Decimal128.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static libraries for %{name}
License:	LGPL-2.1-or-later AND GPL-3.0-or-later WITH GCC-exception-3.1
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description	static
The %{name}-static package contains static libraries for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%define subdir_configure \
cat >configure <<'EOF'\
#!/bin/sh\
exec ../${0##*/} "$@"\
EOF\
chmod +x configure \
%configure

%build

%define _lto_cflags %{nil}
mkdir Build
pushd Build
%subdir_configure --disable-static
%make_build
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  mkdir Build-$cpu
  pushd Build-$cpu
  %subdir_configure --disable-static --with-cpu=$cpu
  make %{?_smp_mflags}
  popd
done
%endif
%check

pushd Build
make -k %{?_smp_mflags} check
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  pushd Build-$cpu
  make -k %{?_smp_mflags} check
  popd
done
%endif
%install
pushd Build
%make_install
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  pushd Build-$cpu
  mkdir -p %{buildroot}%{_libdir}/$cpu
  install -m 755 libdfp-%{version}.so %{buildroot}%{_libdir}/$cpu
  ldconfig -l %{buildroot}%{_libdir}/$cpu/libdfp-%{version}.so
  execstack -c %{buildroot}%{_libdir}/$cpu/libdfp-%{version}.so
  if test $cpu = power6; then
    mkdir -p %{buildroot}%{_libdir}/${cpu}x
    pushd %{buildroot}%{_libdir}/${cpu}x
    ln -sf ../$cpu/*.so .
    cp -a ../$cpu/*.so.* .
    popd
  fi
  popd
done
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdfp-devel -f %{oreon_filedir}/libdfp-devel.list
%files -n libdfp-static -f %{oreon_filedir}/libdfp-static.list

%changelog

%autochangelog
