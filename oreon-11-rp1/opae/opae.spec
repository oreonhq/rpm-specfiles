%global source0_hash 38c54430d0c49089b11d8bb2f3a64bed3e373aa60a8bd1708d2ffae953c2e0a1
Summary:        Open Programmable Acceleration Engine (OPAE) SDK
Name:           opae
Vendor:         Intel Corporation
License:        LicenseRef-Callaway-BSD
Version:        2.13.0
%define opae_release 3
%define patch_level 3
Release:        1%{?dist}
URL:            https://github.com/OPAE/%{name}-sdk
Source0:        https://github.com/OPAE/%{name}-sdk/archive/refs/tags/%{version}-%{opae_release}.tar.gz
Group:          Development/Libraries
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cli11-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  json-c-devel
BuildRequires:  libedit-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pip
BuildRequires:  python3-pybind11
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  rpm-build
BuildRequires:  spdlog-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tbb-devel
# /oreon:deps
%description
Open Programmable Acceleration Engine (OPAE) is a software framework
for managing and accessing programmable accelerators (FPGAs).
Its main parts are:

* OPAE Software Development Kit (OPAE SDK) (this package)
* OPAE Linux driver for Intel(R) PAC with Arria(R) 10 GX FPGA
* Intel(R) PAC N6000/D5005, Silicom FPGA SmartNIC N5010 Series,
* Intel FPGA Programmable Acceleration Card N6000

OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
It provides a library implementing the OPAE C API for presenting a
streamlined and easy-to-use interface for software applications to
discover, access, and manage FPGA devices and accelerators using
the OPAE software stack.

%package devel
Summary:    OPAE headers, sample source, and documentation
Requires:   opae
Requires:   libuuid-devel, %{name}%{?_isa} = %{version}-%{release}
Requires:   openssl-devel
%description devel
OPAE headers, tools, sample source, and documentation

%package extra-tools
Summary:    Additional OPAE tools
Requires:   opae-devel
%description extra-tools
This package contains OPAE extra tools binaries, 
software tools for accelerators

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-sdk-%{version}-%{opae_release}

# No Werror's please
sed -i -e 's@-Werror @ @' cmake/modules/OPAECompiler.cmake

%build

%cmake -DCMAKE_INSTALL_PREFIX=/usr \
       -DOPAE_PRESERVE_REPOS=ON \
       -DOPAE_BUILD_PYTHON_DIST=ON \
       -DOPAE_BUILD_FPGABIST=ON
export PIP_NO_BUILD_ISOLATION=off
%cmake_build
%install
mkdir -p %{buildroot}%{_datadir}/opae
cp RELEASE_NOTES.md %{buildroot}%{_datadir}/opae/RELEASE_NOTES.md
cp LICENSE %{buildroot}%{_datadir}/opae/LICENSE
cp COPYING %{buildroot}%{_datadir}/opae/COPYING
export PIP_NO_BUILD_ISOLATION=off
%cmake_install
for file in %{buildroot}%{python3_sitelib}/opae/admin/tools/{fpgaflash,fpgaotsu,fpgaport,fpgasupdate,ihex2ipmi,rsu,super_rsu,bitstream_info,opaevfio,pci_device,fpgareg,n5010tool}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/ethernet/{hssicommon,hssiloopback,hssimac,hssistats}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/opae/diag/{common,fecmode,fpgadiag,fpgalpbk,fpgamac,fpgastats,fvlbypass,mactest,mux}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitearch}/opae/fpga/tools/opae_mem.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/packager/tools/{afu_json_mgr,packager}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/platmgr/tools/{afu_platform_config,afu_platform_info,afu_synth_setup,rtl_src_config}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/uio/ofs_uio.py; do
   chmod a+x $file
done
chmod a+x %{buildroot}%{_usr}/src/opae/cmake/modules/*.cmake
chmod a+x %{buildroot}%{_usr}/lib/opae-%{version}/modules/*.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post fpgad.service
/sbin/ldconfig
%preun

%systemd_preun fpgad.service
%files -f %{oreon_filedir}/main.list
%files -n opae-devel -f %{oreon_filedir}/opae-devel.list
%files -n opae-extra-tools -f %{oreon_filedir}/opae-extra-tools.list

%changelog

%autochangelog
