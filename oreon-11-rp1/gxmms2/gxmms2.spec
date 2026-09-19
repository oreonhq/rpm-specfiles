%global source0_hash fa3fef28935d29665bd7d788db2dcd131e177c7d9ee71423c096a410bfc05a27

#gkrellm has c23 issues so...

%global optflags %{optflags} -std=gnu17

Name:		gxmms2
Summary: 	A graphical audio player
Version:	0.7.1
Release:	34%{?dist}
License:	GPL-2.0-only
# If we need to use a git checkout to support an xmms2 release...
# git clone git://git.xmms.se/xmms2/gxmms2.git
# tar cvfj gxmms2-20090811git.tar.bz2 gxmms2
# Source0:      %%{name}-20090811git.tar.bz2
Source0:	http://wejp.k.vu/projects/xmms2/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		gxmms2-0.7.0-implicit-DSO-libX11.patch
Patch1:		gxmms2-0.7.1-xmms2-0.9.3.patch
Patch2:		gxmms2-0.7.1-stdio.patch
Patch3:		gxmms2-0.7.1-c23.patch
URL:		http://wejp.k.vu/projects/xmms2/
BuildRequires:	xmms2-devel >= 0.7, gtk2-devel, pango-devel, atk-devel
BuildRequires:	desktop-file-utils, gcc

%description
gxmms2 is a GTK2 based XMMS2 client, written in C. Its main window is small 
and simple. It includes a playlist editor and a file details dialog.

%package -n gkrellxmms2
Summary:	Gkrellm2 plugin client for XMMS2 
BuildRequires:	gkrellm-devel
BuildRequires: make
Requires:	gkrellm

%description -n gkrellxmms2
gkrellxmms2 is a gkrellm2 plugin for XMMS2. It has a title scroller with a 
position marker and five buttons for playback control. The position marker 
can be moved with the mouse to seek in the current track. The M button 
opens a menu with two items for opening a trackinfo dialog and the media 
library window.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .DSO
%patch -P1 -p1 -b .093
%patch -P2 -p1 -b .stdio
%patch -P3 -p1 -b .c23
sed -i 's|/lib/|/%{_lib}/|g' Makefile

%build
make %{?_smp_mflags} CC="gcc %{optflags}"

%install
make PREFIX=%{buildroot}%{_prefix} KRELLPREFIX=%{buildroot}%{_prefix} install

mkdir -p %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/gxmms2/gxmms2_mini.xpm %{buildroot}/%{_datadir}/pixmaps/gxmms2.xpm
# Don't need anything else in these dirs
rm -rf %{buildroot}%{_datadir}/gxmms2 %{buildroot}%{_datadir}/gkrellxmms2

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc CHANGELOG COPYING README
%{_bindir}/%{name}*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/*.desktop

%files -n gkrellxmms2
%doc CHANGELOG COPYING README
%{_libdir}/gkrellm2/plugins/gkrellxmms2.so

%changelog
%autochangelog
