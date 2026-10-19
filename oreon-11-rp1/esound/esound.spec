%global source0_hash 5eb5dd29a64b3462a29a5b20652aba7aa926742cef43577bf0796b787ca34911
Summary:        Allows several audio streams to play on a single audio device
Name:          esound
Epoch:         1
Version:       0.2.41
Release:        1%{?dist}
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://ftp.gnome.org/pub/GNOME/sources/esound
Source0:        https://ftp.gnome.org/pub/gnome/sources/esound/0.2/esound-%{version}.tar.bz2
Patch4:        esound-0.2.38-drain.patch
Patch6:        esound-0.2.38-fix-open-macro.patch
Patch7:        remove-confusing-spew.patch
Patch8:        esound-nospawn.patch
Patch9:        esound-0.2.41-libm.patch
Patch10:       esound-c99.patch
Obsoletes:     esound <= 1:0.2.36-4
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
EsounD, the Enlightened Sound Daemon, is a server process that mixes
several audio streams for playback by a single audio device. For
example, if you're listening to music on a CD and you receive a
sound-related event from ICQ, the two applications won't have to
queue for the use of your sound card.

Install esound if you'd like to let sound applications share your
audio device. You'll also need to install the audiofile package.

%package libs
Summary: Library to talk to the EsounD daemon
%description libs
The esound-libs package includes the libraries required
for applications to talk to the EsounD daemon.

%package tools
Summary: Commandline tools to talk to the EsounD daemon
%description tools
The esound-tools package includes commandline utilities
for controlling the EsounD daemon.

%package  devel
Summary:  Development files for EsounD applications
Requires: esound-libs = %{epoch}:%{version}-%{release}
Requires: audiofile-devel
Requires: alsa-lib-devel
Requires: pkgconfig
Requires: automake
%description devel
The esound-devel package includes the libraries, include files and
other resources needed to develop EsounD applications.

%package daemon
Summary: EsounD daemon
%description daemon
EsounD, the Enlightened Sound Daemon, is a server process that mixes
several audio streams for playback by a single audio device. For
example, if you're listening to music on a CD and you receive a
sound-related event from IM client, the two applications won't have to
queue for the use of your sound card.
The daemon functionality was replaced with PulseAudio (PA) and the binary
was dropped from Fedora in October 2007. However, on PA-disabled systems
the daemon functionality was completely missing and therefore
reintroduced to Fedora in June 2013 in form of subpackage.
The daemon cannot run on PA-enabled systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v -i -f
%configure --disable-static
EGREP='grep -E' make
%install
%makeinstall
rm -f %{buildroot}%{_sysconfdir}/esd.conf
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n esound-libs -f %{oreon_filedir}/esound-libs.list
%files -n esound-tools -f %{oreon_filedir}/esound-tools.list
%files -n esound-devel -f %{oreon_filedir}/esound-devel.list
%files -n esound-daemon -f %{oreon_filedir}/esound-daemon.list

%changelog

%autochangelog
