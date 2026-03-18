Name:		perl-File-Slurp-Tiny
Version:	0.004
Release:	30%{?dist}
Summary:	A simple, sane and efficient file slurper
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-Slurp-Tiny
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-Slurp-Tiny-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
This module provides functions for fast and correct slurping and spewing
of files.

%prep
%setup -q -n File-Slurp-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Slurp::Tiny.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.004-30
- Prepare for Oreon 11 (RP1)
