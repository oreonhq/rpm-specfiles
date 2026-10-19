%global source0_hash 9eaf4fadb0e19eb8e35cd4ac16142d604c589e43d0e8798237333697e6381d39
%global _lto_cflags %nil
Summary:        A software wavetable MIDI synthesizer
Name: timidity++
Version: 2.15.0
Release:        1%{?dist}
Source0:        http://downloads.sourceforge.net/timidity/TiMidity++-2.15.0.tar.xz
Source1: timidity.desktop
Source2: timidity-xaw.desktop
Patch01: 0001-don-t-url_unexpand_home_dir-when-opening-a-file.patch
Patch02: 0002-improve-error-message.patch
Patch03: 0003-use-exponentional-backup-select-in-interface-alsaseq.patch
Patch09: 0009-Debian-adaptions-of-manpages.patch
Patch10: 0010-Pass-LDFLAGS-to-addon-linking.patch
Patch13: 0013-readmidi-Fix-division-by-zero.patch
Patch14: 0014-resample-Fix-out-of-bound-access-in-resamplers.patch
Patch15: 0015-timidity-no_date.patch
Patch16: timidity++-configure-c99.patch
URL: http://timidity.sourceforge.net
License: GPL-2.0-only
Requires: soundfont2-default hicolor-icon-theme
# oreon:deps
BuildRequires:  Xaw3d-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libao-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  speex-devel
# /oreon:deps
%description
TiMidity++ is a MIDI format to wave table format converter and
player. Install timidity++ if you'd like to play MIDI files and your
sound card does not natively support wave table format.

%package        GTK-interface
Summary:        GTK user interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    GTK-interface
The %{name}-GTK-interface package contains a GTK based UI for %{name}.

%package        Xaw3D-interface
Summary:        Xaw3D user interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    Xaw3D-interface
The %{name}-Xaw3D-interface package contains a Xaw3D based UI for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n TiMidity++-2.15.0
autoreconf -ivf

%build

export EXTRACFLAGS="$RPM_OPT_FLAGS -std=gnu11 -DCONFIG_FILE=\\\"%{_sysconfdir}/timidity++.cfg\\\""
%configure --disable-dependency-tracking \
  --with-module-dir=%{_libdir}/%{name} \
  --enable-interface=ncurses,vt100,alsaseq,server,network,gtk,xaw \
  --enable-dynamic=gtk,xaw \
  --enable-audio=ao,alsa,oss,jack,vorbis,speex,flac
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 interface/pixmaps/timidity.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
