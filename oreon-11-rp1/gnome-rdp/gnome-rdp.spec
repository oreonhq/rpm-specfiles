%global source0_hash 809f7998701ae20c99f521f0d4f726445e7da239183801f486d19dbc1748926f

%define debug_package %{nil}

Name:           gnome-rdp        
Version:        0.3.1.0
Release:        39%{?dist}
Summary:        Remote Desktop Protocol client for the GNOME desktop environment

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/gnome-rdp
Source0:        http://downloads.sourceforge.net/%name/%{name}-%{version}.tar.gz
# Now the license is not include in the latest tarball
# I'll open the bug in the upstream
# wget -O COPYING-GNOME-RDP http://sourceforge.net/p/gnome-rdp/code/HEAD/tree/tags/gnome-rdp.0.2.3/COPYING?format=raw 
Source1:	COPYING-GNOME-RDP

# Mono only available on these:
ExclusiveArch: %{mono_arches}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires:	gcc
BuildRequires:  glib2-devel >= 2.15.3
BuildRequires:  gtk2-devel >= 2.12.0  
BuildRequires:  mono-devel >= 1.9
BuildRequires:  mono-data-sqlite >= 1.9
BuildRequires:  gtk-sharp2-devel >= 1.9
BuildRequires:  gnome-sharp-devel >= 2.16.1
BuildRequires:  gnome-desktop-sharp >= 2.20.1
BuildRequires:  gnome-desktop-sharp-devel >= 2.20.1
BuildRequires:  gnome-keyring-sharp-devel
BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
BuildRequires:  tigervnc
BuildRequires:  rdesktop
BuildRequires:  openssh-clients
BuildRequires:  gnome-terminal
BuildRequires:	libappindicator-sharp-devel
BuildRequires: make
Requires:       libappindicator
Requires:       rdesktop >= 1.6.0
Requires:	tigervnc
# for vncpasswd
Requires:	tigervnc-server

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

%files
%doc COPYING-GNOME-RDP
%{_bindir}/gnome-rdp
%{_libdir}/gnome-rdp
%{_datadir}/applications/gnome-rdp.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
