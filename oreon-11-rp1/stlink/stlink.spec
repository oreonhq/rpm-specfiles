%global source0_hash cff760b5c212c2cc480f705b9ca7f3828d6b9c267950c6a547002cd0a1f5f6ac
Name:           stlink
Version:        1.8.0
Release:        1%{?dist}
Summary:        STM32 discovery line Linux programmer
License:        BSD-3-Clause
Url:            https://github.com/stlink-org/stlink
Source0:        https://github.com/%{name}-org/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         6a6718b3342b6c5e282a4e33325b9f97908a0692.patch
Requires:       pkgconfig(udev)
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  pandoc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
# /oreon:deps
%description
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        gui
Summary:        GUI for STM32 discovery line linux programmer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
%description    gui
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Include files and mandatory libraries for development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|/${PROJECT_NAME}||g' src/stlink-gui/CMakeLists.txt
sed -i 's|/${PROJECT_NAME}||g' doc/man/CMakeLists.txt
sed -i 's|#add_subdirectory(cmake/pkgconfig)|add_subdirectory(cmake/pkgconfig)|' CMakeLists.txt
sed -i 's|find_package(libusb REQUIRED)|find_package(libusb REQUIRED)\nset(STLINK_LIBRARY_PATH ${CMAKE_INSTALL_LIBDIR} CACHE PATH "Main library install directory")|' CMakeLists.txt

# sed -i 's|define STLINK_SERIAL_MAX_SIZE           64|define STLINK_SERIAL_MAX_SIZE           28|' include/stlink.h
sed -i 's|static char serialnumber\[28\]|static char serialnumber\[STLINK_SERIAL_MAX_SIZE\]|' src/st-util/gdb-server.c

sed -i 's|CMP0153|CMP0042|' CMakeLists.txt

%build

%cmake3 \
    -DSTLINK_UDEV_RULES_DIR="%{_udevrulesdir}" \
    -DSTLINK_STATIC_LIB=OFF \
    -DSTLINK_GENERATE_MANPAGES=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_libdir}/lib%{name}.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
%files -f %{oreon_filedir}/main.list
%files -n stlink-gui -f %{oreon_filedir}/stlink-gui.list
%files -n stlink-devel -f %{oreon_filedir}/stlink-devel.list

%changelog

%autochangelog
