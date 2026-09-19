%global source0_hash c4e2e067d5065d6b692a713826dec2e9e8e5fc4a9c3548796a38d4e205f7181c

# This file is lincesed under the terms of GNU GPLv2+.
Name:           perl-Perl-Critic-Tics
Version:        0.010
Release:        9%{?dist}
Summary:        Policies for things that make me wince
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Tics
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Perl-Critic-Tics-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Violation)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests
# CPAN::Meta not helpful
Requires:       perl(Perl::Critic::Violation)

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
The Perl-Critic-Tics distribution includes extra policies for Perl::Critic
to address a fairly random assortment of things that make me (rjbs) wince.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Tics-%{version}

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
%doc Changes README
%dir %{perl_vendorlib}/Perl
%dir %{perl_vendorlib}/Perl/Critic
%dir %{perl_vendorlib}/Perl/Critic/Policy
%{perl_vendorlib}/Perl/Critic/Policy/Tics
%{perl_vendorlib}/Perl/Critic/Tics.pm
%{_mandir}/man3/Perl::Critic::Policy::Tics::*
%{_mandir}/man3/Perl::Critic::Tics.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
