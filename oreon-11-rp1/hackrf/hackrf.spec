%global source0_hash none

Name:           hackrf
Version:        2026.01.3
Release:        1%{?dist}
Summary:        HackRF Utilities

License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://greatscottgadgets.com/%{name}/
Source0:        https://github.com/greatscottgadgets/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

Patch0:         shebang.patch
Patch1:         static.patch

BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  systemd

# When the host software changes, we generally will also have to update the firmware.
Recommends:     %{name}-firmware = %{version}-%{release}

%description
Hardware designs and software for HackRF, a project to produce a low cost, open
source software radio platform.

NOTE: To upgrade to this release, you must update libhackrf and hackrf-tools on
your host computer.  You must also update firmware on your HackRF device.

%package devel
Summary:        Development files for %{name}
License:        BSD-3-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libusbx-devel

%description devel
Files needed to develop software against libhackrf.

%package doc
Summary:        Supplemental documentation for HackRF
License:        GPL-2.0-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Supplemental documentation for HackRF.  For more information, visit the project at
https://greatscottgadgets.com/hackrf

%package firmware
Summary:        Firmware for HackRF
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description firmware
Firmware for HackRF.

%package hardware
Summary:        Hardware schematics / pcb layout for HackRF.
License:        CERN-OHL-P-2.0 AND GPL-2.0-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description hardware
Hardware schematics / pcb layout for HackRF.

%prep
%autosetup -p1

# Fix "plugdev" nonsense
sed -i -e 's/GROUP="@HACKRF_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules.in
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules

%build
pushd host
%cmake \
  -DINSTALL_UDEV_RULES=on \
  -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
  -DUDEV_RULES_GROUP=plugdev \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
  -DLIB_INSTALL_DIR:PATH=%{_libdir} \
  -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
  -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
  %if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
  %endif

%cmake_build
popd

%install
pushd host
%cmake_install
popd

# Docs, schematics, and firmware don't have any "make install", so do that manually.
mkdir -p %{buildroot}%{_docdir}/%{name} %{buildroot}%{_datadir}/%{name}
cp -a doc/* %{buildroot}%{_docdir}/%{name}
cp -a firmware-bin %{buildroot}%{_datadir}/%{name}
cp -a hardware %{buildroot}%{_datadir}/%{name}
(
  echo "Please see https://hackrf.readthedocs.io/en/latest/updating_firmware.html for"
  echo "instructions regarding updating the firmware on your HackRF device."
) > %{buildroot}%{_datadir}/%{name}/README-Fedora

%post
%{?ldconfig}
%udev_rules_update

%postun
%{?ldconfig}
%udev_rules_update

%files
%license COPYING
%doc Readme.md RELEASENOTES
%{_bindir}/hackrf_*
%{_libdir}/libhackrf.so.*
%{_udevrulesdir}/53-hackrf.rules

%files devel
%{_includedir}/libhackrf/hackrf.h
%{_libdir}/pkgconfig/libhackrf.pc
%{_libdir}/libhackrf.so
%{_libdir}/cmake/HackRF

%files firmware
%{_datadir}/%{name}/README-Fedora
%{_datadir}/%{name}/firmware-bin

%files hardware
%{_datadir}/%{name}/hardware

%files doc
%{_docdir}/%{name}/*

%changelog
%autochangelog
