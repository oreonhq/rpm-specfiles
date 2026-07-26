%global source0_hash a508083875ed75d1090c24f88abef9895ad65f0f1b54e96d74094478f0c400e6

Name:           SoapySDR
Version:        0.8.1
Release:        22%{?dist}
Summary:        A Vendor Neutral and Platform Independent SDR Support Library

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            https://github.com/pothosware/%{name}
Source0:        https://github.com/pothosware/%{name}/archive/refs/tags/soapy-sdr-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  doxygen
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: (python3-setuptools if python3-devel >= 3.12)

%description
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n python3-%{name}
Summary:        Python3 Bindings for SoapySDR
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %{name}-devel
Summary:        Development Files for SoapySDR
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %{name}-doc
Summary:        Development Files for SoapySDR
BuildArch: noarch

%description -n %{name}-doc
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices. This package includes
library header file documentation.
    
    
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-soapy-sdr-%{version}

%build
# TODO: Remove in the next release
# https://github.com/pothosware/SoapySDR/commit/fbf9f3c328868f46029284716df49095ab7b99a6
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export Python_ADDITIONAL_VERSIONS="%{python3_version}"
%cmake -DUSE_PYTHON_CONFIG=ON -DPYTHON3_EXECUTABLE=%{__python3} -DSOAPY_SDR_EXTVER=%{release}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/%{name}/modules0.8
# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{__cmake_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}

%check
ctest -V %{?_smp_mflags}

%ldconfig_scriptlets
%files
%license LICENSE_1_0.txt
%{_bindir}/SoapySDRUtil
%{_libdir}/libSoapySDR.so.0.8.1
%{_libdir}/libSoapySDR.so.0.8
%{_mandir}/man1/*
%doc README.md
# for hardware support modules
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules0.8

%files -n python3-%{name}
%license LICENSE_1_0.txt
%{python3_sitearch}/SoapySDR.py
%{python3_sitearch}/_SoapySDR.so
%{python3_sitearch}/__pycache__/SoapySDR.cpython-*.pyc

%files -n %{name}-devel
%{_includedir}/%{name}
%{_libdir}/libSoapySDR.so
%{_libdir}/pkgconfig/*
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/*

%files -n %{name}-doc
%license LICENSE_1_0.txt
%{_pkgdocdir}/*

%changelog
%autochangelog
