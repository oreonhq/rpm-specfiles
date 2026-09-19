%global source0_hash 63ebc04b761c5748a121006d0e2672a6836d39cfb9e0b42dda80c8161f7a1246

Name:		perl-Test-Modern
Version:	0.013
Release:	32%{?dist}
Summary:	Precision testing for modern perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Modern
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Modern-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.000
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter::Tiny) >= 0.030
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File) >= 1.08
BuildRequires:	perl(IO::Handle) >= 1.21
BuildRequires:	perl(Import::Into) >= 1.002000
BuildRequires:	perl(Module::Runtime) >= 0.012
BuildRequires:	perl(Moose::Util)
BuildRequires:	perl(Mouse::Util)
BuildRequires:	perl(Role::Tiny)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::API) >= 0.004
BuildRequires:	perl(Test::Deep) >= 0.111
BuildRequires:	perl(Test::Fatal) >= 0.007
BuildRequires:	perl(Test::LongString) >= 0.15
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Version)
BuildRequires:	perl(Test::Warnings) >= 0.009
BuildRequires:	perl(Try::Tiny) >= 0.15
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Data::Dumper)
# Optional Test Requirements
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Moose) >= 2.0600
BuildRequires:	perl(namespace::clean)
# Dependencies
Requires:	perl(B)
Requires:	perl(Moose::Util)
Requires:	perl(Mouse::Util)
Requires:	perl(Role::Tiny)
Requires:	perl(Scalar::Util)
Requires:	perl(Test::LongString) >= 0.15
Requires:	perl(Test::Pod)
Requires:	perl(Test::Pod::Coverage)
Requires:	perl(Test::Version)

%description
Test::Modern provides the best features of Test::More, Test::Fatal,
Test::Warnings, Test::API, Test::LongString, and Test::Deep, as well as ideas
from Test::Requires, Test::DescribeMe, Test::Moose, and Test::CleanNamespaces.

Test::Modern also automatically imposes strict and warnings on your script,
and loads IO::File (much of the same stuff Modern::Perl does).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Modern-%{version}

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
%license COPYRIGHT LICENSE
%doc Changes CONTRIBUTING CREDITS README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Modern.3*

%changelog
%autochangelog
