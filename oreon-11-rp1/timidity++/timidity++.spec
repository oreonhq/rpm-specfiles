%global source0_hash 9eaf4fadb0e19eb8e35cd4ac16142d604c589e43d0e8798237333697e6381d39

# Workaround LTO breaking alsa symbol versioning, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1993671
# https://bugzilla.redhat.com/show_bug.cgi?id=2087786
# https://bugzilla.redhat.com/show_bug.cgi?id=2087904
%global _lto_cflags %nil

Summary: A software wavetable MIDI synthesizer
Name: timidity++
Version: 2.15.0
Release: 16%{?dist}
Source0: http://downloads.sourceforge.net/timidity/TiMidity++-2.15.0.tar.xz
Source1: timidity.desktop
Source2: timidity-xaw.desktop
# Select patches from Debian. Debian patches 0004 and 0005 are *wrong* AFAICT:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=999709
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=999710
# 0006, 0007, 0008, 0011 and 0012 are not applicable with the 2.15.0 release
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
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildRequires: make gcc
BuildRequires: alsa-lib-devel ncurses-devel gtk2-devel Xaw3d-devel
BuildRequires: libao-devel libvorbis-devel flac-devel speex-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils
Requires: soundfont2-default hicolor-icon-theme

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
# gtk2 GtkItemFactoryCallback is not compatible with latest C
export EXTRACFLAGS="$RPM_OPT_FLAGS -std=gnu11 -DCONFIG_FILE=\\\"%{_sysconfdir}/timidity++.cfg\\\""
# Note the first argument to --enable-audio is the default output, and
# we use libao to get pulse output
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

%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_mandir}/*/*

%files GTK-interface
%{_libdir}/%{name}/if_gtk.so
%{_datadir}/applications/timidity.desktop
%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm

%files Xaw3D-interface
%{_libdir}/%{name}/if_xaw.so
%{_datadir}/applications/timidity-xaw.desktop
%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm

%changelog
%autochangelog
