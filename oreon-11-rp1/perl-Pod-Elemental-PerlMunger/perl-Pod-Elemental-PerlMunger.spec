%global source0_hash 51895e4c41a079eadef9f24f5dc48e3245a5c06e3404ed79c85fa5cefeb795a9

Name:           perl-Pod-Elemental-PerlMunger
Version:        0.200007
Release:        9%{?dist}
Summary:        Take a string of Perl and rewrite its documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Elemental-PerlMunger
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Pod-Elemental-PerlMunger-%{version}.tar.gz
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
BuildRequires:  perl(Encode)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(PPI)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Pod::Elemental) >= 0.103000
BuildRequires:  perl(Test::More) >= 0.96
# Optional tests:
# Test::Differences not used

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Pod::Elemental|Test::More)\\)$

%description
This Moose role is to be included in classes that rewrite the documentation of
a Perl document, stripping out all the POD, munging it, and replacing it into
the Perl.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Pod::Elemental) >= 0.103000
Requires:       perl(Pod::Elemental::PerlMunger)
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Elemental-PerlMunger-%{version}

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
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Pod
%dir %{perl_vendorlib}/Pod/Elemental
%{perl_vendorlib}/Pod/Elemental/PerlMunger.pm
%{_mandir}/man3/Pod::Elemental::PerlMunger.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
