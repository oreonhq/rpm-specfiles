%global source0_hash 3ad00993337a45ceb0def86894cbb7cc4e4ca26df72bcabd55cd106a4a08cdbb

Name:           perl-RDF-NS-Curated
Version:        1.006
Release:        7%{?dist}
Summary:        Curated set of RDF prefixes
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/RDF-NS-Curated
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-NS-Curated-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96

%description
This contains a list of prefix and URI pairs that are commonly used in RDF.
The intention is that prefixes in this list can be safely used in code that
has a long lifetime. The list has been derived mostly from W3C standards
documents, but also some popularity lists.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RDF-NS-Curated-%{version}

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
%doc Changes COPYRIGHT CREDITS README
%dir %{perl_vendorlib}/RDF
%dir %{perl_vendorlib}/RDF/NS
%{perl_vendorlib}/RDF/NS/Curated.pm
%{_mandir}/man3/RDF::NS::Curated.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
