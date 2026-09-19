%global source0_hash 3f5d7eaf5daa7dcf3843a01e239cea312045ded03dd77b364fa1082b9356968a

Summary:    Telnet client designed for BBS browsing
Name:       pcmanx-gtk2
Version:    1.3
Release:    24%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Source0:    https://github.com/pcman-bbs/pcmanx/releases/download/%{version}/%{name}-%{version}.tar.xz
URL:        https://github.com/pcman-bbs/pcmanx
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel libXft-devel libtool-ltdl-devel
BuildRequires:  libnotify-devel >= 0.7.0
BuildRequires:  desktop-file-utils gettext
BuildRequires:  intltool

%description
An easy-to-use telnet client mainly targets BBS users.

PCMan X is a newly developed GPL'd version of PCMan, a full-featured
famous BBS client formerly designed for MS Windows only.  It aimed to
be an easy-to-use yet full-featured telnet client facilitating BBS
browsing with the ability to process double-byte characters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

tar Jfx %{SOURCE0}
%setup -qDT
# remove the bundled libltdl
rm -fr libltdl
sed -i -e 's/libltdl//' Makefile.in

%build
%configure --enable-proxy --enable-libnotify --enable-iplookup --enable-wget
make %{?_smp_mflags}

%install
make install INSTALL="install -c -p" DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/pcmanx.desktop

%find_lang pcmanx

%files -f pcmanx.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pcmanx/
%{_datadir}/pixmaps/*
%{_mandir}/man1/pcmanx.1*

%changelog
%autochangelog
