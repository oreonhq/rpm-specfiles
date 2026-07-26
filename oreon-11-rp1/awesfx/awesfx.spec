%global source0_hash 04d47e07a01a82ee59ca0c37db4b77f97d1734cacfb08e02e5a4277671d5a54b

Name:          awesfx
Version:       0.5.1c
Release:       36%{?dist}
Summary:       Utility programs for the AWE32/Emu10k1 sound driver
URL:           http://www.alsa-project.org/~iwai/awedrv.html
Source0:       http://ftp.suse.com/pub/people/tiwai/awesfx/awesfx-%{version}.tar.bz2
Source1:       udev-soundfont
Source2:       load-soundfont
Source3:       41-soundfont.rules
Patch0:        rename-getline-to-parseline.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later

BuildRequires:  gcc
BuildRequires: alsa-lib-devel >= 1.0.0
BuildRequires: systemd
BuildRequires: make

%description
The awesfx package contains various utility programs for controlling the 
AWE32/Emu10k1 sound driver. AWESFX includes asxfload and sfxload, the 
soundfont loaders; setfx, the chorus/reverb effect loader; aweset, a 
controller for setting parameters; and programs for converting soundfonts 
to text.

If you use an AWE32 or Emu10k1 sound driver you should install the awesfx 
package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1

%build
%configure CFLAGS="$RPM_OPT_FLAGS"
make  %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/alsa.d/udev-soundfont
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/alsa.d/load-soundfont
install -Dp -m 644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/41-soundfont.rules
mkdir -p %{buildroot}%{_datadir}/soundfonts
mv %{buildroot}%{_datadir}/sounds/sf2/*.bnk %{buildroot}%{_datadir}/soundfonts
rm -rf %{buildroot}%{_datadir}/sounds
rm -f samples/Makefile*

%files
%license COPYING
%doc AUTHORS ChangeLog README SBKtoSF2.txt samples/README-bank samples/setfx-sample.cfg
%{_bindir}/*
%{_sysconfdir}/alsa.d
%{_udevrulesdir}/41-soundfont.rules
%{_datadir}/soundfonts/
%{_mandir}/man*/*.1.gz

%changelog
%autochangelog
