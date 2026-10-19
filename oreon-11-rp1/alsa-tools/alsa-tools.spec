%global source0_hash 800498d35233672ef67f4bf74cc6e1d37e1fe70c0540e2d2e062f2319e7b5df7
%ifarch ppc ppc64
%{?!_without_tools:     %global builddirstools as10k1 echomixer envy24control hdspconf hdspmixer hwmixvolume rmedigicontrol sbiload sscape_ctl us428control hda-verb hdajackretask hdajacksensetest }
%else
%{?!_without_tools:     %global builddirstools as10k1 echomixer envy24control hdspconf hdspmixer hwmixvolume rmedigicontrol sbiload sb16_csp sscape_ctl us428control hda-verb hdajackretask hdajacksensetest }
%endif
%{?!_without_firmware:  %global builddirsfirmw hdsploader mixartloader usx2yloader vxloader }
%{?!_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        Specialist tools for ALSA
Name:           alsa-tools
Version:        1.2.15
Release:        4%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.alsa-project.org/
Source0:        https://www.alsa-project.org/files/pub/tools/%{name}-%{version}.tar.bz2
Source1:        90-alsa-tools-firmware.rules
Patch1:         hwmixvolume-python.patch
%if 0%{!?_without_tools:1}
Requires:       xorg-x11-fonts-misc
Requires:       python3-alsa
%endif
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  make
# /oreon:deps
%description
This package contains several specialist tools for use with ALSA, including
a number of programs that provide access to special hardware facilities on
certain sound cards.

* as10k1 - AS10k1 Assembler
%ifnarch ppc ppc64
* cspctl - Sound Blaster 16 ASP/CSP control program
%endif
* echomixer - Mixer for Echo Audio (indigo) devices
* envy24control - Control tool for Envy24 (ice1712) based soundcards
* hdspmixer - Mixer for the RME Hammerfall DSP cards
* hwmixvolume - Control the volume of individual streams on sound cards that
  use hardware mixing
* rmedigicontrol - Control panel for RME Hammerfall cards
* sbiload - An OPL2/3 FM instrument loader for ALSA sequencer
* sscape_ctl - ALSA SoundScape control utility
* us428control - Control tool for Tascam 428
* hda-verb - Direct HDA codec access
* hdajackretask - Reassign the I/O jacks on the HDA hardware
* hdajacksensetest - The sense test for the I/O jacks on the HDA hardware

%package firmware
Summary:        ALSA tools for uploading firmware to some soundcards
Requires:       udev
Requires:       alsa-firmware
Requires:       fxload
%description firmware
This package contains tools for flashing firmware into certain sound cards.
The following tools are available:

* hdsploader   - for RME Hammerfall DSP cards
* mixartloader - for Digigram miXart soundcards
* vxloader     - for Digigram VX soundcards
* usx2yloader  - second phase firmware loader for Tascam USX2Y USB soundcards

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
%patch -P 1 -p1 -b .hwmixvolume-python

%build

mv seq/sbiload . ; rm -rf seq
for i in %{?builddirstools:%builddirstools} %{?builddirsfirmw:%builddirsfirmw}
do
  cd $i ; %configure
  make %{?_smp_mflags} || exit 1
  cd ..
done
%install
mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}
for i in %{?builddirstools:%builddirstools} %{?builddirsfirmw:%builddirsfirmw}
do
  case $i in
    usx2yloader)
      (cd $i ; %make_install hotplugdir=/usr/lib/udev) || exit 1
      ;;
    *)
      (cd $i ; %make_install) || exit 1
      ;;
   esac
   if [[ -s "${i}"/README ]]
   then
      if [[ ! -d "%{buildroot}%{_pkgdocdir}/${i}" ]]
      then
         mkdir -p "%{buildroot}%{_pkgdocdir}/${i}"
      fi
      cp "${i}"/README "%{buildroot}%{_pkgdocdir}/${i}"
   fi
   if [[ -s "${i}"/COPYING ]]
   then
      if [[ ! -d "%{buildroot}%{_pkgdocdir}/${i}" ]]
      then
         mkdir -p "%{buildroot}%{_pkgdocdir}/${i}"
      fi
      cp "${i}"/COPYING "%{buildroot}%{_pkgdocdir}/${i}"
   fi
   if [[ -s %{buildroot}%{_datadir}/applications/${i}.desktop ]] ; then
      desktop-file-validate %{buildroot}%{_datadir}/applications/${i}.desktop
      desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/${i}.desktop
   fi
done
rm -f %{buildroot}/usr/lib/udev/tascam_fw.usermap
mkdir -p %{buildroot}/usr/lib/udev/rules.d
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{!?_without_tools:1}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.15-4
- Prepare for Oreon 11 (RP1)
%endif
