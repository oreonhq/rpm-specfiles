%global source0_hash 2a870e37140686c0721bef1d28356ea377bc23317c58fe4df0f42ee2e4796990

Name:           perl-Test-Dependencies
Version:        0.34
Release:        4%{?dist}
# see lib/Test/Dependencies.pm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Ensure that your Makefile.PL specifies all module dependencies
Source:         https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Test-Dependencies-%{version}.tar.gz
Url:            https://metacpan.org/release/Test-Dependencies
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Strip)
BuildRequires:  perl(Test::Builder::Module)
# Tests:
BuildRequires:  perl(Test::Builder::Tester) >= 0.64
BuildRequires:  perl(Test::More) >= 1.30
BuildRequires:  perl(Test::Needs)

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

It has two styles: light, which is fast but confusable; and heavy, which takes
more time but is more accurate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Dependencies-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README README.md Changes
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*.3*

%changelog
%autochangelog
