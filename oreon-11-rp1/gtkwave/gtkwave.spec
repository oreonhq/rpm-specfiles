%global source0_hash 817e197fc1808f8aac3543c2c2f9683cb01368c91192b8eae5af58070ef1d1f8
Summary:        Waveform Viewer
Name:		gtkwave
Version:	3.3.128
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		http://gtkwave.sourceforge.net/
Source0:        http://gtkwave.sourceforge.net/gtkwave-gtk3-%{version}.tar.gz
Recommends:	gedit
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
%if 0%{?el8}
ExcludeArch:	s390x
%endif
# oreon:deps
BuildRequires:  Judy-devel
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gedit
BuildRequires:  gperf
BuildRequires:  hardlink
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  shared-mime-info
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
GTKWave is a waveform viewer that can view VCD files produced by most Verilog
simulation tools, as well as LXT files produced by certain Verilog simulation
tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtkwave-gtk3-%{version}

%build

%configure \
	--disable-dependency-tracking \
	--disable-mime-update \
	--enable-gtk3 \
	--enable-judy \
	--with-gsettings \
	--with-tirpc
%{make_build}
%install
%{make_install} pkgdatadir=%{_pkgdocdir}
desktop-file-install --vendor "" --dir %{buildroot}%{_datadir}/applications \
	share/applications/gtkwave.desktop
install -D -m 644 -p share/icons/gnome/16x16/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/32x32/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
install -D -m 644 -p share/icons/gnome/48x48/mimetypes/gtkwave.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png
install -D -m 644 -p share/icons/gtkwave_256x256x32.png \
	%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/gtkwave.png
install -D -m 644 -p share/appdata/io.github.gtkwave.GTKWave.metainfo.xml \
	%{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml
install -p -m 644 AUTHORS %{buildroot}%{_pkgdocdir}/
install -p -m 644 ChangeLog %{buildroot}%{_pkgdocdir}/
hardlink -cv %{buildroot}%{_datadir}/icons/
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
