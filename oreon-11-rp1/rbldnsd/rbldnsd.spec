%global source0_hash 08a9a5c76f0a45798b737e610871aa0567e95316bb91090b7599741327980be5
%global systemd_rpm_macros systemd-rpm-macros
%global use_sysusers 1
%global _hardened_build 1
Summary:        Small, fast daemon to serve DNSBLs
Name:		rbldnsd
Version:	0.998b
Release:        20%{?dist}
License:	GPL-2.0-or-later
URL:		https://rbldnsd.io/
Source0:        https://rbldnsd.io/dwl/rbldnsd-%{version}.tgz
Source2:	rbldnsd.conf
Source3:	rbldnsctl
Source4:	README.systemd
Patch0:		rbldnsd-configure-c99.patch
Patch1:		rbldnsd-0.998b-version.patch
Patch2:		https://github.com/spamhaus/rbldnsd/commit/85932ec5.patch
%if !%{use_sysusers}
Requires(pre):	shadow-utils
%endif
Requires:	gawk
%{?systemd_requires}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Rbldnsd is a small, authoritative-only DNS nameserver designed to serve
DNS-based blocklists (DNSBLs). It may handle IP-based and name-based
blocklists.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Port non-autoconf configure script to C99
%patch -P 0 -p1

# Fix version number reported by rbldnsd
%patch -P 1

# Fix base template replacement issue
# https://github.com/spamhaus/rbldnsd/issues/18
# https://github.com/spamhaus/rbldnsd/issues/19
# https://github.com/spamhaus/rbldnsd/pull/22
%patch -P 2 -p1

sed -i	-e 's@/var/lib/rbldns\([/ ]\)@%{_localstatedir}/lib/rbldnsd\1@g' \
	-e 's@\(-r/[a-z/]*\) -b@\1 -q -b@g' contrib/debian/rbldnsd.default
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} ./

# Create a sysusers.d config file
cat >rbldnsd.sysusers.conf <<EOF
u rbldns - 'rbldns daemon' %{_localstatedir}/lib/rbldnsd -
EOF

%build

CFLAGS="%{optflags}" \
LDFLAGS="%{?__global_ldflags}" \
./configure
make
%install
mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man8,%{_initrddir},%{_sysconfdir}/sysconfig}
mkdir -p %{buildroot}{/etc/systemd,%{_localstatedir}/lib/rbldnsd}
install -p -m 755 rbldnsd				%{buildroot}%{_sbindir}/
install -p -m 644 rbldnsd.8				%{buildroot}%{_mandir}/man8/
install -p -m 644 contrib/debian/rbldnsd.default	%{buildroot}%{_sysconfdir}/sysconfig/rbldnsd
install -p -m 644 rbldnsd.conf				%{buildroot}/etc/systemd/
install -p -m 755 rbldnsctl				%{buildroot}%{_sbindir}/
install -m0644 -D rbldnsd.sysusers.conf %{buildroot}%{_sysusersdir}/rbldnsd.conf
%oreon_autofiles main
%if !%{use_sysusers}
%pre

getent group rbldns >/dev/null || groupadd -r rbldns
getent passwd rbldns >/dev/null || \
	useradd -r -g rbldns -d %{_localstatedir}/lib/rbldnsd \
		-s /sbin/nologin -c "rbldns daemon" rbldns
exit 0
%endif
%post

systemctl daemon-reload &>/dev/null || :
%preun

if [ $1 -eq 0 ]; then
	%{_sbindir}/rbldnsctl stop &>/dev/null || :
	%{_sbindir}/rbldnsctl disable &>/dev/null || :
fi
%postun

systemctl daemon-reload &>/dev/null || :
if [ $1 -ge 1 ]; then
	%{_sbindir}/rbldnsctl try-restart &>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
