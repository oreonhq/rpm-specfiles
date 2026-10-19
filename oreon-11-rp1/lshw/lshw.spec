%global source1_hash 24f6710eb0728e84370b4acececfab1bda919be79c5ae28e7c30802ee8adac25
%global source0_hash 6b8346a89fb0f0f1798e66f6a707a881d38b9b3a67256b30fc4628dac09f291a
%undefine __cmake_in_source_build
%bcond_without gui
Summary:        Hardware lister
Name:          lshw
Version:       B.02.20
Release:        11%{?dist}
License:       GPL-2.0-only
URL:           https://github.com/lyonel/lshw
Source0:        https://github.com/lyonel/lshw/archive/refs/tags/%{version}.tar.gz#/lshw-B.02.20.tar.gz
Source1:       https://salsa.debian.org/openstack-team/third-party/lshw/raw/debian/stein/debian/patches/lshw-gtk.1
Patch:         lshw-B.02.20-209f83.patch
Patch:         lshw-B.02.18-scandir.patch
Patch:         lshw-B.02.20-cmake.patch
%if %{with gui}
%endif
Requires:      hwdata
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86
systems and on some PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%if %{with gui}
%package       gui
Summary:       Graphical hardware lister
Requires:      polkit
Requires:      %{name} = %{version}-%{release}
%description   gui
Graphical frontend for the hardware lister (lshw) tool. If desired,
hardware information can be saved to file in plain, XML or HTML
format.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with gui}
%global gui_config -DGUI=ON
%else
%global gui_config -DGUI=OFF
%endif
%cmake -DNOLOGO=ON -DHWDATA=OFF -DPOLICYKIT=ON -DSQLITE=ON -DBUILD_SHARED_LIBS=OFF %{gui_config} -GNinja
%cmake_build
%install
%cmake_install
%if %{with gui}
install -m0644 -D %{SOURCE1} %{buildroot}%{_mandir}/man1/lshw-gui.1
%if "%{_sbindir}" != "%{_bindir}"
ln -s gtk-lshw %{buildroot}%{_sbindir}/lshw-gui
%endif
%endif
rm -rf %{buildroot}%{_datadir}/locale/*/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with gui}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%endif
%{_vpath_builddir}/src/lshw -json \
    -disable usb -disable pcmcia -disable isapnp \
    -disable ide -disable scsi -disable dmi -disable memory \
    -disable cpuinfo 2>/dev/null | %{__python3} -m json.tool
%files -f %{oreon_filedir}/main.list
%files -n lshw-gui -f %{oreon_filedir}/lshw-gui.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - B.02.20-11
- Prepare for Oreon 11 (RP1)
