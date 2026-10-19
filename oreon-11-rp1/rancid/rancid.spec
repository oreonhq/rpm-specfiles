%global source0_hash 7241d2972b1f6f76a28bdaa0e7942b1257e08b404a15d121c9dee568178f8bf5
Name: rancid
Version: 3.13
Release:        1%{?dist}
Summary:        Really Awesome New Cisco confIg Differ
License: BSD-3-Clause
URL: http://www.shrubbery.net/rancid/
Source0:        https://shrubbery.net/pub/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.cron
Patch0: %{name}-Makefile.patch
Patch1: %{name}-configure-no-ping-test.patch
Patch2: %{name}-3.13-dnos10-psu-filter.patch
Requires: expect >= 5.40
Requires: findutils
Requires: iputils
Requires: perl-interpreter
Requires: /usr/sbin/sendmail
Requires: cronie
Requires: openssh-clients
Requires: git
Suggests: telnet
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expect
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  iputils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  ssmtp
BuildRequires:  telnet
# /oreon:deps
%description
RANCID monitors a router's (or more generally a device's) configuration, 
including software and hardware (cards, serial numbers, etc) and uses CVS 
(Concurrent Version System), Subversion, or Git to maintain history of changes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >rancid.sysusers.conf <<EOF
u rancid - 'RANCID' %{_localstatedir}/%{name}/ /bin/bash
EOF

%build

%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --bindir=%{_libexecdir}/%{name} \
    --libdir=%{perl_vendorlib} \
    --localstatedir=%{_localstatedir}/%{name} \
    --enable-conf-install \
    --with-git
%make_build
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -d -m 0755 %{buildroot}/%{_localstatedir}/%{name}
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/old
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cron.d
install -d -m 0755 %{buildroot}/%{_bindir}/
for base in \
 %{name} %{name}-cvs %{name}-fe %{name}-run
 do
 ln -sf ../libexec/%{name}/${base} \
  %{buildroot}/%{_bindir}/${base}
done
install -D -p -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/cron.d/%{name}
sed -i 's|RANCIDBINDIR|%{_libexecdir}/%{name}|g' %{buildroot}/%{_sysconfdir}/cron.d/%{name}
grep -rlF '$BASEDIR/logs' %{buildroot} | xargs sed -i 's|\$BASEDIR/logs|%{_localstatedir}/log/%{name}|'
rm -f %{buildroot}%{_datadir}/%{name}/{CHANGES,FAQ,README,README.lg,UPGRADING,Todo,COPYING}
install -m0644 -D rancid.sysusers.conf %{buildroot}%{_sysusersdir}/rancid.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
