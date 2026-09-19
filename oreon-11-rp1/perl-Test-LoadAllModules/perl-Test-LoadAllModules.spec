%global source0_hash 1b861f555020648a7481d4ad281a89e624187f89437a98b34635691b265e5cfe

Name:           perl-Test-LoadAllModules
Version:        0.022
Release:        35%{?dist}
Summary:        Do use_ok for the modules in a search path
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-LoadAllModules
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-LoadAllModules-%{version}.tar.gz
# Do not require unhelpful Module::Install::Base
Patch0:         Test-LoadAllModules-0.022-Do-not-require-Module-Install-Base.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)

%description
Test::LoadAllModules Perl module calls Test::More::use_ok() for the modules in
a search_path argument.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-LoadAllModules-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
