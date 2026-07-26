%global source0_hash d9f9d162fa8a8f61ab1b9983b69180fb0e39573535dfce3b1cbb912a6ffe2d51

%define debug_package %{nil}

Name:           ETL
Epoch:          1
Version:        1.5.4
Release:        1%{?dist}
Summary:        Extended Template Library

License:        GPL-2.0-or-later
URL:            http://synfig.org
Source0:        http://downloads.sourceforge.net/synfig/ETL-%{version}.tar.gz
Buildrequires:  doxygen
Buildrequires:  gcc-c++
BuildRequires:  make
BuildRequires:  glibmm24-devel
Requires:       pkgconfig

%description
Voria ETL is a multi-platform class and template library designed to add
new datatypes and functions which combine well with the existing
types and functions from the C++ Standard Template Library (STL).

%package devel
Summary:        Development files for %{name}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build docs

%install
%make_install

%files devel
%license COPYING
%doc README AUTHORS NEWS
%{_includedir}/ETL/
%{_bindir}/ETL-config
%{_libdir}/pkgconfig/ETL.pc

%changelog
%autochangelog
