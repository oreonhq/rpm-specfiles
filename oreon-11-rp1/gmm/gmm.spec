%global source0_hash 15eb1943011b92665aab3b02ecf3cede1cf89ea15a9006f81f2ba2cd662aa02b

Name:    gmm
Version: 5.4.4
Release: %autorelease
Summary: A generic C++ template library for sparse, dense and skyline matrices
License: LGPL-3.0-or-later AND BSD-3-Clause
URL:     https://getfem.org/gmm.html
Source0: https://download-mirror.savannah.gnu.org/releases/getfem/stable/gmm-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gcc-c++
BuildRequires: perl-interpreter
BuildRequires: make

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

%autosetup

%build
%configure

%install
%make_install

%check
make check -k || cat tests/test-suite.log ||:

%files devel
%doc README
%license COPYING
%{_includedir}/gmm/

%changelog
%autochangelog
