%global source0_hash 89d5f7992ae1e74d8cf26ec6479dde74d1f480bde950043756e875a689d065d7
Name:           direwolf
Version:        1.8.1
Release:        1%{?dist}
Summary:        Sound Card-based AX.25 TNC
License:        GPL-2.0-or-later
URL:            https://github.com/wb2osz/direwolf/
Source0:        https://github.com/wb2osz/direwolf/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        direwolf.service
Source2:        direwolf.sysconfig
Source3:        direwolf.logrotate
Patch:          %{url}/pull/565.patch
ExcludeArch:    i686
Requires:       ax25-tools ax25-apps
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gpsd-devel
BuildRequires:  hamlib-devel
BuildRequires:  hidapi-devel
BuildRequires:  libgpiod-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
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
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
cp ${RPM_BUILD_ROOT}%{_pkgdocdir}/conf/%{name}.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}.conf
mkdir -m 0755 -p ${RPM_BUILD_ROOT}/var/log/%{name}
cp direwolf-block-diagram.png ${RPM_BUILD_ROOT}%{_pkgdocdir}/direwolf-block-diagram.png
cp tnc-test-cd-results.png    ${RPM_BUILD_ROOT}%{_pkgdocdir}/tnc-test-cd-results.png
rm ${RPM_BUILD_ROOT}/usr/share/applications/direwolf.desktop
rm ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/direwolf_icon.png
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/CHANGES.md
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/LICENSE
rm ${RPM_BUILD_ROOT}%{_pkgdocdir}/README.md
rm -r ${RPM_BUILD_ROOT}%{_pkgdocdir}/external
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
mv ${RPM_BUILD_ROOT}%{_bindir}/telem* ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/
chmod 0644 ${RPM_BUILD_ROOT}%{_pkgdocdir}/telem/*
install -m0644 -D direwolf.sysusers.conf %{buildroot}%{_sysusersdir}/direwolf.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n direwolf-doc -f %{oreon_filedir}/direwolf-doc.list

%changelog

%autochangelog
