%define haproxy_user    haproxy
%define haproxy_group   %{haproxy_user}
%define haproxy_homedir %{_localstatedir}/lib/haproxy
%define haproxy_confdir %{_sysconfdir}/haproxy
%define haproxy_datadir %{_datadir}/haproxy

%global _hardened_build 1

Name:           haproxy
Version:        3.0.17
Release:        1%{?dist}
Summary:        HAProxy reverse proxy for high availability environments

License:        GPL-2.0-or-later

URL:            http://www.haproxy.org/
Source0:        http://www.haproxy.org//download/3.0/src/haproxy-3.0.17.tar.gz
Source1:        %{name}.service
Source2:        %{name}.cfg
Source3:        %{name}.logrotate
Source4:        %{name}.sysconfig
Source5:        %{name}.sysusers
Source6:        https://salsa.debian.org/haproxy-team/haproxy/-/raw/c30a7411203b8c4234698e47325d2543359f9d66/debian/halog.1

# https://github.com/haproxy/haproxy/commit/1c0f781994a89b5cbd7b4b893c23e6d2b75b1764
Patch0:        https://github.com/haproxy/haproxy/commit/1c0f781994a89b5cbd7b4b893c23e6d2b75b1764.patch#/haproxy-3.0.17-lua-5.5.patch
# oreon url source checksums begin
%global source0_sha256 58492710f8c82d81988e94f1188afc84eafd05d77393732241b252a8d14bd8a3
%global source0_file haproxy-3.0.17.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  lua-devel
BuildRequires:  pcre2-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  make

Requires(pre):  shadow-utils
%{?systemd_requires}

%description
HAProxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
 - route HTTP requests depending on statically assigned cookies
 - spread load among several servers while assuring server persistence
   through the use of HTTP cookies
 - switch to backup servers in the event a main one fails
 - accept connections to special ports dedicated to service monitoring
 - stop accepting connections without breaking existing ones
 - add, modify, and delete HTTP headers in both directions
 - block requests matching particular patterns
 - report detailed status to authenticated users from a URI
   intercepted from the application

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/haproxy-3.0.17.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "58492710f8c82d81988e94f1188afc84eafd05d77393732241b252a8d14bd8a3" || { echo "oreon: Source0 SHA256 mismatch for haproxy-3.0.17.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1 -b .lua55

%build

make %{?_smp_mflags} CPU="generic" TARGET="linux-glibc" USE_OPENSSL=1 USE_PCRE2=1 USE_SLZ=1 USE_LUA=1 USE_CRYPT_H=1 USE_SYSTEMD=1 USE_LINUX_TPROXY=1 USE_GETADDRINFO=1 USE_PROMEX=1 DEFINE=-DMAX_SESS_STKCTR=12 ADDINC="%{build_cflags}" ADDLIB="%{build_ldflags}"

make admin/halog/halog ADDINC="%{build_cflags}" ADDLIB="%{build_ldflags}"

pushd admin/iprange
make OPTIMIZE="%{build_cflags}" LDFLAGS="%{build_ldflags}"
popd

%install
make install-bin DESTDIR=%{buildroot} PREFIX=%{_prefix} SBINDIR=%{_sbindir} TARGET="linux2628"
make install-man DESTDIR=%{buildroot} PREFIX=%{_prefix}

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{haproxy_confdir}/%{name}.cfg
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/halog.1
install -d -m 0755 %{buildroot}%{haproxy_homedir}
install -d -m 0755 %{buildroot}%{haproxy_datadir}
install -d -m 0755 %{buildroot}%{haproxy_confdir}/conf.d
install -d -m 0755 %{buildroot}%{_bindir}
install -p -m 0755 ./admin/halog/halog %{buildroot}%{_bindir}/halog
install -p -m 0755 ./admin/iprange/iprange %{buildroot}%{_bindir}/iprange
install -p -m 0755 ./admin/iprange/ip6range %{buildroot}%{_bindir}/ip6range

for httpfile in $(find ./examples/errorfiles/ -type f) 
do
    install -p -m 0644 $httpfile %{buildroot}%{haproxy_datadir}
done

rm -rf ./examples/errorfiles/

find ./examples/* -type f ! -name "*.cfg" -exec rm -f "{}" \;

for textfile in $(find ./ -type f -name '*.txt')
do
    mv $textfile $textfile.old
    iconv --from-code ISO8859-1 --to-code UTF-8 --output $textfile $textfile.old
    rm -f $textfile.old
done

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc doc/* examples/*
%doc CHANGELOG README VERSION
%license LICENSE
%dir %{haproxy_homedir}
%dir %{haproxy_confdir}
%dir %{haproxy_confdir}/conf.d
%dir %{haproxy_datadir}
%{haproxy_datadir}/*
%config(noreplace) %{haproxy_confdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}
%{_bindir}/halog
%{_bindir}/iprange
%{_bindir}/ip6range
%{_mandir}/man1/*
%{_sysusersdir}/%{name}.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.17-1
- Prepare for Oreon 11 (RP1)
