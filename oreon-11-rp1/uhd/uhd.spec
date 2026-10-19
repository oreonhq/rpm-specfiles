%global source0_hash 1e53faec13ea2be9dd8f765956157d1434f41fa0a124fac8f7b2340f8445b026
%bcond_without binary_firmware
%bcond_with wireshark
%bcond_with neon
%global wireshark_ver_full %((%{__awk} '/^#define VERSION[ \t]+/ { print $NF }' /usr/include/wireshark/config.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')
%global wireshark_ver %(VF="%{wireshark_ver_full}"; echo ${VF%.*})
%ifarch %{arm} aarch64
%if ! %{with neon}
%global have_neon -DHAVE_ARM_NEON_H=0
%endif
%endif
Name:           uhd
URL:            http://github.com/EttusResearch/uhd
Version:        4.11.0.0
%global images_ver 4.9.0.0
Release:        1%{?dist}
License:        GPL-3.0-or-later
%if %{with wireshark}
%endif
%if ! %{with binary_firmware}
%endif
Requires(pre):  glibc-common
Requires:       python3-tkinter
Summary:        Universal Hardware Driver for Ettus Research products
Source0:        http://github.com/EttusResearch/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-limits.conf
Source2:        %{url}/releases/download/v%{images_ver}/uhd-images_%{images_ver}.tar.xz
Patch:          uhd-4.8.0.0-imagepath-fix.patch
Patch:          uhd-4.9.0.1-cmake-4-fix.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libatomic
BuildRequires:  libgcrypt-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pybind11-devel
BuildRequires:  python3-cheetah
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-mako
BuildRequires:  python3-numpy
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  tar
BuildRequires:  vim-common
BuildRequires:  wireshark-devel
# /oreon:deps
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

%if ! %{with binary_firmware}
export PATH=$PATH:%{_libexecdir}/sdcc
pushd images
sed -i '/-name "\*\.twr" | xargs grep constraint | grep met/ s/^/#/' Makefile
make %{?_smp_mflags} images
popd
%endif
pushd host
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
pushd tools/dissectors
%cmake -DENABLE_OCTOCLOCK=ON -DENABLE_ZPU=ON
%cmake_build
popd
%endif
%install
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;
pushd host
%cmake_install
sed -i 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/GROUP:="usrp", MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
mv %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-usrp-uhd.rules
rm -rf %{buildroot}%{_libdir}/uhd/{tests,examples}
mkdir -p %{buildroot}%{_libexecdir}/uhd
mv %{buildroot}%{_libdir}/uhd/utils/* %{buildroot}%{_libexecdir}/uhd
popd
mkdir _tmpdoc
mv %{buildroot}%{_docdir}/%{name}/{LICENSE,README.md} _tmpdoc
install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/security/limits.d/99-usrp.conf
mkdir -p %{buildroot}%{_datadir}/uhd/images
cp -r images/images/* %{buildroot}%{_datadir}/uhd/images
rm -rf %{buildroot}%{_datadir}/uhd/images/winusb_driver
pushd %{buildroot}%{_bindir}
for f in uhd_images_downloader usrp2_card_burner
do
  unlink $f
  ln -s ../..%{_libexecdir}/uhd/${f}.py $f
done
popd
install -Dpm 0755 tools/usrp_x3xx_fpga_jtag_programmer.sh %{buildroot}%{_bindir}/usrp_x3xx_fpga_jtag_programmer.sh
%if %{with wireshark}
pushd tools/dissectors
%cmake_install
popd
mkdir -p %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
mv %{buildroot}%{_prefix}/epan %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
%endif
mkdir -p %{buildroot}%{_libdir}/uhd/modules
install -m0644 -D uhd.sysusers.conf %{buildroot}%{_sysusersdir}/uhd.conf
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n uhd-firmware -f %{oreon_filedir}/uhd-firmware.list
%files -n uhd-devel -f %{oreon_filedir}/uhd-devel.list
%files -n uhd-doc -f %{oreon_filedir}/uhd-doc.list
%files -n uhd-tools -f %{oreon_filedir}/uhd-tools.list
%files -n uhd-wireshark -f %{oreon_filedir}/uhd-wireshark.list

%changelog

%autochangelog
