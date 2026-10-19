%global source0_hash a966acad32bd6c48a53e5eb5e71db9172981a7ad2282c2900404d192f832d748
Name: cloudy
Version: 17.03
Release:        14%{?dist}
Summary:        Spectral synthesis code to simulate conditions in interstellar matter
License: Zlib
URL: http://www.nublado.org/
Source0:        http://data.nublado.org/cloudy_releases/c17/c%{version}.tar.gz
Patch0: cloudy-make.patch
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Most of the quantitative information we have about the cosmos comes from 
spectroscopy. In many cases the light we analyze was produced by atoms in 
the first generations of stars and galaxies.  The spectra are produced by 
dilute gas where such properties as the gas kinetic temperature, chemical 
state, level of ionization, and level populations, are determined by a 
host of microphysical processes rather than by a single temperature. 
Analytical solutions are seldom possible and computer solutions are 
needed to understand their physical properties. Numerical simulations make 
it possible to understand complex physical environments starting from 
first principles. Cloudy is designed to do exactly this.

%package data
Summary: data %{name}
BuildArch: noarch
%description data
This package contains the atomic data for %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
This package contains the usage documentation for %{name}.

%prep
%global oreon_srcdir c%{version}
%oreon_prep
%build

cd source
make %{?_smp_mflags} CXX="%{__cxx}" CXXFLAGS="%{optflags}" \
    CLOUDY_DATA_PATH=%{_datadir}/%{name}/data/
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/scripts
mkdir -p %{buildroot}/%{_datadir}/%{name}/grain
install -m 755 source/cloudy.exe %{buildroot}/%{_bindir}/cloudy
cp -a data/ %{buildroot}/%{_datadir}/%{name}/
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/convert_calpgm
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/convert_calpgm.cpp
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/.gitignore
%oreon_autofiles cloudy-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cloudy-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

echo "test" > test.in
export CLOUDY_DATA_PATH="%{buildroot}/%{_datadir}/%{name}/data/"
%{buildroot}/%{_bindir}/cloudy -r test
%files -f %{oreon_filedir}/main.list
%files -n cloudy-data -f %{oreon_filedir}/cloudy-data.list
%files -n cloudy-doc -f %{oreon_filedir}/cloudy-doc.list

%changelog

%autochangelog
