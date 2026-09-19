%global source0_hash c5f445344a465c1d9afc6516544dc4a2fba588af7ba0f1ac1a6b538260f0cd96

Name:           gau2grid
Version:        2.0.8
Release:        1%{?dist}
Summary:        Fast computation of a gaussian function and its derivative on a grid
License:        BSD-3-Clause
URL:            https://github.com/dgasmith/gau2grid
Source0:        https://github.com/dgasmith/gau2grid/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy

%description
A collocation code for computing gaussians on a grid of the form:
out_Lp = x^l y^m z^n \sum_i coeff_i e^(exponent_i * (|center - p|)^2)

%package devel
Summary:        Development headers for gau2grid
Requires:       cmake
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for gau2grid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DENABLE_XHOST=OFF
%{cmake_build}

%install
%{cmake_install}

%files
%license LICENSE
%doc README.md
%{_libdir}/libgg.so.2*

%files devel
%{_includedir}/gau2grid/ 
%{_datadir}/cmake/gau2grid/
%{_libdir}/libgg.so

%changelog
%autochangelog
