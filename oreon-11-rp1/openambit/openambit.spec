%global source0_hash 93303be6a613b3a92fa8742cceb50cf61dbe21588c6e34c70c60d802102fb05c

#global commit 042e1019d31e89ba4acf8fe08bfdc9089bbace0f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           openambit
Version:        0.5
Release:        17%{?commit:.git%shortcommit}%{?dist}
Summary:        Open software for the Suunto Ambit(2)

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://openambit.org/
Source0:        https://github.com/openambitproject/openambit/archive/%{?commit:%commit}%{!?commit:%version}/openambit-%{?commit:%shortcommit}%{!?commit:%version}.tar.gz

# Unbundle hidapi (see also %%prep)
Patch0:         openambit_unbundle-hidapi.patch
# Port scripts to python3
Patch1:         openambit_python3.patch
# Add missing extern declarations (GCC10 FTBFS)
Patch2:         openambit_gcc10.patch
# Raise CMake minimum version to 3.5
Patch3:         openambit_cmakever.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  systemd-devel
BuildRequires:  hidapi-devel
BuildRequires:  python3
BuildRequires:  zlib-devel
%if 0%{?with_wireshark:1}
BuildRequires:  wireshark-devel
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description
Openambit is application for downloading moves from the Suunto
Ambit(2) outdoor watches, and synchronizing them with the
movescount website.

%package libs
Summary:        Libraries for %{name}
# For %%{_sysconfdir}/udev/rules.d/ ownership
Requires:       systemd

%description libs
The %{name}-libs package contains libraries for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?with_wireshark:1}
%package        wireshark
Summary:        Wireshark dissector for %{name}
Requires:       wireshark%{?_isa} >= 1.12.6-3
License:        BSD

%description    wireshark
The %{name}-wireshark package contains the Wireshark dissector for %{name},
which parses pcap-files made with usbpcap.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{?commit:%commit}%{!?commit:%version}

# Remove exec permissions since it is installed as %%doc
chmod -x tools/movescountXmlDiff.pl

# Remove bundled hidapi files
rm -rf src/libambit/hidapi

%build
%cmake \
  -DCMAKE_INSTALL_UDEVRULESDIR=%{_udevrulesdir} \
  -DUSE_QT5=ON \
%if 0%{?with_wireshark}
  -DBUILD_EXTRAS=ON \
  -DCMAKE_INSTALL_WIRESHARKPLUGINSDIR=%{_libdir}/wireshark/plugins/ \
%endif
%cmake_build

%install
%cmake_install
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%ldconfig_scriptlets libs

%files
%license src/openambit/COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files libs
%license src/libambit/COPYING
%{_libdir}/libambit.so.*
%{_libdir}/libmovescount.so.*
%{_udevrulesdir}/libambit.rules

%files devel
%doc src/example/ambitconsole.c
%doc tools/*
%{_includedir}/libambit.h
%{_includedir}/movescount/
%{_libdir}/libambit.so
%{_libdir}/libmovescount.so

%if 0%{?with_wireshark:1}
%files wireshark
%license wireshark_dissector/COPYING
%{_libdir}/wireshark/plugins/ambit.so
%endif

%changelog
%autochangelog
