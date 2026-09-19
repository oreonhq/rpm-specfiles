%global source0_hash none

Name:           direwolf
Version:        1.8.1
Release:        4%{?dist}
Summary:        Sound Card-based AX.25 TNC

License:        GPL-2.0-or-later
URL:            https://github.com/wb2osz/direwolf/
# This is the actual source
Source0:        https://github.com/wb2osz/direwolf/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        direwolf.service
Source2:        direwolf.sysconfig
Source3:        direwolf.logrotate
# Only include externals when actually needed
Patch:          %{url}/pull/565.patch

ExcludeArch:    i686

BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  avahi-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  glibc-devel
BuildRequires:  gpsd-devel
BuildRequires:  hamlib-devel
BuildRequires:  hidapi-devel
BuildRequires:  libgpiod-devel
BuildRequires:  systemd systemd-devel

Requires:       ax25-tools ax25-apps

%description
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, Winlink Express, BPQ32, Outpost PM, and many
others.

%package -n %{name}-doc
Summary:        Documentation for Dire Wolf
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-doc
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, RMS Express, BPQ32, Outpost PM, and many
others.

%prep
%autosetup -p 1

# Create a sysusers.d config file
cat >direwolf.sysusers.conf <<EOF
u direwolf -:audio 'Direwolf Sound Card-based AX.25 TNC' %{_datadir}/%{name} -
m direwolf audio
m direwolf dialout
EOF

# Remove bundled libraries we're not using
rm -r external/{hidapi,misc,regex}
# Not needed and breaks finding hidapi on Fedora
rm cmake/modules/Findhidapi.cmake

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DUNITTEST=1 -DENABLE_GENERIC=1 -DUSE_SYSTEM_HIDAPI=ON
%cmake_build

%install
%cmake_install

# Install service file
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service

# Install service config file
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

# Install logrotate config file
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

# copy config file
cp ${RPM_BUILD_ROOT}%{_pkgdocdir}/conf/%{name}.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}.conf

# Make log directory
mkdir -m 0755 -p ${RPM_BUILD_ROOT}/var/log/%{name}

# Move udev rules to system dir
#mkdir -p ${RPM_BUILD_ROOT}%{_udevrulesdir}
#mv ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/99-direwolf-cmedia.rules ${RPM_BUILD_ROOT}%{_udevrulesdir}/99-direwolf-cmedia.rules

# Copy doc pngs
cp direwolf-block-diagram.png ${RPM_BUILD_ROOT}%{_pkgdocdir}/direwolf-block-diagram.png
cp tnc-test-cd-results.png    ${RPM_BUILD_ROOT}%{_pkgdocdir}/tnc-test-cd-results.png

# remove extraneous files
# This is not a desktop application, per the guidelines.  Running it in a terminal
# does not make it a desktop application.
rm ${RPM_BUILD_ROOT}/usr/share/applications/direwolf.desktop
rm ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/direwolf_icon.png
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/CHANGES.md
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/LICENSE
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/README.md

# remove Windows external library directories
rm -r ${RPM_BUILD_ROOT}%{_pkgdocdir}/external

# Move Telemetry Toolkit sample scripts into docs
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
mv ${RPM_BUILD_ROOT}%{_bindir}/telem* ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
chmod 0644 ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/*

install -m0644 -D direwolf.sysusers.conf %{buildroot}%{_sysusersdir}/direwolf.conf

%check
%ctest

%files
%license LICENSE
%{_udevrulesdir}/99-direwolf-cmedia.rules
%{_bindir}/* 
%{_mandir}/man1/*
%{_datadir}/%{name}/*
%dir %{_pkgdocdir}
%{_pkgdocdir}/conf/*
%{_pkgdocdir}/scripts/*
%{_pkgdocdir}/telem/*
%{_unitdir}/%{name}.service
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755, %{name}, %{name}) /var/log/%{name}
%{_sysusersdir}/direwolf.conf

%files -n %{name}-doc
%{_pkgdocdir}/*.pdf
%{_pkgdocdir}/*.png

# At install, create a user in group audio (so can open sound card device files)
# and in group dialout (so can open serial device files)

%changelog
%autochangelog
