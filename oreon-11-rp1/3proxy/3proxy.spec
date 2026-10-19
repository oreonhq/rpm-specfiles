%global source0_hash 35b07de1046f3aaeac4a7085101b7e5c453efa3527cbdc42a84690366c7ecfa8
%global _hardened_build 1
Name:             3proxy
Version:          1.0.0
Release:        1%{?dist}
Summary:        Tiny but very powerful proxy
Summary(ru):      Маленький, но крайне мощный прокси-сервер
License:          BSD-3-Clause OR Apache-2.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Url:              http://3proxy.ru/?l=EN
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:          3proxy.cfg
Source3:          3proxy.service
Patch0:           3proxy-0.6.1-config-path.patch
Patch1:           3proxy-0.9.4-poll-build.patch
Patch2:           3proxy-0.9.4-manpage.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{name} -- light proxy server.
Universal proxy server with HTTP, HTTPS, SOCKS v4, SOCKS v4a, SOCKS v5, FTP,
POP3, UDP and TCP portmapping, access control, bandwith control, traffic
limitation and accounting based on username, client IP, target IP, day time,
day of week, etc.

%description -l ru
%{name} -- маленький прокси сервер.
Это универсальное решение поддерживающее HTTP, HTTPS, SOCKS v4, SOCKS v4a,
SOCKS v5, FTP, POP3, UDP и TCP проброс портов (portmapping), списки доступа
управление скоростью доступа, ограничением трафика и статистикоу, базирующейся
на имени пользователя, слиентском IP адресе, IP цели, времени дня, дня недели
и т.д.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# To use "fedora" CFLAGS (exported)
sed -i -e "s/^CFLAGS =/CFLAGS +=/" Makefile.Linux

%build

make -f Makefile.Linux
%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
mkdir -p %{buildroot}%{_mandir}/man{3,8}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
install -m755 -D bin/%{name} %{buildroot}%{_bindir}/%{name}
install -m755 -D bin/ftppr %{buildroot}%{_bindir}/ftppr
install -m755 -D bin/mycrypt %{buildroot}%{_bindir}/mycrypt
install -m755 -D bin/pop3p %{buildroot}%{_bindir}/pop3p
install -m755 -D bin/proxy %{buildroot}%{_bindir}/htproxy
install -m755 -D bin/smtpp %{buildroot}%{_bindir}/smtpp
install -m755 -D bin/socks %{buildroot}%{_bindir}/socks
install -m755 -D bin/tcppm %{buildroot}%{_bindir}/tcppm
install -m755 -D bin/tlspr %{buildroot}%{_bindir}/tlspr
install -m755 -D bin/udppm %{buildroot}%{_bindir}/udppm
install -pD -m644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}.cfg
install -pD -m755 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.service
for man in man/*.{3,8} ; do
  install "$man" "%{buildroot}%{_mandir}/man${man:(-1)}/"
done
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
