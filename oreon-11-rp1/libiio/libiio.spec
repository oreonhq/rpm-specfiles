%global source0_hash fb445fb860ef1248759f45d4273a4eff360534480ec87af64c6b8db3b99be7e5

Name:          libiio
Version:       0.26
Release:       8%{?dist}
Summary:       Library for Industrial IO
License:       LGPL-2.0-or-later
URL:           https://analogdevicesinc.github.io/libiio/
Source0:       https://github.com/analogdevicesinc/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: avahi-devel
BuildRequires: bison
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libaio-devel
BuildRequires: libusb1-devel
BuildRequires: libxml2-devel
BuildRequires: man2html
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme

%description
Library for interfacing with Linux IIO devices

libiio is used to interface to Linux Industrial Input/Output (IIO) Subsystem.
The Linux IIO subsystem is intended to provide support for devices that in some 
sense are analog to digital or digital to analog converters (ADCs, DACs). This 
includes, but is not limited to ADCs, Accelerometers, Gyros, IMUs, Capacitance 
to Digital Converters (CDCs), Pressure Sensors, Color, Light and Proximity 
Sensors, Temperature Sensors, Magnetometers, DACs, DDS (Direct Digital 
Synthesis), PLLs (Phase Locked Loops), Variable/Programmable Gain Amplifiers 
(VGA, PGA), and RF transceivers.

%package utils
Summary: Utilities for Industrial IO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for accessing IIO using libiio

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package doc
Summary: Development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for development with %{name}.

%package -n python3-iio
Summary: Python 3 bindings for Industrial IO (libiio)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-iio
Python 3 bindings for Industrial IO

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's#${LIBIIO_VERSION_MAJOR}-doc##' CMakeLists.txt
sed -i 's#DESTINATION ${CMAKE_HTML_DEST_DIR}/${CMAKE_API_DEST_DIR}#DESTINATION ${CMAKE_HTML_DEST_DIR}##' CMakeLists.txt

%build
%cmake -DPYTHON_BINDINGS=on -DWITH_DOC=on -DWITH_MAN=on \
       -DUDEV_RULES_INSTALL_DIR=%{_udevrulesdir}

%cmake_build

%install
%cmake_install

#hack: Fix man locations
mv %{buildroot}%{_mandir}/man1/man/* %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/man3/man/* %{buildroot}%{_mandir}/man3
rmdir %{buildroot}%{_mandir}/man1/man %{buildroot}%{_mandir}/man3/man
#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%files
%license COPYING.txt
%{_libdir}/%{name}.so.*
%{_mandir}/man3/libiio*
%{_udevrulesdir}/90-libiio.rules

%files utils
%{_bindir}/iio_*
%{_bindir}/iiod
%{_mandir}/man1/iio*

%files devel
%{_includedir}/iio.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc %{_docdir}/%{name}

%files -n python3-iio
%{python3_sitelib}/__pycache__/iio*
%{python3_sitelib}/iio.py
%{python3_sitelib}/pylibiio*

%changelog
%autochangelog
