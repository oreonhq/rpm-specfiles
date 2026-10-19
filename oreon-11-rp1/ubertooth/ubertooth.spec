%global source0_hash 93a4ce7af8eddcc299d65aff8dd3a0455293022f7fea4738b286353f833bf986
%global POSTYEAR 2020
%global POSTMONTH 12
%global POSTNUM 1
Name:           ubertooth
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        25%{?dist}
Summary:        Bluetooth wireless development platform for experimentation
License:        GPL-2.0-only
URL:            https://github.com/greatscottgadgets/ubertooth
Source0:        https://github.com/greatscottgadgets/%{name}/releases/download/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}/%{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.xz
Patch:          ubertooth-0001-remove-shebang-from-library-script.patch
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-specan-ui = %{version}-%{release}
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbtbb-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package        -n lib%{name}
Summary:        Shared library for Bluetooth experimentation
Requires:       systemd-udev
%description    -n lib%{name}

This package provides the the ubertooth shared library.

%package        devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        specan-ui
Summary:        Graphical spectrum analyzer for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-QtPy python3-pyside6%{?_isa}
%description    specan-ui
The %{name}-specan-ui is a basic spectrum analysis tool for the Ubertooth.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}

# Fix udev rules
sed -i -e 's/GROUP="@UBERTOOTH_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' \
  host/misc/udev/40-ubertooth.rules.in

# Use the correct version
sed -i "s/version\s*=.*/version = '%{version}',/" \
  host/python/specan_ui/setup.py.in \
  host/python/specan_ui/setup.py

%build

%cmake \
    -DINSTALL_UDEV_RULES=on \
    -DUDEV_RULES_GROUP=plugdev \
    -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
    -S host
%cmake_build
(
  cd host/python/specan_ui
  %py3_build
)
%install
%cmake_install
(
  cd host/python/specan_ui
  %py3_install
  install -Dp -m755 ubertooth-specan-ui %{buildroot}%{_bindir}
)
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libubertooth -f %{oreon_filedir}/libubertooth.list
%files -n ubertooth-devel -f %{oreon_filedir}/ubertooth-devel.list
%files -n ubertooth-specan-ui -f %{oreon_filedir}/ubertooth-specan-ui.list

%changelog

%autochangelog
