%global source0_hash 797d9200c7d38ba4a07592bbb5b307580891d9e9ca2e130090ab6ced0accd7c2

%global cpan_name Authen-Credential

Name:           perl-%{cpan_name}
Version:        1.2
Release:        14%{?dist}
Summary:        Abstraction of a credential
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LC/LCONS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(No::Worries::Die) >= 1.1
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(No::Worries::Die) >= 1.1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(No::Worries::Die\\)$

%description
This module offers an abstraction of a credential, i.e. something that
can be used to authenticate. It allows the creation and manipulation of
credentials. In particular, it defines a standard string representation
(so that credentials can be given to external programs as command line
options), a standard structured representation (so that credentials can
be stored in structured configuration files or using JSON) and
"preparators" that can transform credentials into ready-to-use data for
well known targets.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
unset X509_CERT_DIR X509_CERT_FILE X509_USER_CERT X509_USER_KEY
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{3pod,4podcov}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset X509_CERT_DIR X509_CERT_FILE X509_USER_CERT X509_USER_KEY
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%files
%doc Changes README
%dir %{perl_vendorlib}/Authen
%{perl_vendorlib}/Authen/Credential
%{perl_vendorlib}/Authen/Credential.pm
%{_mandir}/man3/Authen::Credential.*
%{_mandir}/man3/Authen::Credential::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
