Name:		perl-ExtUtils-Config
Version:	0.010
Release:	4%{?dist}
Summary:	A wrapper for perl's configuration
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/ExtUtils-Config
Source0:	https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-Config-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.6
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module
BuildRequires:	perl(Config)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(ExtUtils::MakeMaker::Config)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
Requires:	perl(Data::Dumper)

%description
ExtUtils::Config is an abstraction around the %%Config hash.

%prep
%setup -q -n ExtUtils-Config-%{version}

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
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::Config.3*
%{_mandir}/man3/ExtUtils::Config::MakeMaker.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.010-4
- Prepare for Oreon 11 (RP1)
