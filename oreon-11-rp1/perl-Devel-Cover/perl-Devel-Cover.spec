%global source0_hash 9d90b44ab602ca373fa221255708de4d19df86026f4d7110bef608846eed44fb
Name:           perl-Devel-Cover
Version:        1.52
Release:        2%{?dist}
Summary:        Code coverage metrics for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Cover
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(JSON)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Cover::Dumper\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Template\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Concise)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBM::Deep)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI::HTML)
BuildRequires:  perl(Parallel::Iterator)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Provider)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides code coverage metrics for Perl. Code coverage metrics
describe how thoroughly tests exercise code. By using Devel::Cover you can
discover areas of code not exercised by your tests and determine which
tests to create to increase coverage. Code coverage can be considered as an
indirect measure of quality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Cover-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
