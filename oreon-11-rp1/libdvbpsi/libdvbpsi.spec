%global source0_hash 5dbd0fe4a3602a1e3706fe5fe0745554b9af0b56460a2f9d3971a7a727e2ed8b
%global commit0 26bdfd4c0dc58f0f4917461cdf31dae24f9e1463
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Summary:        Library for MPEG TS and DVB PSI tables decoding and generation
Name:		libdvbpsi
Version:	1.3.3
Release:        18%{?dist}
License:	LGPL-2.1-or-later
URL:		https://www.videolan.org/developers/libdvbpsi.html
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%package devel
Summary:	Development package for %{name}
Requires:	%{name}%{_isa} = %{version}-%{release}
%package doc
Summary:	Documentation for %{name}
%description
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.

%description devel
libdvbpsi is a very simple and fully portable library designed for
MPEG TS and DVB PSI table decoding and generation.
This package contains development files for %{name}

%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit0}
autoreconf -vif

%build

%configure --disable-dependency-tracking --disable-static
%make_build
%make_build doc
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdvbpsi-devel -f %{oreon_filedir}/libdvbpsi-devel.list
%files -n libdvbpsi-doc -f %{oreon_filedir}/libdvbpsi-doc.list

%changelog

%autochangelog

