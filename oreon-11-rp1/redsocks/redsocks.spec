%global source0_hash bbeb531d7f1986d7102f1bd6733dacce41d3f3ba7d604f1aab61c63e0ba2ee62
%global forgeurl https://github.com/darkk/redsocks
%global tag      release-%{version}
%global distprefix %{nil} 
%forgemeta
Name:           redsocks
Version:        0.5
Release:        1%{?dist}
Summary:        SOCKS and HTTP proxy redirector
License:        Apache-2.0 AND LGPL-2.1-or-later AND Zlib
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:        redsocks.conf
Source2:        redsocks.service
Source3:        redsocks.sysconfig
Source4:        redsocks.sysuser
Source5:        Apache-2.0.txt
Source6:        LGPL-2.1-or-later.txt
Source7:        Zlib.txt
Patch0:         setgroups-before-setuid.patch
Patch1:         libevent-2.1-compat.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%make_build
%install
install -Dpm 755 redsocks %{buildroot}%{_bindir}/redsocks
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/redsocks.conf
install -dm  755 %{buildroot}%{_unitdir}
install -pm  644 %{SOURCE2} %{buildroot}%{_unitdir}
install -Ddm 755 %{buildroot}%{_sysconfdir}/sysconfig
install -pm  644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/redsocks
install -Dpm 644 %{SOURCE4} %{buildroot}%{_sysusersdir}/redsocks.conf
install -pm  644 %{SOURCE5} Apache-2.0.txt
install -pm  644 %{SOURCE6} LGPL-2.1-or-later.txt
install -pm  644 %{SOURCE7} Zlib.txt
install -Ddm 755 %{buildroot}%{_mandir}/man8
install -pm  644 debian/redsocks.8 %{buildroot}%{_mandir}/man8
%oreon_autofiles main

%pre 

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post redsocks.service
%preun

%systemd_preun redsocks.service
%postun

%systemd_postun_with_restart redsocks.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
