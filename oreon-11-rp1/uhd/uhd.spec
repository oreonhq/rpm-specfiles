%global source0_hash none

#%%global git_commit c52f3f41806622c95573de21be042f966f675543
#%%global git_date 201904023

#%%global git_short_commit %%(echo %{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%{git_short_commit}

# By default include binary_firmware, otherwise try to rebuild
# the firmware from sources. If you want to rebuild all firmware
# images you need to install appropriate tools (e.g. Xilinx ISE).
%bcond_without binary_firmware

# Currently broken: https://github.com/EttusResearch/uhd/issues/413
%bcond_with wireshark

# NEON support is by default disabled on ARMs
# building with --with=neon will enable auto detection
%bcond_with neon

# X.Y.Z
%global wireshark_ver_full %((%{__awk} '/^#define VERSION[ \t]+/ { print $NF }' /usr/include/wireshark/config.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')
# X.Y
%global wireshark_ver %(VF="%{wireshark_ver_full}"; echo ${VF%.*})

%ifarch %{arm} aarch64
%if ! %{with neon}
%global have_neon -DHAVE_ARM_NEON_H=0
%endif
%endif

Name:           uhd
URL:            http://github.com/EttusResearch/uhd
Version:        4.9.0.1
#%%global images_ver %%{version}
%global images_ver 4.9.0.0
Release:        3%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  libusb1-devel
BuildRequires:  python3-cheetah
BuildRequires:  ncurses-devel
BuildRequires:  python3-docutils
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  libpcap-devel
BuildRequires:  python3-numpy
BuildRequires:  vim-common
BuildRequires:  libatomic
%if %{with wireshark}
BuildRequires:  wireshark-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  gnutls-devel
%endif
BuildRequires:  pybind11-devel
BuildRequires:  python3-mako
BuildRequires:  python3-requests
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  tar
%if ! %{with binary_firmware}
BuildRequires:  sdcc
BuildRequires:  sed
%endif
Requires(pre):  glibc-common
Requires:       python3-tkinter
Summary:        Universal Hardware Driver for Ettus Research products
Source0:        %{url}/archive/v%{version}/uhd-%{version}.tar.gz
Source1:        %{name}-limits.conf
Source2:        %{url}/releases/download/v%{images_ver}/uhd-images_%{images_ver}.tar.xz
# dirty workaround for the https://github.com/EttusResearch/uhd/issues/551
# until the better fix is available
Patch:          uhd-4.8.0.0-imagepath-fix.patch
# already in upstream
Patch:          uhd-4.9.0.1-cmake-4-fix.patch

%description
The UHD is the universal hardware driver for Ettus Research products.
The goal of the UHD is to provide a host driver and API for current and
future Ettus Research products. It can be used standalone without GNU Radio.

%package firmware
Summary:        Firmware files for UHD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description firmware
Firmware files for the Universal Hardware driver (UHD).

%package devel
Summary:        Development files for UHD
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for the Universal Hardware Driver (UHD).

# arch due to bug in doxygen
%package doc
Summary:        Documentation files for UHD

%description doc
Documentation for the Universal Hardware Driver (UHD).

%package tools
Summary:        Tools for working with / debugging USRP device
Requires:       %{name} = %{version}-%{release}

%description tools
Tools that are useful for working with and/or debugging USRP device.

%if %{with wireshark}
%package wireshark
Summary:        Wireshark dissector plugins
Requires:       %{name} = %{version}-%{release}
Requires:       %{_libdir}/wireshark/plugins/%{wireshark_ver}

%description wireshark
Wireshark dissector plugins.
%endif

%prep
%autosetup -p1

# firmware
%if %{with binary_firmware}
# extract binary firmware
mkdir -p images/images
tar -xJf %{SOURCE2} -C images/images --strip-components=1
rm -f images/images/{LICENSE.txt,*.tag}
# remove Windows drivers
rm -rf images/winusb_driver
%endif

# fix python shebangs
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

# Create a sysusers.d config file
cat >uhd.sysusers.conf <<EOF
g usrp -
EOF

%build
# firmware
%if ! %{with binary_firmware}
# rebuilt from sources
export PATH=$PATH:%{_libexecdir}/sdcc
pushd images
sed -i '/-name "\*\.twr" | xargs grep constraint | grep met/ s/^/#/' Makefile
make %{?_smp_mflags} images
popd
%endif

pushd host
# DLIB_SUFFIX workaround for cmake 4.0
# https://github.com/EttusResearch/uhd/issues/844
%cmake %{?have_neon} -DPYTHON_EXECUTABLE="%{__python3}" \
  -DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
  -DUHD_VERSION="%{version}" \
  -DENABLE_TESTS=off ../ \
%if "%{?_lib}"=="lib64"
  -DLIB_SUFFIX=64
%endif
%cmake_build
popd

%if %{with wireshark}
# wireshark dissectors
pushd tools/dissectors
%cmake -DENABLE_OCTOCLOCK=ON -DENABLE_ZPU=ON
%cmake_build
popd
%endif

#%%check
#cd host/%%{_vpath_builddir}
#%%ctest

%install
# fix python shebangs (run again for generated scripts)
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

pushd host
%cmake_install

# Fix udev rules and use dynamic ACL management for device
sed -i 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/GROUP:="usrp", MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
mv %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-usrp-uhd.rules

# Remove tests, examples binaries
rm -rf %{buildroot}%{_libdir}/uhd/{tests,examples}

# Move the utils stuff to libexec dir
mkdir -p %{buildroot}%{_libexecdir}/uhd
mv %{buildroot}%{_libdir}/uhd/utils/* %{buildroot}%{_libexecdir}/uhd

popd
# Package base docs to base package
mkdir _tmpdoc
mv %{buildroot}%{_docdir}/%{name}/{LICENSE,README.md} _tmpdoc

install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/security/limits.d/99-usrp.conf

# firmware
mkdir -p %{buildroot}%{_datadir}/uhd/images
cp -r images/images/* %{buildroot}%{_datadir}/uhd/images

# remove win stuff
rm -rf %{buildroot}%{_datadir}/uhd/images/winusb_driver

# convert hardlinks to symlinks (to not package the file twice)
pushd %{buildroot}%{_bindir}
for f in uhd_images_downloader usrp2_card_burner
do
  unlink $f
  ln -s ../..%{_libexecdir}/uhd/${f}.py $f
done
popd

# tools
install -Dpm 0755 tools/usrp_x3xx_fpga_jtag_programmer.sh %{buildroot}%{_bindir}/usrp_x3xx_fpga_jtag_programmer.sh

%if %{with wireshark}
# wireshark dissectors
pushd tools/dissectors
%cmake_install
popd
# fix wireshark dissectors location
mkdir -p %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
mv %{buildroot}%{_prefix}/epan %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
%endif

# add directory for modules
mkdir -p %{buildroot}%{_libdir}/uhd/modules

install -m0644 -D uhd.sysusers.conf %{buildroot}%{_sysusersdir}/uhd.conf

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/doxygen
%exclude %{_datadir}/uhd/images
%doc _tmpdoc/*
%dir %{_libdir}/uhd
%{_bindir}/usrpctl
%{_bindir}/uhd_*
%{_bindir}/usrp2_*
%{_bindir}/usrp_hwd.py
%{_prefix}/lib/udev/rules.d/10-usrp-uhd.rules
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf
%{_libdir}/lib*.so.*
%{_libdir}/uhd/modules
%{_libexecdir}/uhd
%{_mandir}/man1/*.1*
%{_datadir}/uhd
%{python3_sitearch}/uhd
%{python3_sitearch}/usrp_mpm
%{_sysusersdir}/uhd.conf

%files firmware
%dir %{_datadir}/uhd/images
%{_datadir}/uhd/images/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/uhd/*.cmake
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{name}/doxygen

%files tools
%doc tools/README.md
%{_bindir}/usrp_x3xx_fpga_jtag_programmer.sh

%if %{with wireshark}
%files wireshark
%{_libdir}/wireshark/plugins/%{wireshark_ver}/epan/*
%endif

%changelog
%autochangelog
