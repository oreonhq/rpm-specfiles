%global source0_hash 64307b3afd4703c90a71dc017570b8a735a80f8fac380d9335195c1644469e45

# Upstream has not made releases in a while.  Track HEAD instead of trying to
# backport individual patches.
%global commit0 8473c299bc193f44c520c930a72618999ae5bb17
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Command line multimedia player based on gstreamer
Name: gst123
Version: 0.3.3
Release: 29.1.%{shortcommit0}%{?dist}
URL: http://space.twc.de/~stefan/gst123.php
Source0: http://space.twc.de/cgi-bin/gitweb.cgi?p=gst123.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tgz

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2

# We need to generate configure scripts because upstream does it at release
# time.
BuildRequires:  gcc-c++
BuildRequires: autoconf automake
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gtk2-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
BuildRequires: make

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

%files

%{_bindir}/gst123
%{_mandir}/man1/gst123.1.gz
%doc COPYING AUTHORS README NEWS

%changelog
%autochangelog
