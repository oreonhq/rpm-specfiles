%global source0_hash da113cd8f03c9ccac173566e27b66531f429b6a39e1e4b79b6927d9d81184176
Summary:        A predictive text input system
Name: dasher
Version: 5.0.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.inference.phy.cam.ac.uk/dasher/
Source0:        https://github.com/ipomoena/dasher/archive/DASHER_5_0_0_beta.tar.gz
Patch0: dasher-5.0.0-sys-stat.patch
Patch1: gnome-doc-utils-depr.patch
Patch2: 0001-Remove-extern-C-warpper-around-atspi-glib-headers-in.patch
# oreon:deps
BuildRequires:  at-spi2-core-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libXtst-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  yelp-tools
# /oreon:deps
%description
Dasher is an information-efficient text-entry interface, driven by natural
continuous pointing gestures. Dasher is a competitive text-entry system
wherever a full-size keyboard cannot be used, e.g. when operating a computer
one-handed, by joystick, touchscreen, trackball, or mouse, when operating
a computer without hands (i.e. by head-mouse or by eyetracker), or on
palmtops or wearable computers.

%prep

%setup -q -n dasher-DASHER_5_0_0_beta
%autopatch -p1
echo "5.0.0" > .tarball-version
rm  m4/glib-gettext.m4
NOCONFIGURE=1 ./autogen.sh

%build

%configure --disable-japanese
make %{?_smp_mflags}
%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/dasher.desktop
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
