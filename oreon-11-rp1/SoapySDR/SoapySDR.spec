%global source0_hash a508083875ed75d1090c24f88abef9895ad65f0f1b54e96d74094478f0c400e6
Name:           SoapySDR
Version:        0.8.1
Release:        22%{?dist}
Summary:        A Vendor Neutral and Platform Independent SDR Support Library
License:        BSL-1.0
URL:            https://github.com/pothosware/%{name}
Source0:        https://github.com/pothosware/%{name}/archive/refs/tags/soapy-sdr-%{version}.tar.gz
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  swig
# /oreon:deps
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
%global oreon_srcdir %{name}-soapy-sdr-%{version}
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export Python_ADDITIONAL_VERSIONS="%{python3_version}"
%cmake -DUSE_PYTHON_CONFIG=ON -DPYTHON3_EXECUTABLE=%{__python3} -DSOAPY_SDR_EXTVER=%{release}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/%{name}/modules0.8
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{__cmake_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}
%oreon_autofiles python3-SoapySDR usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles SoapySDR-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles SoapySDR-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ctest -V %{?_smp_mflags}
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n python3-SoapySDR -f %{oreon_filedir}/python3-SoapySDR.list
%files -n SoapySDR-devel -f %{oreon_filedir}/SoapySDR-devel.list
%files -n SoapySDR-doc -f %{oreon_filedir}/SoapySDR-doc.list

%changelog

%autochangelog
