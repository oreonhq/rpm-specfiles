%global source0_hash 809f7998701ae20c99f521f0d4f726445e7da239183801f486d19dbc1748926f
%define debug_package %{nil}
Name:           gnome-rdp        
Version:        0.3.1.0
Release:        39%{?dist}
Summary:        Remote Desktop Protocol client for the GNOME desktop environment
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/gnome-rdp
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	COPYING-GNOME-RDP
ExclusiveArch: %{mono_arches}
ExcludeArch:   %{ix86}
Requires:       libappindicator
Requires:       rdesktop >= 1.6.0
Requires:	tigervnc
Requires:	tigervnc-server
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gnome-desktop-sharp
BuildRequires:  gnome-desktop-sharp-devel
BuildRequires:  gnome-keyring-sharp-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gnome-terminal
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libappindicator-sharp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  openssh-clients
BuildRequires:  perl(XML::Parser)
BuildRequires:  rdesktop
BuildRequires:  tigervnc
# /oreon:deps
%description
gnome-rdp is a Remote Desktop Protocol client for the GNOME desktop
environment. It supports RDP, VNC and SSH. Configured sessions can be saved to
the built in list.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE1} .
sed -i 's/tight-vncviewer/vncviewer/' Sessions/SessionCollection.cs
sed -i 's/pkglib_SCRIPTS/programfiles_SCRIPTS/' Makefile.include
sed -i "s#gmcs#mcs#g" Makefile.*
sed -i "s#gmcs#mcs#g" gnome-rdp.make
sed -i "s#gmcs#mcs#g" configure*

%build

%configure 
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	Menu/gnome-rdp.desktop 
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 Menu/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
