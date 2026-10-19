%global source0_hash 092399d5e8749a1d5e188e393157521cec4b75693b60ebb79bbce728cff2232c
%define   baseversion     1.2.16
%global   _hardened_build 1
%global   utils_patch     0
Summary:        Advanced Linux Sound Architecture (ALSA) utilities
Name:    alsa-utils
Version: %{baseversion}%{?fixversion}
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://www.alsa-project.org/
Source0:        https://www.alsa-project.org/files/pub/utils/alsa-utils-%{version}.tar.bz2
Source4: alsaunmute
Source5: alsaunmute.1
Source11: alsactl.conf
Source20: alsa-restore.service
Source22: alsa-state.service
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: alsa-lib%{?_isa} >= %{baseversion}
Requires: alsa-ucm >= %{baseversion}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python3-docutils
BuildRequires:  systemd
BuildRequires:  xmlto
# /oreon:deps
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
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE20} %{buildroot}/%{_unitdir}/alsa-restore.service
install -p -m 644 %{SOURCE22} %{buildroot}/%{_unitdir}/alsa-state.service
mkdir -p -m755 %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE4} %{buildroot}/%{_bindir}
mkdir -p -m755 %{buildroot}/%{_mandir}/man1
install -p -m 644 %{SOURCE5} %{buildroot}/%{_mandir}/man1/alsaunmute.1
mkdir -p -m 755 %{buildroot}%{alsacfgdir}
mv %{buildroot}%{_datadir}/alsa/init %{buildroot}%{alsacfgdir}
ln -s ../../lib/alsa/init %{buildroot}%{_datadir}/alsa/init
mkdir -p -m 755 %{buildroot}/etc/alsa
install -p -m 644 %{SOURCE11} %{buildroot}/etc/alsa
mkdir -p -m 755 %{buildroot}%{_sharedstatedir}/alsa
find %{buildroot} -name "*.la" -exec rm {} \;
%oreon_autofiles alsa-ucm-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alsa-topology-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alsa-utils-alsabat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n alsa-ucm-utils -f %{oreon_filedir}/alsa-ucm-utils.list
%files -n alsa-topology-utils -f %{oreon_filedir}/alsa-topology-utils.list
%files -n alsa-utils-alsabat -f %{oreon_filedir}/alsa-utils-alsabat.list

%changelog

%autochangelog
