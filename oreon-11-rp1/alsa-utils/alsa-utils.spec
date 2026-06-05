%global source0_hash none

%define   baseversion     1.2.15
%define   fixversion      .2
%global   _hardened_build 1

%global   utils_patch     0

Summary: Advanced Linux Sound Architecture (ALSA) utilities
Name:    alsa-utils
Version: %{baseversion}%{?fixversion}
Release: 3%{?dist}
License: GPL-2.0-or-later
URL:     https://www.alsa-project.org/
# HTTPS so spectool/mock can fetch without FTP (often blocked in builders).
Source:        https://www.alsa-project.org/files/pub/utils/alsa-utils-%{version}.tar.bz2
Source4: alsaunmute
Source5: alsaunmute.1
Source11: alsactl.conf
Source20: alsa-restore.service
Source22: alsa-state.service
%if %{utils_patch}
Patch1:  alsa-git.patch
%endif

BuildRequires: gcc
BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel >= %{baseversion}
BuildRequires: libsamplerate-devel
BuildRequires: ncurses-devel
BuildRequires: gettext-devel
BuildRequires: xmlto
BuildRequires: python3-docutils
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# use latest alsa-lib - the executables in this package requires latest API
Requires: alsa-lib%{?_isa} >= %{baseversion}
Requires: alsa-ucm >= %{baseversion}

%description
This package contains command line utilities for the Advanced Linux Sound
Architecture (ALSA).

%package -n alsa-ucm-utils
Summary: Advanced Linux Sound Architecture (ALSA) - Use Case Manager

%description -n alsa-ucm-utils
This package contains Use Case Manager tools for Advanced Linux Sound
Architecture (ALSA) framework.

%package -n alsa-topology-utils
Summary: Advanced Linux Sound Architecture (ALSA) - Topology
Requires: alsa-topology >= %{baseversion}

%description -n alsa-topology-utils
This package contains topology tools for Advanced Linux Sound
Architecture (ALSA) framework.

%package alsabat
Summary: Advanced Linux Sound Architecture (ALSA) - Basic Audio Tester
BuildRequires: fftw-devel
BuildRequires: make

%description alsabat
This package contains tool for basic audio testing using Advanced Linux Sound
Architecture (ALSA) framework and Fast Fourier Transform library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
%if %{utils_patch}
%patch -P1 -p1 -b .alsa-git
%endif

%build
autoreconf -vif
%configure CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" --disable-alsaconf \
   --with-udev-rules-dir=%{_prefix}/lib/udev/rules.d \
   --with-systemdsystemunitdir=%{_unitdir} \
   --with-alsactl-udev-args="-E ALSA_CONFIG_PATH=/etc/alsa/alsactl.conf --initfile=/lib/alsa/init/00main" \
   --with-alsactl-udev-extra-test=""
make %{?_smp_mflags}
cp %{SOURCE4} .

%install
%global alsacfgdir %{_prefix}/lib/alsa

make install DESTDIR=%{buildroot}
%find_lang %{name}

# Install ALSA udev rules and services
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE20} %{buildroot}/%{_unitdir}/alsa-restore.service
install -p -m 644 %{SOURCE22} %{buildroot}/%{_unitdir}/alsa-state.service

# Install support utilities
mkdir -p -m755 %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE4} %{buildroot}/%{_bindir}
mkdir -p -m755 %{buildroot}/%{_mandir}/man1
install -p -m 644 %{SOURCE5} %{buildroot}/%{_mandir}/man1/alsaunmute.1

# Move /usr/share/alsa/init to /usr/lib/alsa/init
mkdir -p -m 755 %{buildroot}%{alsacfgdir}
mv %{buildroot}%{_datadir}/alsa/init %{buildroot}%{alsacfgdir}

# Link /usr/lib/alsa/init to /usr/share/alsa/init back
ln -s ../../lib/alsa/init %{buildroot}%{_datadir}/alsa/init

# Create a place for global configuration
mkdir -p -m 755 %{buildroot}/etc/alsa
install -p -m 644 %{SOURCE11} %{buildroot}/etc/alsa

