%global source0_hash e2f389fe3e7a9e4b61488692919ad723b98f3b479b5288f610daa8c27995b351

# Perform optional tests
# Support XML serialization of LDAP schemata (DSML languge)
%if 0%{?rhel}
%bcond_with perl_LDAP_enables_optional_test
%bcond_with perl_LDAP_enables_xml
%else
%bcond_without perl_LDAP_enables_optional_test
%bcond_without perl_LDAP_enables_xml
%endif

Name:           perl-LDAP
Version:        0.68
Release:        17%{?dist}
Epoch:          1
Summary:        LDAP Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/perl-ldap
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARSCHAP/perl-ldap-%{version}.tar.gz
# Optional tests need to know a location of an LDAP server executable
Patch0:         perl-ldap-0.65-Configure-usr-sbin-slapd-for-tests.patch
# Remove an unreliable cancelling test
Patch1:         perl-ldap-0.66-test-Remove-a-test-for-cancelling-asynchronous-calls.patch
# Fix resolving localhost on loopback-only machines,
# <https://github.com/perl-ldap/perl-ldap/pull/60>, CPAN RT#104793
Patch2:         perl-ldap-0.68-Do-not-default-IO-Socket-IP-to-AI_ADDRCONFIG-flag.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
# Not needed for tests perl(Authen::SASL) >= 2.00
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::ASN1) >= 0.2
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# Not needed for tests perl(HTTP::Negotiate)
# Not needed for tests perl(HTTP::Response)
# Not needed for tests perl(HTTP::Status)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
%if %{with perl_LDAP_enables_optional_test}
BuildRequires:  perl(IO::Socket::SSL) >= 1.26
%endif
# Not needed for tests perl(JSON)
# Not needed for tests perl(LWP::MediaTypes)
# Not needed for tests perl(LWP::Protocol)
# Not needed for tests perl(MIME::Base64)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Prefer core Text::Soundex
BuildRequires:  perl(Text::Soundex)
BuildRequires:  perl(Time::Local)
%if %{with perl_LDAP_enables_xml}
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Writer)
%endif
# Optional:
# Not needed for tests perl(IO::Socket::INET6)
# Not needed for tests perl(IO::Socket::IP)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
%if %{with perl_LDAP_enables_optional_test}
# Optional tests:
BuildRequires:  openldap-servers
BuildRequires:  perl(LWP::UserAgent)
%endif
Requires:       perl(Authen::SASL) >= 2.00
Requires:       perl(Convert::ASN1) >= 0.2
Requires:       perl(IO::Socket::SSL) >= 1.26
Requires:       perl(JSON)
%if %{with perl_LDAP_enables_xml}
Suggests:       perl(Net::LDAP::DSML)
%endif
Requires:       perl(MIME::Base64)
# Prefer core Text::Soundex
Requires:       perl(Text::Soundex)
Requires:       perl(Time::Local)

# Remove under-specified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Net::LDAP::Filter\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(t::common.pl\\)

%description
Net::LDAP is a collection of modules that implements an LDAP services API
for Perl programs. The module may be used to search directories or perform
maintenance functions such as adding, deleting or modifying entries.

%if %{with perl_LDAP_enables_xml}
%package -n perl-Net-LDAP-DSML
Summary:        DSML Writer for Net::LDAP
Requires:       perl-LDAP = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(MIME::Base64)
Requires:       perl(Net::LDAP::Schema)
Requires:       perl(XML::SAX::Writer)

%description -n perl-Net-LDAP-DSML
Directory Service Markup Language (DSML) is the XML standard for representing
directory service information in XML. At the moment this Perl module only
writes DSML entry and schema entities. Reading DSML entities is a future
project.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       coreutils
Requires:       perl-LDAP = %{?epoch:%{epoch}:}%{version}-%{release}
# perl-Test-Harness for "prove" command
Requires:       perl-Test-Harness
Requires:       perl(Convert::ASN1) >= 0.2
Requires:       perl(File::Spec)
Requires:       perl(Net::LDAPI)
# Prefer core Text::Soundex
Requires:       perl(Text::Soundex)
%if %{with perl_LDAP_enables_xml}
Requires:       perl(XML::SAX::Base)
Requires:       perl(XML::SAX::Writer)
%endif
%if %{with perl_LDAP_enables_optional_test}
# Optional tests:
Requires:       openldap-servers
Requires:       perl(IO::Socket::SSL) >= 1.26
Requires:       perl(Net::LDAPS)
Requires:       perl(LWP::UserAgent)
%endif

%description tests
Tests from %{name}-%{version}. Execute them with "%{_libexecdir}/%{name}/test".


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n perl-ldap-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
chmod -c 644 bin/* contrib/* lib/Net/LDAP/DSML.pm
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' contrib/*
# Remove bundled libraries
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove tests specific for XML support if the support is disabled
%if !%{with perl_LDAP_enables_xml}
rm t/05dsml.t
perl -i -ne 'print $_ unless m{^t/05dsml\.t}' MANIFEST
%endif
find -type f \! -name 'regenerate_cert.sh' -exec chmod -x {} +
# Help generators to recognize Perl scripts
for F in t/*; do
    perl -i -MConfig -pe 's/\A#!perl\b/$Config{startperl}/' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 < /dev/null
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
# FIXME: Generators should scan these non-executable files
cp -a data t test.cfg %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test <<'EOF'
#!/bin/bash
set -e
# t/common.pl reads from ./data and writes into ./temp. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test
 
%files
%doc Changes CREDITS
%doc contrib/ bin/
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/LWP/
%{perl_vendorlib}/Net/
%exclude %{perl_vendorlib}/Net/LDAP/DSML.pm
%{_mandir}/man3/*.3pm*
%exclude %{_mandir}/man3/Net::LDAP::DSML.3pm*

%if %{with perl_LDAP_enables_xml}
%files -n perl-Net-LDAP-DSML
%{perl_vendorlib}/Net/LDAP/DSML.pm
%{_mandir}/man3/Net::LDAP::DSML.3pm*
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.68-17
- Prepare for Oreon 11 (RP1)
