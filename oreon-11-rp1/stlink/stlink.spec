%global source0_hash cff760b5c212c2cc480f705b9ca7f3828d6b9c267950c6a547002cd0a1f5f6ac

# %global gitcommit_full f82700623127538c8cf5cddbbeba6afc12d3adbf
# %global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
# %global date 20200420

Name:           stlink
Version:        1.8.0
# Release:        0.1.%{date}git%{gitcommit}%{?dist}
Release:        3%{?dist}
Summary:        STM32 discovery line Linux programmer
License:        BSD-3-Clause

Url:            https://github.com/stlink-org/stlink
# Source0:        %{url}/tarball/%{gitcommit_full}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         6a6718b3342b6c5e282a4e33325b9f97908a0692.patch

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  desktop-file-utils
BuildRequires:  pandoc
Requires:       pkgconfig(udev)

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
# Remove static library
rm %{buildroot}%{_libdir}/lib%{name}.a

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%config(noreplace) %{_sysconfdir}/modprobe.d/%{name}*
%{_bindir}/st-*
%{_datadir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/st-*.1*
%{_udevrulesdir}/49-%{name}*

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/%{name}-gui.ui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-gui.svg

%files devel
%{_includedir}/%{name}*
# %{_includedir}/stm32.h
%{_libdir}/lib%{name}.so
# %{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
