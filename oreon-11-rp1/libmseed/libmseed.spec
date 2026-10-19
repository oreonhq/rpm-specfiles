%global source0_hash f397b9a32714164d6440b9eeadfbf5b4aece46184515b6ba48941e2cbcb4806a
Name:		libmseed
Version:	3.5.4
Release:        1%{?dist}
License:	LGPL-3.0-or-later
Summary:        A C library framework for manipulating and managing SEED data records
Url:		https://www.iris.edu/ds/nodes/dmc/software/downloads/libmseed
Source0:        https://github.com/iris-edu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:	0001-Fail-tests-early.patch
# oreon:deps
BuildRequires:  binutils
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
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
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd test
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" make test
popd
%files -f %{oreon_filedir}/main.list
%files -n libmseed-devel -f %{oreon_filedir}/libmseed-devel.list

%changelog

%autochangelog
