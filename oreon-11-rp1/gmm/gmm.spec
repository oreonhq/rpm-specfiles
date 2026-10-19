%global source0_hash c7603f9007fe8e0be5beb68709d655bdef13c327f50391b69243fbc42dfefac6
Name:    gmm
Version: 5.5
Release:        1%{?dist}
Summary:        A generic C++ template library for sparse, dense and skyline matrices
License: LGPL-3.0-or-later AND BSD-3-Clause
URL:     https://getfem.org/gmm.html
Source0:        https://download-mirror.savannah.gnu.org/releases/getfem/stable/gmm-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%package devel
Summary:A generic C++ template library for sparse, dense and skyline matrices
Provides: %{name} = %{version}-%{release}
Provides: gmm++-devel = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check -k || cat tests/test-suite.log ||:
%files -f %{oreon_filedir}/main.list
%files -n gmm-devel -f %{oreon_filedir}/gmm-devel.list

%changelog

%autochangelog
