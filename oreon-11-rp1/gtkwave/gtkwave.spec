%global source0_hash 965019d74829746b5d1d382a9cf1e272246c91101d0e131f0da512c94ba5816a

Summary:	Waveform Viewer
Name:		gtkwave
Version:	3.3.126
Release:	2%{?dist}
License:	GPL-2.0-or-later
URL:		http://gtkwave.sourceforge.net/
Source0:	http://gtkwave.sourceforge.net/gtkwave-gtk3-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gcc-c++
%if 0%{?fedora>} > 40 || 0%{?rhel} > 9
BuildRequires:	gdk-pixbuf2-modules-extra
%endif
BuildRequires:	flex
BuildRequires:	gedit
BuildRequires:	gperf
BuildRequires:	hardlink
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	hicolor-icon-theme
BuildRequires:	Judy-devel
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	shared-mime-info
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
# Dependencies
Recommends:	gedit
%if 0%{?fedora>} > 40 || 0%{?rhel} > 9
Requires:	gdk-pixbuf2-modules-extra
%endif
Requires:	hicolor-icon-theme
Requires:	shared-mime-info

# Judy-devel missing on EL-8 s390x
# https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/thread/O4JISZYIVXXPIB6OZIE2TNKR2EIQZWBL/
%if 0%{?el8}
ExcludeArch:	s390x
%endif

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

# Icons and desktop entry
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

# Appdata
install -D -m 644 -p share/appdata/io.github.gtkwave.GTKWave.metainfo.xml \
	%{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml

# Include extra docs
install -p -m 644 AUTHORS %{buildroot}%{_pkgdocdir}/
install -p -m 644 ChangeLog %{buildroot}%{_pkgdocdir}/

# hardlink identical icons together
hardlink -cv %{buildroot}%{_datadir}/icons/

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml

%files
%license COPYING LICENSE.TXT
%doc %{_pkgdocdir}/
%{_bindir}/evcd2vcd
%{_bindir}/fst2vcd
%{_bindir}/fstminer
%{_bindir}/gtkwave
%{_bindir}/json2stems
%{_bindir}/lxt2miner
%{_bindir}/lxt2vcd
%{_bindir}/rtlbrowse
%{_bindir}/shmidcat
%{_bindir}/twinwave
%{_bindir}/vcd2fst
%{_bindir}/vcd2lxt
%{_bindir}/vcd2lxt2
%{_bindir}/vcd2vzt
%{_bindir}/vzt2vcd
%{_bindir}/vztminer
%{_bindir}/xml2stems
%{_datadir}/appdata/io.github.gtkwave.GTKWave.metainfo.xml
%{_datadir}/applications/gtkwave.desktop
%{_datadir}/glib-2.0/schemas/com.geda.gtkwave.gschema.xml
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/gnome/16x16/
%dir %{_datadir}/icons/gnome/16x16/mimetypes/
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/16x16/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/16x16/mimetypes/gtkwave.png
%dir %{_datadir}/icons/gnome/32x32/
%dir %{_datadir}/icons/gnome/32x32/mimetypes/
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/32x32/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/32x32/mimetypes/gtkwave.png
%dir %{_datadir}/icons/gnome/48x48/
%dir %{_datadir}/icons/gnome/48x48/mimetypes/
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-ae2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-aet.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-evcd.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-fst.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-ghw.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-gtkw.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lx2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lxt.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-lxt2.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-vcd.png
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-vnd.gtkwave-vzt.png
%{_datadir}/icons/gnome/48x48/mimetypes/gtkwave.png
%{_datadir}/icons/gtkwave_256x256x32.png
%{_datadir}/icons/gtkwave_files_256x256x32.png
%{_datadir}/icons/gtkwave_savefiles_256x256x32.png
%{_datadir}/icons/hicolor/16x16/apps/gtkwave.png
%{_datadir}/icons/hicolor/32x32/apps/gtkwave.png
%{_datadir}/icons/hicolor/48x48/apps/gtkwave.png
%{_datadir}/icons/hicolor/256x256/apps/gtkwave.png
%{_datadir}/icons/hicolor/scalable/apps/gtkwave.svg
%{_datadir}/mime/packages/x-gtkwave-extension-ae2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-aet.xml
%{_datadir}/mime/packages/x-gtkwave-extension-evcd.xml
%{_datadir}/mime/packages/x-gtkwave-extension-fst.xml
%{_datadir}/mime/packages/x-gtkwave-extension-ghw.xml
%{_datadir}/mime/packages/x-gtkwave-extension-gtkw.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lx2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lxt.xml
%{_datadir}/mime/packages/x-gtkwave-extension-lxt2.xml
%{_datadir}/mime/packages/x-gtkwave-extension-vcd.xml
%{_datadir}/mime/packages/x-gtkwave-extension-vzt.xml
%{_mandir}/man1/evcd2vcd.1*
%{_mandir}/man1/fst2vcd.1*
%{_mandir}/man1/fstminer.1*
%{_mandir}/man1/gtkwave.1*
%{_mandir}/man1/json2stems.1*
%{_mandir}/man1/lxt2miner.1*
%{_mandir}/man1/lxt2vcd.1*
%{_mandir}/man1/rtlbrowse.1*
%{_mandir}/man1/shmidcat.1*
%{_mandir}/man1/twinwave.1*
%{_mandir}/man1/vcd2fst.1*
%{_mandir}/man1/vcd2lxt.1*
%{_mandir}/man1/vcd2lxt2.1*
%{_mandir}/man1/vcd2vzt.1*
%{_mandir}/man1/vzt2vcd.1*
%{_mandir}/man1/vztminer.1*
%{_mandir}/man1/xml2stems.1*
%{_mandir}/man5/gtkwaverc.5*

%changelog
%autochangelog
