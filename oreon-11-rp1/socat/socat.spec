%global source0_hash 06602ffd591e98c75b3dc1d66f0f19136cc666b0b2d95caad987d6ab2cb28097
%global _hardened_build 1
Summary:        Bidirectional data relay between two data channels ('netcat++')
Name: socat
Version: 1.8.1.3
Release:        1%{?dist}
License: GPL-2.0-only
Url:  http://www.dest-unreach.org/socat/
Source0:        http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  iproute
BuildRequires:  iputils
BuildRequires:  kernel-headers
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  net-tools
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  procps-ng
BuildRequires:  readline-devel
# /oreon:deps
%description
Socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES
%autopatch -p1

%build

sed -i "s/FGREP=fgrep/FGREP='grep -F'/" configure
sed -i "s/fgrep/grep -F/" test.sh
sed -i "s/egrep/egrep -E/" test.sh
%configure  \
        --enable-help --enable-stdio \
        --enable-fdnum --enable-file --enable-creat \
        --enable-gopen --enable-pipe --enable-termios \
        --enable-unix --enable-ip4 --enable-ip6 \
        --enable-rawip --enable-tcp --enable-udp \
        --enable-listen --enable-proxy --enable-exec \
        --enable-system --enable-pty --enable-readline \
        --enable-openssl --enable-sycls --enable-filan \
        --enable-retry # --enable-fips
%make_build
%install
%make_install
install -d %{buildroot}/%{_docdir}/socat
install -m 0644 *.sh %{buildroot}/%{_docdir}/socat/
echo ".so man1/socat.1" | gzip > %{buildroot}/%{_mandir}/man1/filan.1.gz
cp -a %{buildroot}/%{_mandir}/man1/filan.1.gz %{buildroot}/%{_mandir}/man1/procan.1.gz
%oreon_autofiles main

%check

%ifarch x86_64
export TERM=ansi
export OD_C=/usr/bin/od
sed -i 's/NUMCOND=true/NUMCOND="test \\$N -ne 146 -a \\$N -ne 478 -a \\$N -ne 528"/' test.sh
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
