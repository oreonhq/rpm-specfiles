%global source0_hash db2b05ec3971b509dc198581fb0031c0848d07b2a2ecaa7bb83ee147c5bcdaf9

%global pname     streamdev
# If this variable is set the spec file assumes it's building a git snapshot
# Also see info below on generating snapshots
%global gitver    b84b7d858cf4f6f3473ba72d456326c048946cb0
%global gitshort  %(echo %gitver | awk '{print substr($0,1,8)}')
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

%if 0%{?gitver:0}
  # Use vdr-streamdev-snapshot.sh contained in the source of the package to
  # generate new snapshots
  # You can also create snapshots for specific commit hashes
  # Example: sh vdr-streamdev-snapshot.sh b84b7d858cf4f6f3473ba72d456326c048946cb0
  %global srcfile   %{name}-%{gitshort}.tar.xz
  %global setuppath %{name}-%{gitshort}
%else
  # URL for original source file when not using git snapshots
  %global srcfile   https://github.com/vdr-projects/vdr-plugin-streamdev/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
  %global setuppath %{pname}-%{version}
%endif

Name:           vdr-%{pname}
Version:        0.6.5
%if 0%{?gitver:0}
Release:        0.52%{?gitver:.git%{gitshort}}%{?dist}
%else
Release:        2%{?dist}
%endif
Summary:        Streaming plug-in for VDR
License:        GPL-1.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-streamdev

Source0:        %{srcfile}
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}-server.conf
Source2:        %{name}-client.conf
# Script to generate git snapshots
# listed here so that it's pulled into the SRPM
Source3:        %{name}-snapshot.sh

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}

%description
The streamdev plug-in adds streaming capabilities to your VDR.

%package server
Summary:        Streaming server plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description server
Lets your VDR act as a streaming server for other clients.
This will let you watch TV or Recordings across the network.

%package client
Summary:        Streaming client plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description client
Lets your VDR in conjunction with a streamdev-server act as a streaming client.
VDR will then be able to work even without a DVB device.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?gitver:0}
%autosetup -p1 -n %{setuppath}
%else
%autosetup -p1 -n vdr-plugin-streamdev-%{version}
%endif

sed -i 's@$(VDRDIR)/device.h@%{_includedir}/vdr/device.h@' Makefile

for f in CONTRIBUTORS HISTORY; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
install -dm 755 $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server
install -Dpm 644 streamdev-server/streamdevhosts.conf $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf
install -Dpm 755 streamdev-server/externremux.sh $RPM_BUILD_ROOT%{_libdir}/vdr/bin/externremux.sh 
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf
%find_lang %{name}-server
%find_lang %{name}-client

%files server -f %{name}-server.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-server.so.%{vdr_apiversion}
%{_libdir}/vdr/bin/externremux.sh
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
%dir %{vdr_configdir}/plugins/streamdev-server
%config(noreplace) %{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf

%files client -f %{name}-client.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-client.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf

%changelog
%autochangelog
