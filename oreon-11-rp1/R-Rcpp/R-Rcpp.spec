%global source0_hash da0c616a71c82150397259516b2ea7558dbd31a5b4a217423ec9666b3a0fcfb7
Name:           R-Rcpp
Version:        1.1.1
Release:        1%{?dist}
Summary:        Seamless R and C++ Integration
License:        GPL-2.0-or-later AND BSL-1.0
URL:            https://cran.r-project.org/package=Rcpp
Source0:        https://cran.r-project.org/src/contrib/Archive/Rcpp/Rcpp_%{version}.tar.gz
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel <= 1.1.0
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  dos2unix
# /oreon:deps
%description
The Rcpp package provides R functions as well as C++ classes which
offer a seamless integration of R and C++. Many R data types and
objects can be mapped back and forth to C++ equivalents which
facilitates both writing of new code as well as easier integration of
third-party libraries.
Documentation about Rcpp is provided by several vignettes included in
this package, via the Rcpp Gallery site at http://gallery.rcpp.org,
the paper by Eddelbuettel and Francois (2011, JSS), and the book by
Eddelbuettel (2013, Springer).
See citation("Rcpp") for details on the last two.

%package        examples
Summary:        Rcpp Examples
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
Examples for using Rcpp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

dos2unix -k \
    Rcpp/inst/tinytest/cpp/InternalFunction.cpp \
    Rcpp/inst/tinytest/cpp/InternalFunctionCPP11.cpp

%build

%install
%R_install
sed 's!/bin/env Rscript!/usr/bin/Rscript!' \
    -i %{buildroot}%{_R_libdir}/Rcpp/discovery/cxx0x.R
chmod 755 %{buildroot}%{_R_libdir}/Rcpp/discovery/cxx0x.R
for f in ConvolveBenchmarks/overhead.r ConvolveBenchmarks/overhead.sh \
         Misc/ifelseLooped.r Misc/newFib.r OpenMP/OpenMPandInline.r ; do
    chmod 755 %{buildroot}%{_R_libdir}/Rcpp/examples/$f
done
for f in `find %{buildroot}%{_R_libdir}/Rcpp/examples -type f` ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done
%R_save_files
grep -vE "examples|tinytest" %{R_files} > %{R_files}.main
grep examples %{R_files} > %{R_files}.examples
%oreon_autofiles R-Rcpp-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%R_check
rm -rf %{buildroot}%{_R_libdir}/Rcpp/tinytest
%files -f %{oreon_filedir}/main.list
%files -n R-Rcpp-examples -f %{oreon_filedir}/R-Rcpp-examples.list

%changelog

%autochangelog