# Create /var/lib/alsa tree
mkdir -p -m 755 %{buildroot}%{_sharedstatedir}/alsa

find %{buildroot} -name "*.la" -exec rm {} \;

%files -f %{name}.lang
%doc COPYING ChangeLog README.md TODO alsamixer/alsamixer.rc.example
%config /etc/alsa/*
%{_prefix}/lib/udev/rules.d/*
%{_unitdir}/*
#{_unitdir}/sound.target.wants/*
%{alsacfgdir}/init/*
%{_bindir}/aconnect
%{_sbindir}/alsactl
%{_bindir}/alsaloop
%{_bindir}/alsamixer
%{_bindir}/alsaunmute
%{_sbindir}/alsa-info.sh
%{_bindir}/amidi
%{_bindir}/amixer
%{_bindir}/aplay
%{_bindir}/aplaymidi
%{_bindir}/aplaymidi2
%{_bindir}/arecord
%{_bindir}/arecordmidi
%{_bindir}/arecordmidi2
%{_bindir}/aseqdump
%{_bindir}/aseqnet
%{_bindir}/aseqsend
%{_bindir}/axfer
%{_bindir}/iecset
%{_bindir}/nhlt-dmic-info
%{_bindir}/speaker-test
%{_datadir}/alsa/
%{_datadir}/sounds/*
%{_mandir}/man7/*
%{_mandir}/man1/alsactl.1.gz
%{_mandir}/man1/alsaloop.1.gz
%{_mandir}/man1/alsamixer.1.gz
%{_mandir}/man1/alsaunmute.1.gz
%{_mandir}/man1/amidi.1.gz
%{_mandir}/man1/amixer.1.gz
%{_mandir}/man1/aplay.1.gz
%{_mandir}/man1/aplaymidi.1.gz
%{_mandir}/man1/aplaymidi2.1.gz
%{_mandir}/man1/arecord.1.gz
%{_mandir}/man1/arecordmidi.1.gz
%{_mandir}/man1/arecordmidi2.1.gz
%{_mandir}/man1/aseqdump.1.gz
%{_mandir}/man1/aseqnet.1.gz
%{_mandir}/man1/aseqsend.1.gz
%{_mandir}/man1/axfer.1.gz
%{_mandir}/man1/axfer-list.1.gz
%{_mandir}/man1/axfer-transfer.1.gz
%{_mandir}/man1/iecset.1.gz
%{_mandir}/man1/speaker-test.1.gz
%{_mandir}/man1/aconnect.1.gz
%{_mandir}/man8/alsa-info.sh.8.gz
%{_mandir}/man1/nhlt-dmic-info.1.gz

%dir /etc/alsa/
%dir %{alsacfgdir}/
%dir %{alsacfgdir}/init/
%dir %{_sharedstatedir}/alsa/

%files -n alsa-ucm-utils
%{_bindir}/alsaucm
%{_mandir}/man1/alsaucm.1.gz

%files -n alsa-topology-utils
%{_bindir}/alsatplg
%{_mandir}/man1/alsatplg.1.gz
%{_libdir}/alsa-topology/libalsatplg_module_*

%files alsabat
%{_bindir}/alsabat
%{_sbindir}/alsabat-test.sh
%{_mandir}/man1/alsabat.1.gz

%pre
if [ ! -r %{_unitdir}/alsa-state.service ]; then
  [ -d /etc/alsa ] || mkdir -m 0755 /etc/alsa
  echo "# Remove this file to disable the alsactl daemon mode" > \
                                                    /etc/alsa/state-daemon.conf
fi

%post
if [ -s /etc/alsa/asound.state -a ! -s /etc/asound.state ] ; then
  mv /etc/alsa/asound.state /etc/asound.state
fi
if [ -s /etc/asound.state -a ! -s %{_sharedstatedir}/alsa/asound.state ] ; then
  mv /etc/asound.state %{_sharedstatedir}/alsa/asound.state
fi
%systemd_post alsa-state.service

%preun
%systemd_preun alsa-state.service

%postun
%systemd_postun_with_restart alsa-state.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{baseversion}%{?fixversion}-3
- Prepare for Oreon 11 (RP1)
