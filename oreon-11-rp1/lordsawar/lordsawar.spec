%global source0_hash ee9f8f2f0e07595ae5fbdb6259bfbc1fb9c88d17eeda723c8e23428a0bcda7b1
Name:           lordsawar
Version:        0.3.2
Release:        18%{?dist}
Summary:        Turn-based strategy game in a fantasy setting
%global rel_version %{version}
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://savannah.nongnu.org/projects/%{name}
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch4:         assert.patch
Patch5:		lordsawar-armynameinit.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gstreamermm-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  libarchive-devel
BuildRequires:  libtool
BuildRequires:  libxml++-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
