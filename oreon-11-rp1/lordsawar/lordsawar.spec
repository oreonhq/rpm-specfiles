%global source0_hash none

Name:           lordsawar
Version:        0.3.2
Release:        18%{?dist}
Summary:        Turn-based strategy game in a fantasy setting

# This is used for prereleases and such
# If not prerelease, set this to the version macro
%global rel_version %{version}

# Some documentation is GFDLv1.1+
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://savannah.nongnu.org/projects/%{name}
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{rel_version}.tar.gz
# Use a local copy of the manual, rather than a remote one, for help
# Except we don't have a copy of the movie demo that doesn't come with
# the source.
# FIXME(hguemar): patch needs to be refreshed, disabled to rebuild against newer gstreamermm
#Patch1:         lordsawar-local-manual.patch
#Patch2:         0001-Migrate-to-Gstreamermm-1.0-API.patch
#Patch3:         0002-Fix-compilation-with-GCC-7-never-compare-pointers-to.patch
# Reserve doesn't actually make vectors bigger, it is used to make resizing 
# more efficient. resize is needed to actually make it bigger.
Patch4:         assert.patch
# The following is a fix for something gcc starting flagging related to
# array initialization in a constructor. I don't think the flagged
# reference was even needed, since the name was copied over explicitly
# in the constructor.
Patch5:		lordsawar-armynameinit.patch

BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel gettext desktop-file-utils gstreamermm-devel
BuildRequires:  libarchive-devel intltool libxslt-devel docbook-utils
BuildRequires:  libxml++-devel libtool
BuildRequires: make

%description
LordsAWar! is a turn-based strategy game set in a fantasy setting.

%prep
%setup -qn %{name}-%{rel_version}
#%patch1
#%patch2 -p1
#%patch3 -p1
%patch -P4
%patch -P5 -p0
sed -i.orig -e "s/Comment=Play a clone of Warlords II/Comment=Play a turn-based strategy game/" dat/lordsawar.desktop.in.in

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}-appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-import
%{_bindir}/%{name}-upgrade-file
%{_bindir}/%{name}-game-host-client
%{_bindir}/%{name}-game-host-server
%{_bindir}/%{name}-game-list-client
%{_bindir}/%{name}-game-list-server
#%%{_datadir}/gnome/help/%%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man6/lordsawar-game-host-client.6*
%{_mandir}/man6/lordsawar-game-host-server.6*
%{_mandir}/man6/lordsawar-game-list-client.6*
%{_mandir}/man6/lordsawar-game-list-server.6*
%{_mandir}/man6/lordsawar-import.6*
%{_mandir}/man6/lordsawar.6*

%changelog
%autochangelog
