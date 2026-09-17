%global source0_hash 2781dd3a6cc5f9a49c91a4519dde2b1c24335a5bfe0cc1c9881b6363142452b4

Name:           armadillo
Version:        12.8.1
Release:        9%{?dist}
Summary:        Fast C++ matrix library with syntax similar to MATLAB and Octave

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://arma.sourceforge.net/
Source:         http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  arpack-devel
BuildRequires:  hdf5-devel
BuildRequires:  SuperLU-devel

# flexiblas is only available on Fedora, for EPEL replace it by atlas, lapack and openblas
%if 0%{?fedora} || 0%{?rhel} >= 9
%global extra_options -DALLOW_FLEXIBLAS_LINUX=ON
BuildRequires:  flexiblas-devel
%else
%undefine __cmake_in_source_build
%global extra_options %{nil}
BuildRequires:  atlas-devel
BuildRequires:  lapack-devel
%{!?openblas_arches:%global openblas_arches x86_64 %{ix86} armv7hl %{power64} aarch64}
%ifarch %{openblas_arches}
BuildRequires:  openblas-devel
%endif
%endif

%description
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab or Octave.

%package devel
Summary:        Development headers and documentation for the Armadillo C++ library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       arpack-devel
Requires:       hdf5-devel
Requires:       SuperLU-devel

%if 0%{?fedora} || 0%{?rhel} >= 9
Requires:  flexiblas-devel
%else
Requires:  atlas-devel
Requires:  lapack-devel
%ifarch %{openblas_arches}
Requires:  openblas-devel
%endif
%endif

%description devel
This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (API reference guide).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\r//' README.md
rm -rf examples/*win64*
sed -i 's/cmake_minimum_required(VERSION 3.5)/cmake_minimum_required(VERSION 3.5...3.30)/' CMakeLists.txt

%build
%cmake %{extra_options} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%check
%cmake %{extra_options} -DBUILD_SMOKE_TEST=ON

%ctest

%if (0%{?rhel} && 0%{?rhel} <= 7)
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%files
%{_libdir}/libarmadillo.so.12*
%license LICENSE.txt NOTICE.txt

%files devel
%{_libdir}/libarmadillo.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/
%doc README.md
%doc index.html
%doc docs.html
%doc examples
%doc armadillo_icon.png
%doc mex_interface
%doc armadillo_nicta_2010.pdf
%doc armadillo_rcpp_2014.pdf
%doc armadillo_joss_2016.pdf
%doc armadillo_spcs_2017.pdf
%doc armadillo_lncs_2018.pdf
%doc armadillo_solver_2020.pdf

%changelog
%autochangelog
