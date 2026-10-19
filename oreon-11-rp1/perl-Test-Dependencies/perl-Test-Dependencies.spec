%global source0_hash 2a870e37140686c0721bef1d28356ea377bc23317c58fe4df0f42ee2e4796990
Name:           perl-Test-Dependencies
Version:        0.34
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Ensure that your Makefile.PL specifies all module dependencies
Source0:        https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Test-Dependencies-%{version}.tar.gz
Url:            https://metacpan.org/release/Test-Dependencies
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Pod::Strip)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(base)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
