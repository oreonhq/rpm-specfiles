%global source0_hash 593da54b522c09cc26bbcc0e4e49c1c8e688a6fd33b0726af801d722a5c8d0f1
%bcond_without perl_Crypt_Random_Seed_enables_egd
Name:           perl-Crypt-Random-Seed
Version:        0.03
Release:        1%{?dist}
Summary:        Simple method to get strong randomness
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-Random-Seed
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Random-Seed-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Crypt_Random_Seed_enables_egd}
Recommends:     egd
Recommends:     perl(IO::Socket)
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A simple mechanism to get strong randomness. The main purpose of this
module is to provide a simple way to generate a seed for a PRNG such as
Math::Random::ISAAC, for use in cryptographic key generation, or as the
seed for an upstream module such as Bytes::Random::Secure. Flags for
requiring non-blocking sources are allowed, as well as a very simple method
for plugging in a source.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.45
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Random-Seed-%{version}
# Remove always skipped tests
for F in t/04-win32.t \
    t/90-release-perlcritic.t t/91-release-pod-syntax.t \
    t/92-release-pod-coverage.t t/93-release-kwalitee.t \
    t/94-release-manifest.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Correct shebangs
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Crypt-Random-Seed-tests -f %{oreon_filedir}/perl-Crypt-Random-Seed-tests.list

%changelog

%autochangelog
