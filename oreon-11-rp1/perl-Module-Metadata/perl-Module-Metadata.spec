Name:		perl-Module-Metadata
Version:	1.000038
Release:	521%{?dist}
Summary:	Gather package and POD information from perl module files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Module-Metadata
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Metadata-%{version}.tar.gz
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
BuildRequires:	perl(Encode)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(version) >= 0.87
BuildRequires:	perl(warnings)
# Regular test suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(vars)
# Optional test requirements
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Dependencies
Requires:	perl(Encode)
Requires:	perl(Fcntl)

%description
This module provides a standard way to gather metadata about a .pm file
without executing unsafe code.

%prep
%setup -q -n Module-Metadata-%{version}

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
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Metadata.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.000038-521
- Prepare for Oreon 11 (RP1)
