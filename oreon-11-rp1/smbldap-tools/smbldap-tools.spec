%global source0_hash bf263c7b6cee2f51cb2b53a69f55747a7a3698f25d8571aedc026572fead9df5
Summary:        User and group administration tools for Samba/OpenLDAP
Name:		smbldap-tools
Version:	0.9.11
Release:        30%{?dist}
License:	GPL-2.0-or-later
URL:		http://gna.org/projects/smbldap-tools/
Source0:        http://download.gna.org/smbldap-tools/sources/%{version}/smbldap-tools-%{version}.tar.gz
Patch0:		smbldap-tools-0.9.11-bz1456783.patch
Patch10:	smbldap-tools-0.9.9-config.patch
BuildArch:	noarch
%if 0%{?fedora} < 38 && 0%{?rhel} < 10 && 0%{?oreon} < 11
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%endif
Requires:	perl(IO::Socket::SSL)
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(Crypt::SmbHash)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Extension::SetPassword)
BuildRequires:  perl(Net::LDAP::LDIF)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
In conjunction with OpenLDAP and Samba-LDAP servers, this collection is useful
to add, modify and delete users and groups, and to change Unix and Samba
passwords. In those contexts they replace the system tools to manage users,
groups and passwords.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Use usersdn instead of full LDAP search base when looking for user accounts (#1456783)
%patch -P 0

# Fedora integration
%patch -P 10

# Not allowed to have executable docs any more
chmod -R -c -x+X doc/

# Should still fix script interpreters though
sed -i -e 's|@PERL_COMMAND@|/usr/bin/perl|' smbldap-config.pl

%build

%configure
make
%install
make install DESTDIR=%{buildroot}
install -d -m 755 %{buildroot}%{_mandir}/man8/
install -p -m 644 smbldap-*.8 %{buildroot}%{_mandir}/man8/
install -d -m 755 %{buildroot}%{_sysconfdir}/smbldap-tools/
install -p -m 644 smbldap.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap.conf
install -p -m 600 smbldap_bind.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap_bind.conf
sed -e 's|@PERL_COMMAND@|/usr/bin/perl|' smbldap-upgrade-0.9.6.pl > \
	%{buildroot}%{_sbindir}/smbldap-upgrade-0.9.6.pl
chmod 755 %{buildroot}%{_sbindir}/smbldap-upgrade-0.9.6.pl
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
