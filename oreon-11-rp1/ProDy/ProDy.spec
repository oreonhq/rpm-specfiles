%global source0_hash 69e18fa88f0b36c7204e81b86b947a1eb122c806910030609b91ff6b40d0ade7
%global with_check 0
%global _privatelibs  ^%{python3_sitearch}/prody/.*\\.so$
%global __provides_exclude_from ^(%{_privatelibs})$
%global __requires_exclude_from ^(%{_privatelibs})$
Name: ProDy
Summary:        Application for protein structure, dynamics and sequence analysis
Version: 2.6.1
Release:        1%{?dist}
License: MIT AND MIT-CMU AND MIT-Modern-Variant AND BSD-2-Clause AND BSD-3-Clause AND Python-2.0.1 AND NIST-PD
URL: http://www.bahargroup.org/prody
Source0:        https://github.com/prody/ProDy/archive/v%{version}/ProDy-%{version}.tar.gz
ExcludeArch:    %{ix86}
Patch0: Fix-rtbtools-to-permit-numpy-upgrade.patch
Patch1: eigh-evd-when-no-turbo.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) < 2.0
BuildRequires:  python3dist(pyparsing) <= 3.1.1
BuildRequires:  python3dist(setuptools) < 69
Requires:       python3-ProDy = %{version}-%{release}
# /oreon:deps
%description
ProDy is a free and open-source Python package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis.

%package -n python3-%{name}
Summary: Application for protein structure, dynamics and sequence analysis
%{?python_provide:%python_provide python3-%{name}}
Provides: ProDy = 0:%{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-urllib3
BuildRequires: python3-scipy
BuildRequires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-biopython
BuildRequires: python3-setuptools
BuildRequires: pyproject-rpm-macros
%description -n python3-%{name}
This is ProDy Python3 package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%prep

%autosetup -p1

# Fix permissions
find prody/proteins/ccealign -name '*.h' -exec chmod 0644 '{}' \;
find prody/proteins/ccealign -name '*.cpp' -exec chmod 0644 '{}' \;

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/*
cd scripts
cp -pr ./prody ./python%{python3_version}-prody
cp -pr ./evol  ./python%{python3_version}-evol
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
 ./prody \
 ./evol \
 ./python%{python3_version}-prody \
 ./python%{python3_version}-evol
for i in prody-%{python3_version}; do
  touch -r ./python%{python3_version}-prody $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./prody $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}
  ln -srf python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}/$i
done
for i in evol-%{python3_version}; do
  touch -r ./python%{python3_version}-evol $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./evol $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}
  ln -srf python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}/$i
done
cd ..
%oreon_autofiles python3-ProDy usr/lib/python3*/site-packages/ProDy* usr/lib64/python3*/site-packages/ProDy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ProDy* usr/lib64/python3*/site-packages/ProDy* usr/bin/*
%if 0%{?with_check}
%check

%pyproject_check_import
%pytest -m "not network"
%endif
%files
%files -n python3-ProDy -f %{oreon_filedir}/python3-ProDy.list

%changelog

%autochangelog
