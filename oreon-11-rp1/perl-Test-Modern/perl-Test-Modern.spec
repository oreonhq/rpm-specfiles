%global source0_hash 63ebc04b761c5748a121006d0e2672a6836d39cfb9e0b42dda80c8161f7a1246
Name:		perl-Test-Modern
Version:	0.013
Release:        1%{?dist}
Summary:        Precision testing for modern perl
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Modern
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Modern-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(B)
Requires:	perl(Moose::Util)
Requires:	perl(Mouse::Util)
Requires:	perl(Role::Tiny)
Requires:	perl(Scalar::Util)
Requires:	perl(Test::LongString) >= 0.15
Requires:	perl(Test::Pod)
Requires:	perl(Test::Pod::Coverage)
Requires:	perl(Test::Version)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::API)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Version)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
