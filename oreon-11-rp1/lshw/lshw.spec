%undefine __cmake_in_source_build

%bcond_without gui

Summary:       Hardware lister
Name:          lshw
Version:       B.02.20
Release:       11%{?dist}
License:       GPL-2.0-only
URL:           https://github.com/lyonel/lshw
Source0:       https://github.com/lyonel/lshw/archive/refs/tags/%{version}.tar.gz
Source1:       https://salsa.debian.org/openstack-team/third-party/lshw/raw/debian/stein/debian/patches/lshw-gtk.1
Patch:         lshw-B.02.20-209f83.patch
Patch:         lshw-B.02.18-scandir.patch
Patch:         lshw-B.02.20-cmake.patch
# oreon url source checksums begin
%global source0_sha256 6b8346a89fb0f0f1798e66f6a707a881d38b9b3a67256b30fc4628dac09f291a
%global source0_file B.02.20.tar.gz
# oreon url source checksums end
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
%if %{with gui}
BuildRequires: gtk3-devel >= 3.24
BuildRequires: libappstream-glib
%endif
BuildRequires: ninja-build
BuildRequires: python3-devel
BuildRequires: sqlite-devel
Requires:      hwdata
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/B.02.20.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6b8346a89fb0f0f1798e66f6a707a881d38b9b3a67256b30fc4628dac09f291a" || { echo "oreon: Source0 SHA256 mismatch for B.02.20.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

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
# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/*/

%check
%if %{with gui}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%endif

# check json output is valid
%{_vpath_builddir}/src/lshw -json \
    -disable usb -disable pcmcia -disable isapnp \
    -disable ide -disable scsi -disable dmi -disable memory \
    -disable cpuinfo 2>/dev/null | %{__python3} -m json.tool

#files -f %{name}.lang
%files
%license COPYING
%doc README.md
%{_mandir}/man1/lshw.1*
%{_sbindir}/lshw

%if %{with gui}
%files gui
%license COPYING
%{_bindir}/lshw-gui
%{_sbindir}/gtk-lshw
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/lshw-gui
%endif
%{_mandir}/man1/lshw-gui.1*
%dir %{_datadir}/lshw
%{_datadir}/lshw/artwork
%dir %{_datadir}/lshw/ui
%{_datadir}/lshw/ui/gtk-lshw.ui
%{_datadir}/pixmaps/gtk-lshw.svg
%{_datadir}/applications/gtk-lshw.desktop
%{_datadir}/appdata/gtk-lshw.appdata.xml
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - B.02.20-11
- Prepare for Oreon 11 (RP1)
