%global source0_hash 9c0d4a101b5d40176296eb8b2b531f0e90fdc4aa8d3308241c5e05666a1fd4d7

%global pname   osdteletext
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

%global commit0 cae4629f84886015b0619af6fdb1084853b80f93
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20211217

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

Name:           vdr-%{pname}
Version:        2.3.2
Release:        0.7.%{gitdate}git%{shortcommit0}%{?dist}
# Release:        21%%{?dist}
Summary:        OSD teletext plugin for VDR

License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-osdteletext
Source0:        https://github.com/vdr-projects/vdr-plugin-osdteletext/archive/%{commit0}/%{name}-%{version}-%{shortcommit0}.tar.gz
# Source0:        https://github.com/vdr-projects/vdr-plugin-osdteletext/archive/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source1:        %{name}.conf
# https://www.vdr-portal.de/forum/thread/136886-gel%%C3%%B6st-vdr-startet-nicht-mehr-mit-aktivem-vdr-osdteletext-plugin/?postID=1382554#post1382554
Patch0:         Fix_DrawMessage.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
The OSD teletext plugin displays teletext directly on VDR's on-screen
display, with sound and video from the current channel playing in the
background.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n vdr-plugin-%%{pname}-%%{version}
%autosetup -p1 -n vdr-plugin-%{pname}-%{commit0}
sed -i -e 's|/var/cache/vdr/vtx|%{vdr_rundir}/%{pname}|g' \
    osdteletext.c README README.DE rootdir.c

%build
%make_build

%install
%make_install

install -dm 755 $RPM_BUILD_ROOT%{vdr_rundir}/%{pname}
install -dm 755 $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/fonts/vdr%{pname}
echo "d %{vdr_rundir}/%{pname} 0755 %{vdr_user} root -" > \
  $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/%{name}.conf

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

install -Dpm 644 teletext2.ttf \
  $RPM_BUILD_ROOT%{_datadir}/fonts/vdr%{pname}/teletext2.ttf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{_datadir}/fonts/vdrosdteletext/teletext2.ttf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%attr(-,%{vdr_user},root) %{vdr_rundir}/%{pname}/

%changelog
%autochangelog
