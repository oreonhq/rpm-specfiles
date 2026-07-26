%global source0_hash 83139846247e6a0530b974e03744bb358d11f88109f231a3031815924374bb9d

# Some of the tests randomly hang, others attempt to spin up various network
# services that don't work properly in mock
%bcond_with tests

%if 0%{?fedora} > 40
%bcond_with python
%else
%bcond_without python
%endif

%global common_description %{expand:
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.}

Name:           vrpn
Version:        07.35
Release:        9%{?dist}
Summary:        Virtual-Reality Peripheral Network

# According to upstream, linking to the wiiuse (GPLv3+) and gpm (GPLv2+)
# libraries makes the vrpn server (libvrpnserver.so and vrpn_server binary, as
# well as the language bindings) GPLv3+. See
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/384#note_1606303642
# for the other licenses.
License:        BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later
URL:            https://github.com/vrpn/vrpn
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vrpn.service

# Extending range of Python version search to support two-digit minor versions
Patch:          %{url}/commit/1b4676b3cf8bbaff2f75c8e41b005401b189b2e2.patch
# Fix modbus libraries detection
Patch:          vrpn-find_modbus.patch
%if %{with python}
# Fix Python modules installation
Patch:          vrpn-python_install.patch
%endif
# Add soversion to all libraries
Patch:          vrpn-soversion.patch
# Do not install binaries only used for unit tests
Patch:          vrpn-dont-install-tests.patch

%if %{with python}
BuildRequires:  chrpath
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  perl
BuildRequires:  perl-Parse-RecDescent
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  swig

BuildRequires:  glut-devel
BuildRequires:  gpm-devel
BuildRequires:  hidapi-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libGL-devel
%ifnarch s390x
BuildRequires:  libi2c-devel
%endif
BuildRequires:  libmodbus-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb1-devel
%if %{with python}
BuildRequires:  python3-devel
%else
# Drop once f40 is EOL
Provides:       python3-vrpn = %{version}-%{release}
Obsoletes:      python3-vrpn < 07.35-5
%endif
BuildRequires:  wiiuse-devel

%description    %{common_description}

The idea is to have a PC or other host at each VR station that controls the
peripherals (tracker, button device, haptic device, analog inputs, sound, etc).
VRPN provides connections between the application and all of the devices using
the appropriate class-of-service for each type of device sharing this link. The
application remains unaware of the network topology. Note that it is possible
to use VRPN with devices that are directly connected to the machine that the
application is running on, either using separate control programs or running
all as a single program.

%package devel
Summary:        Development files for the Virtual-Reality Peripheral Network
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gpm-devel
Requires:       hidapi-devel
Requires:       jsoncpp-devel
Requires:       libudev-devel
Requires:       libusb1-devel
Requires:       wiiuse-devel

%description devel %{common_description}

This package contains development files for the VRPN libraries.

%package doc
Summary:        Developer's documentation for VRPN
BuildArch:      noarch

%description doc %{common_description}

This package contains generated VRPN source code documentation.

%if %{with python}
%package -n python3-%{name}
Summary:        Python 3 bindings for the Virtual-Reality Peripheral Network

%description -n python3-%{name} %{common_description}

This package contains Python 3 bindings for the VRPN libraries.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix binaries path
sed -i 's:/usr/local/bin:%{_bindir}:g' vrpn_Connection.C

%build
%cmake \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DVRPN_GPL_SERVER=ON \
    -DBUILD_TESTING=ON \
%if %{with python}
    -DVRPN_BUILD_PYTHON_HANDCODED_3X=ON \
    -DVRPN_PYTHON_INSTALL_DIR=%{python3_sitearch} \
%endif
    %{nil}
%cmake_build
%cmake_build --target doc

%install
%cmake_install

%if %{with python}
# Install Python module and strip broken rpath
chrpath -d %{_vpath_builddir}/python/vrpn.so
install -Dpm0755 -t %{buildroot}%{python3_sitearch} %{_vpath_builddir}/python/vrpn.so
%endif

# Install systemd service
install -Dpm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Move sample config out of the way
mv %{buildroot}/%{_datadir}/%{name}-%{version}/%{name}.cfg.sample .

%if %{with tests}
%check
%ctest
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc ChangeLog %{name}.cfg.sample
%license README.Legal
%{_libdir}/lib%{name}*.so.07{,.*}
%{_libdir}/libgpsnmea.so.07{,.*}
%{_libdir}/libquat.so.07{,.*}
%{_bindir}/%{name}*
%{_bindir}/run_auxiliary_logger
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_unitdir}/%{name}.service

%files devel
%{_includedir}/latLonCoord.h
%{_includedir}/nmeaParser.h
%{_includedir}/quat.h
%{_includedir}/utmCoord.h
%{_includedir}/%{name}*
%{_libdir}/lib%{name}*.so
%{_libdir}/libgpsnmea.so
%{_libdir}/libquat.so

%files doc
%doc Format_Of_Protocol.txt
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.map
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.md5

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/*.so
%endif

%changelog
%autochangelog
