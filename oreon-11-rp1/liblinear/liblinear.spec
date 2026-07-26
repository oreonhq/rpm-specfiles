%global source0_hash 11367ebdbd492fb8daa2ad13c749db5b301b01a11a8c0e6e1b9529caf9bb3114

Name:			liblinear
Version:		1.94
Release:		46%{?dist}
Summary:		Library for Large Linear Classification
%{?el5:Group:		System Environment/Libraries}

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib blas
%endif

# Automatically converted from old format: BSD - review is highly recommended.
License:		LicenseRef-Callaway-BSD
URL:			http://www.csie.ntu.edu.tw/~cjlin/%{name}
Source0:		%{url}/%{name}-%{version}.tar.gz
Source1:		%{url}/index.html
Source2:		%{url}/FAQ.html
Source3:		%{url}/exp.html
Source4:		http://www.csie.ntu.edu.tw/~cjlin/papers/%{name}.pdf

# simple fixes, not needed by upstream
Patch0:			liblinear-adapt_makefile.patch
Patch1:			liblinear-fix_compiler_warnings.patch

%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:  gcc-c++
BuildRequires:  %{blaslib}-devel

%description
%{name} is an open source library for large-scale linear classification.
It supports logistic regression and linear support vector machines.  It
provides easy-to-use command-line tools and library calls for users and
developers.  Comprehensive documents are available for both beginners
and advanced users.

Experiments demonstrate that %{name} is very efficient on large sparse
data sets.  %{name} is the winner of ICML 2008 large-scale learning
challenge (linear SVM track).  It is also used for winning KDD Cup 2010.

%ldconfig_scriptlets

%files
%doc COPYRIGHT
%{_libdir}/%{name}.so.*

%package cli
Summary:		CLI-tools for %{name}
%{?el5:Group:		Applications/Engineering}

Requires:		%{name}%{?_isa}		== %{version}-%{release}

%description cli
This package contains cli-tools for use with %{name}.

For further information read "3.1 Practical Usage" from the pdf included
in the %{name}-doc package.

%files cli
%doc heart_scale
%{_bindir}/*

%package devel
Summary:		Development files for %{name}
%{?el5:Group:		Development/Libraries}

Requires:		%{name}%{?_isa}		== %{version}-%{release}
%{?el5:Requires:	%{_bindir}/pkg-config}

%{?el5:Provides:	pkgconfig(%{name})	== %{version}}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%package doc
Summary:		Documentation files for %{name}
%{?el5:Group:		Documentation}

%{!?el5:BuildArch:	noarch}

%description doc
The %{name}-doc package contains some brief documentation for developing
applications that use %{name}.

%files doc
%doc COPYRIGHT README* {predict,train}.c *.html *.pdf

%if 0%{?fedora} || 0%{?rhel} >= 8
%package -n python3-%{name}
Summary:		Python3 bindings for %{name}

BuildRequires:		python3-devel
BuildRequires: make
Requires:		%{name}%{?_isa}		== %{version}-%{release}

%description  -n python3-%{name}
This package contains bindings for developing Python3 applications that
use %{name}.

For further information read "README.python" included in the
%{name}-doc package.

%files -n python3-%{name}
%{python3_sitearch}/*
%endif #0%{?fedora} || 0%{?rhel} >= 8

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

# pull in other sources
install -pm 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

# remove bundled stuff
rm -rf blas/ matlab/ windows/ Makefile.*

# add pkg-config file
cat << EOF >> %{name}.pc
#################################
# Pkg-Config file for %{name} #
#################################

Name: %{name}
Description: Library for Large Linear Classification
URL: %{url}
Version: %{version}

prefix=%{_prefix}
includedir=%{_includedir}

Cflags: -I\$\{includedir\}/liblinear
Libs: -llinear
EOF

# rename python/README for inclusion in doc
mv python/README README.python

# remove hashbang from lib's files
for _file in python/*.py
do
  sed '1{\@^#!/usr/bin/env python@d}' ${_file} > ${_file}.new &&
  touch -r ${_file} ${_file}.new &&
  mv -f ${_file}.new ${_file}
done

# set blaslib
sed -i 's/-lblas/-l%{blaslib}/g' Makefile

%build
# Fortran doesn't like as-needed
%undefine _ld_as_needed

%configure ||:
make %{?_smp_mflags}

%install
%{?el5:rm -rf %{buildroot}}

# no install-target in Makefile
mkdir -p %{buildroot}%{_bindir}			\
	%{buildroot}%{_libdir}/pkgconfig	\
	%{buildroot}%{_includedir}/%{name}

install -pm 0755 predict %{buildroot}%{_bindir}/%{name}-predict
install -pm 0755 train %{buildroot}%{_bindir}/%{name}-train
install -pm 0755 %{name}.so.1 %{buildroot}%{_libdir}
ln -s %{name}.so.1 %{buildroot}%{_libdir}/%{name}.so
install -pm 0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig
install -pm 0644 {linear,tron}.h %{buildroot}%{_includedir}/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 8
mkdir -p %{buildroot}%{python3_sitearch}
install -pm 0644 python/*.py %{buildroot}%{python3_sitearch}
%endif #0%{?fedora} || 0%{?rhel} >= 8

%changelog
%autochangelog
