%global source0_hash c97cb1122cc6e3e4a079059da71e12f65760bfb0671d19d25a7ec7c5f1f240fb

Name:		perl-Test2-Plugin-NoWarnings
Version:	0.10
Release:	5%{?dist}
Summary:	Fail if tests warn
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test2-Plugin-NoWarnings
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) > 6.75
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test2) >= 1.302167
BuildRequires:	perl(Test2::API)
BuildRequires:	perl(Test2::Event)
BuildRequires:	perl(Test2::Util::HashBase)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Test2::Require::Module)
BuildRequires:	perl(Test2::V0)
BuildRequires:	perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

%description
Loading this plugin causes your tests to fail if there are any warnings while
they run. Each warning generates a new failing test and the warning content is
outputted via diag.

This module uses $SIG{__WARN__}, so if the code you're testing sets this, then
this module will stop working.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test2-Plugin-NoWarnings-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md README.md
%{perl_vendorlib}/Test2/
%{_mandir}/man3/Test2::Event::Warning.3*
%{_mandir}/man3/Test2::Plugin::NoWarnings.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10-5
- Prepare for Oreon 11 (RP1)
