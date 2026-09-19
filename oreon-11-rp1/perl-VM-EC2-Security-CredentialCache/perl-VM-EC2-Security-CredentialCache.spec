%global source0_hash fc7e9c152ff2b721ccb221ac40089934775cf58366aedb5cc1693609f840937b

Name:           perl-VM-EC2-Security-CredentialCache
Version:        0.25
Release:        31%{?dist}
Summary:        Cache credentials respecting expiration time for IAM roles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/VM-EC2-Security-CredentialCache
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCONOVER/VM-EC2-Security-CredentialCache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(VM::EC2::Instance::Metadata)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%description
This Perl package provides a cache for an EC2's IAM credentials. Rather than
retrieving the credentials for every possible call that uses them, cache them
until they expire and retrieve them again if they have expired.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n VM-EC2-Security-CredentialCache-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc CHANGES README
%dir %{perl_vendorlib}/VM
%dir %{perl_vendorlib}/VM/EC2
%dir %{perl_vendorlib}/VM/EC2/Security
%{perl_vendorlib}/VM/EC2/Security/CredentialCache.pm
%{_mandir}/man3/VM::EC2::Security::CredentialCache.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
