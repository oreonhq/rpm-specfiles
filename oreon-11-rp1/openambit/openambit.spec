%global source0_hash 93303be6a613b3a92fa8742cceb50cf61dbe21588c6e34c70c60d802102fb05c
Name:           openambit
Version:        0.5
Release:        1%{?dist}
Summary:        Open software for the Suunto Ambit(2)
License:        GPL-3.0-or-later
URL:            http://openambit.org/
Source0:        https://github.com/%{name}project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         openambit_unbundle-hidapi.patch
Patch1:         openambit_python3.patch
Patch2:         openambit_gcc10.patch
Patch3:         openambit_cmakever.patch
%if 0%{?with_wireshark:1}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  systemd-devel
BuildRequires:  wireshark-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Openambit is application for downloading moves from the Suunto
Ambit(2) outdoor watches, and synchronizing them with the
movescount website.

%package libs
Summary:        Libraries for %{name}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openambit-libs -f %{oreon_filedir}/openambit-libs.list
%files -n openambit-devel -f %{oreon_filedir}/openambit-devel.list
%files -n openambit-wireshark -f %{oreon_filedir}/openambit-wireshark.list

%changelog

%autochangelog
