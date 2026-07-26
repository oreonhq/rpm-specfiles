%global source0_hash 9fb50eb15a5d775d4b89598c66e48d6058232faf1bcf040922a291fa63aa8429

Name:		libdfp
Version:	1.0.17
Release:	2%{?dist}
Summary:	Decimal Floating Point C Library
License:	LGPL-2.1-or-later
Url:		https://github.com/libdfp/libdfp
Source0:	https://github.com/libdfp/libdfp/releases/download/%{version}/%{name}-%{version}.tar.gz
#
# Patches from upstream
#

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libdfp.so.1

# Select which different cpu variants are build in addition to the default one
%ifarch ppc ppc64
%global cpu_variants power6
%endif

ExclusiveArch:	aarch64 ppc ppc64 ppc64le s390 s390x x86_64
BuildRequires: make
BuildRequires:	gcc, python3
%if 0%{?cpu_variants:1}
BuildRequires:	execstack
%endif

%description
The "Decimal Floating Point C Library" is an implementation of ISO/IEC
Technical report  "ISO/IEC TR 24732" which describes the C-Language library
routines necessary to provide the C library runtime support for decimal
floating point data types introduced in IEEE 754-2008, namely _Decimal32,
_Decimal64, and _Decimal128.

%package	devel
Summary:	Development files for %{name}
# Use _isa to specify an arch-specific requirement.
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static libraries for %{name}
License:	LGPL-2.1-or-later AND GPL-3.0-or-later WITH GCC-exception-3.1
# Use _isa to specify an arch-specific requirement.
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
# This package uses ASMs for symbol versioning.  It needs to be using
# the symbol verioning attribute instead.  Until then disable LTO
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

%files
%{_libdir}/%{soname}
%{_libdir}/%{name}-%{version}.so
%if 0%{?cpu_variants:1}
%(for cpu in %{cpu_variants}; do echo %dir %{_libdir}/$cpu; test $cpu = power6 && echo %dir %{_libdir}/${cpu}x; done)
%{_libdir}/*/%{soname}
%{_libdir}/*/%{name}-%{version}.so
%endif
%doc %{_docdir}/dfp/README
%doc %{_docdir}/dfp/ChangeLog.md
%license COPYING.txt
%doc %{_docdir}/dfp/COPYING.txt
%doc %{_docdir}/dfp/COPYING.libdfp.txt
%doc %{_docdir}/dfp/COPYING.libdecnumber.txt
%doc %{_docdir}/dfp/COPYING3
%doc %{_docdir}/dfp/COPYING.RUNTIME

%files devel
%{_includedir}/dfp/*
%{_libdir}/*.so
%exclude %{_libdir}/*-*.so
%{_libdir}/pkgconfig/libdfp.pc

%files static
%{_includedir}/decnumber/*
%{_libdir}/libdecnumber.a
%{_libdir}/pkgconfig/libdecnumber.pc

%changelog
%autochangelog
