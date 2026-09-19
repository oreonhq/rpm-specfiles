%global source0_hash 7241d2972b1f6f76a28bdaa0e7942b1257e08b404a15d121c9dee568178f8bf5

Name: rancid
Version: 3.13
Release: 17%{?dist}
Summary: Really Awesome New Cisco confIg Differ

License: BSD-3-Clause
URL: http://www.shrubbery.net/rancid/
Source0: https://shrubbery.net/pub/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.cron
Patch0: %{name}-Makefile.patch
Patch1: %{name}-configure-no-ping-test.patch
Patch2: %{name}-3.13-dnos10-psu-filter.patch

BuildRequires: automake, autoconf
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: expect >= 5.40
BuildRequires: findutils
# To configure ping command line arguments:
BuildRequires: iputils
# To configure path to /usr/sbin/sendmail:
BuildRequires: ssmtp
# To configure telnet command line arguments:
BuildRequires: telnet

Requires: expect >= 5.40
# For control_rancid's use of find command:
Requires: findutils
# For lg.cgi's use of ping command:
Requires: iputils
Requires: perl-interpreter
Requires: /usr/sbin/sendmail
Requires: cronie
Requires: openssh-clients
Requires: git
Suggests: telnet

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

#symlink some bins from %%{_libexecdir}/%%{name} to %%{_bindir}
for base in \
 %{name} %{name}-cvs %{name}-fe %{name}-run
 do
 ln -sf ../libexec/%{name}/${base} \
  %{buildroot}/%{_bindir}/${base}
done

install -D -p -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/cron.d/%{name}

#Patch cron file to point to correct installation directory
sed -i 's|RANCIDBINDIR|%{_libexecdir}/%{name}|g' %{buildroot}/%{_sysconfdir}/cron.d/%{name}

#Patch to point to correct log directory
grep -rlF '$BASEDIR/logs' %{buildroot} | xargs sed -i 's|\$BASEDIR/logs|%{_localstatedir}/log/%{name}|'

#Remove docs that will get installed to docdir in files section below
rm -f %{buildroot}%{_datadir}/%{name}/{CHANGES,FAQ,README,README.lg,UPGRADING,Todo,COPYING}

install -m0644 -D rancid.sysusers.conf %{buildroot}%{_sysusersdir}/rancid.conf

%files
%doc CHANGES FAQ README README.lg UPGRADING Todo
%license COPYING

#%%{_sysconfdir}-files
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/%{name}
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/%{name}

#%%{_libexecdir}/%%{name}-files
%{_libexecdir}/%{name}

#%%{_bindir}-files
%{_bindir}/*

#%%{_mandir}-files
%{_mandir}/*/*

#%%{_datadir}/%%{name}-files
%{_datadir}/%{name}

#%%{_localstatedir}-directories
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}/old
%attr(750,%{name},%{name}) %dir %{_localstatedir}/%{name}/

%{perl_vendorlib}/*
%{_sysusersdir}/rancid.conf

%changelog
%autochangelog
