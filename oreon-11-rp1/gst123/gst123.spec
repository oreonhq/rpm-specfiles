%global source0_hash 64307b3afd4703c90a71dc017570b8a735a80f8fac380d9335195c1644469e45
%global commit0 8473c299bc193f44c520c930a72618999ae5bb17
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Summary:        Command line multimedia player based on gstreamer
Name: gst123
Version: 0.3.3
Release:        1%{?dist}
URL: http://space.twc.de/~stefan/gst123.php
Source0:        http://space.twc.de/cgi-bin/gitweb.cgi?p=%{name}.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tgz
License: LicenseRef-Callaway-LGPLv2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk2-devel
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description

The program gst123 is designed to be a more flexible command line player 
in the spirit of ogg123 and mpg123, based on gstreamer. It plays all file 
formats gstreamer understands, so if you have a music collection which 
contains different file formats, you can use gst123 to play all your 
music files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{shortcommit0}
./autogen.sh

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
