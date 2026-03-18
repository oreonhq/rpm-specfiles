Name:           perl-Import-Into
Version:        1.002005
Release:        30%{?dist}
Summary:        Import packages into other packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Import-Into
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Import-Into-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
Loading Import::Into creates a global method import::into which you can call on
any package to import it into another package.

%prep
%setup -q -n Import-Into-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Import/
%{_mandir}/man3/Import::Into.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.002005-30
- Prepare for Oreon 11 (RP1)
