%global source0_hash 96c50fefe7ecf015cf64ba6cec9e421ffd3b18fef809f59961ef9229df528f3e
Name:           connect-proxy
Version:        1.105
Release:        1%{?dist}
Summary:        SSH Proxy command helper
License:        GPL-2.0-or-later
URL:            http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Source0:        ssh-connect-%{version}.tar.gz
Source1:        connect-proxy.1
Patch0:         connect-proxy-1.105-socklen.patch
Requires:       openssh
# oreon:deps
BuildRequires:  add-determinism
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
connect-proxy is the simple relaying command to make network connection via
SOCKS and https proxy. It is mainly intended to be used as proxy command
of OpenSSH. You can make SSH session beyond the firewall with this command.

Features of connect-proxy are:

    * Supports SOCKS (version 4/4a/5) and https CONNECT method.
    * Supports NO-AUTH and USERPASS authentication of SOCKS
    * Partially supports telnet proxy (experimental).
    * You can input password from tty, ssh-askpass or environment variable.
    * Simple and general program independent from OpenSSH.
    * You can also relay local socket stream instead of standard I/O.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ssh-connect-%{version}
%patch -P 0 -p1

%build

make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp connect $RPM_BUILD_ROOT/%{_bindir}/connect-proxy
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
