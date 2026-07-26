%global source0_hash 77a2d335416a1debd2e01251e9cbca5d7f81dc993dc59ca356810c24ab8c84ec

Name:		libmseed
Version:	2.19.5
Release:	22%{?dist}
License:	LGPL-3.0-or-later
Summary:	A C library framework for manipulating and managing SEED data records
Url:		https://www.iris.edu/ds/nodes/dmc/software/downloads/libmseed
Source0:	https://github.com/iris-edu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream doesn't want this, but we want to fail the build for failing tests.
Patch0001:	0001-Fail-tests-early.patch

BuildRequires:	binutils
BuildRequires:	diffutils
BuildRequires:	gcc
BuildRequires:	make

%package devel
Summary:	%{summary}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Mini-SEED library provides a framework for manipulation of SEED data
records including the unpacking and packing of data records. Functionality is
also included for managing waveform data as continuous traces. All structures
of SEED 2.4 data records are supported with the following exceptions:
Blockette 2000 opaque data which has an unknown data structure by definition
and Blockette 405 which depends on full SEED (SEED including full ASCII
headers) for a full data description.

%description devel
Development files for %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# This code is not strict-aliasing safe.  See the various swap routines
%build
CC=gcc CFLAGS="%{optflags} -fno-strict-aliasing" %make_build shared

pushd example
CC=gcc CFLAGS="%{optflags} -fno-strict-aliasing" %make_build all
popd

%install
%make_install \
	PREFIX=%{_prefix} \
	EXEC_PREFIX=%{_exec_prefix} \
	LIBDIR=%{_libdir} \
	INCLUDEDIR=%{_includedir} \
	DATAROOTDIR=%{_datarootdir} \
	DOCDIR=%{_docdir}/%{name} \
	MANDIR=%{_mandir} \
	install

mkdir -p %{buildroot}%{_bindir}
cp -pd example/msrepack example/msview %{buildroot}%{_bindir}/

# We don't use this.
rm -rf %{buildroot}%{_docdir}/%{name}

%check
pushd test
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" make test
popd

%files
%doc README.md README.byteorder ChangeLog
%license LICENSE.txt
%{_bindir}/msrepack
%{_bindir}/msview
%{_libdir}/libmseed.so.*

%files devel
%doc doc/libmseed-UsersGuide example/test.mseed
%license LICENSE.txt
%{_includedir}/libmseed.h
%{_libdir}/libmseed.so
%{_libdir}/pkgconfig/mseed.pc
%{_mandir}/man3/*

%changelog
%autochangelog
