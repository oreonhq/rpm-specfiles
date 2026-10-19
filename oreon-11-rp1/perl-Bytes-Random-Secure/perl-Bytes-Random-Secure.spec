%global source0_hash 53bbd339e6a11efca07c619a615c7c188a68bb2be849a1cb7efc3dd4d9ae85ae
%bcond_without perl_Bytes_Random_Secure_enables_optional_test
Name:           perl-Bytes-Random-Secure
Version:        0.29
Release:        1%{?dist}
Summary:        Perl extension to generate cryptographically-secure random bytes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Bytes-Random-Secure
Source0:        https://cpan.metacpan.org/modules/by-module/Bytes/Bytes-Random-Secure-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Bytes_Random_Secure_enables_optional_test}
%endif
Requires:       perl(Scalar::Util) >= 1.21
Requires:       perl(MIME::QuotedPrint) >= 3.03
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::QuotedPrint|Scalar::Util)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::Random::Seed)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Statistics::Basic)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-boilerplate.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Bytes-Random-Secure-tests -f %{oreon_filedir}/perl-Bytes-Random-Secure-tests.list

%changelog

%autochangelog
