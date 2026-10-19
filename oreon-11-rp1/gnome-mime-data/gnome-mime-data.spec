%global source0_hash 37196b5b37085bbcd45c338c36e26898fe35dd5975295f69f48028b1e8436fd7
Summary:        MIME type data files for GNOME desktop
Name: gnome-mime-data
Version: 2.18.0
Release:        37%{?dist}
URL: http://www.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-mime-data/2.18/%{name}-%{version}.tar.bz2
License: GPL-1.0-or-later
BuildArch: noarch
Patch0: gnome-mime-data-2.2.0-openoffice.patch
Patch1: gnome-mime-data-2.2.0-rpminstall.patch
Patch2: gnome-mime-data-2.3.2-nohtmlcomponent.patch
Patch3: gnome-mime-data-2.4.1-default-applications.patch
Patch5: gnome-mime-data-2.4.0-OOo-startup.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
gnome-mime-data provides the file type recognition data files for gnome-vfs

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .openoffice
%patch -P1 -p1 -b .rpminstall
%patch -P2 -p1 -b .nohtmlcomponent
%patch -P3 -p1 -b .default-applications
%patch -P5 -p1 -b .OOo-startup

## be sure .keys is regenerated from patched .keys.in
rm gnome-vfs.keys

## no command line apps as bindings
perl -pi -e 's/,mpg123//g' gnome-vfs.keys.in
perl -pi -e 's/mpg123//g' gnome-vfs.keys.in

%build

%configure 
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
