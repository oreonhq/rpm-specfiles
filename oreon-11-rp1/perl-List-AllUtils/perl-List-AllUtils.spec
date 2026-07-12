%global source0_hash 30a8146ab21a7787b8c56d5829cf9a7f2b15276d3b3fca07336ac38d3002ffbc

Name:           perl-List-AllUtils
Version:        0.19
Release:        16%{?dist}
Summary:        Combines List::Util and List::SomeUtils
# CODE_OF_CONDUCT.md:   CC-BY-4.0
# lib/List/AllUtils.pm: Artistic-2.0
License:        Artistic-2.0 AND CC-BY-4.0
URL:            https://metacpan.org/release/List-AllUtils
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::SomeUtils) >= 0.58
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(List::UtilsBy) >= 0.11
# Tests:
# CPAN::Meta not useful
# CPAN::Meta::Prereqs not usedful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::Util\\) >= 1\.56$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Sub::Util|Test::More)\\)$

Provides:       perl(List::AllUtils)
%description
Are you sick of trying to remember whether a particular helper is defined
in List::Util or List::SomeUtils? I sure am. Now you don't have to remember.
This module will export all of the functions that either of those two
modules defines.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(List::Util) >= 1.56
Requires:       perl(Sub::Util)
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n List-AllUtils-%{version}
for F in \
    t/00-report-prereqs.dd \
    t/00-report-prereqs.t \
    ; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
