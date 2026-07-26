%global source0_hash 53bbd339e6a11efca07c619a615c7c188a68bb2be849a1cb7efc3dd4d9ae85ae

# Perform optional tests
%bcond_without perl_Bytes_Random_Secure_enables_optional_test

Name:           perl-Bytes-Random-Secure
Version:        0.29
Release:        32%{?dist}
Summary:        Perl extension to generate cryptographically-secure random bytes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Bytes-Random-Secure
Source0:        https://cpan.metacpan.org/modules/by-module/Bytes/Bytes-Random-Secure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::Random::Seed)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint) >= 3.03
BuildRequires:  perl(Scalar::Util) >= 1.21
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Time::HiRes)
%if %{with perl_Bytes_Random_Secure_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Statistics::Basic)
BuildRequires:  perl(Test::Warn)
%endif
Requires:       perl(Scalar::Util) >= 1.21
Requires:       perl(MIME::QuotedPrint) >= 3.03

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::QuotedPrint|Scalar::Util)\\)$

%description
Bytes::Random::Secure provides two interfaces for obtaining crypto-quality
random bytes. The simple interface is built around plain functions. For
greater control over the random number generator's seeding, there is an
object-oriented interface that provides much more flexibility.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Crypt::Random::Seed)
Requires:       perl(Math::Random::ISAAC)
Requires:       perl(MIME::QuotedPrint) >= 3.03
%if %{with perl_Bytes_Random_Secure_enables_optional_test}
Requires:       perl(Statistics::Basic)
Requires:       perl(Test::Warn)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Bytes-Random-Secure-%{version}
# Remove always skipped tests
for F in t/01-manifest.t t/02-pod.t t/03-pod-coverage.t t/04-perlcritic.t \
    t/05-kwalitee.t t/06-meta-yaml.t t/07-meta-json.t t/09-changes.t \
%if !%{with perl_Bytes_Random_Secure_enables_optional_test}
    t/21-bytes_random_tests.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Inspects unrelated files
rm %{buildroot}%{_libexecdir}/%{name}/t/00-boilerplate.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README examples
%dir %{perl_vendorlib}/Bytes
%dir %{perl_vendorlib}/Bytes/Random
%{perl_vendorlib}/Bytes/Random/Secure.pm
%{_mandir}/man3/Bytes::Random::Secure.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
