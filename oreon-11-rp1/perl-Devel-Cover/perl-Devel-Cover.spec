%global source0_hash 9d90b44ab602ca373fa221255708de4d19df86026f4d7110bef608846eed44fb

Name:           perl-Devel-Cover
Version:        1.52
Release:        2%{?dist}
Summary:        Code coverage metrics for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Cover
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.38.0
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(B::Concise)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
# CPAN::Releases::Latest not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities) >= 3.69
# JSON or JSON::PP by Devel::Cover::DB::IO::JSON
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Moo)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Parallel::Iterator)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI::HTML) >= 1.07
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Template) >= 2.00
BuildRequires:  perl(Template::Provider)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Optional run-time:
# Browser::Open not used at tests
# (PPI && PPI::HTML 1.07) || Perl::Tidy 20060719
# Perl::Tidy 20060719 not used at tests
BuildRequires:  perl(Pod::Coverage) >= 0.06
BuildRequires:  perl(Pod::Coverage::CountParents)
# PPI::HTML 1.07 not used at tests 
BuildRequires:  perl(Test::Differences)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(DBM::Deep)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moose)
BuildRequires:  perl(overload)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
# CPAN::Releases::Latest not yet packaged
# JSON or JSON::PP by Devel::Cover::DB::IO::JSON
Requires:       perl(JSON)

%{?perl_default_filter}

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Cover::Dumper\\)
# Fiter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Template\\)$

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

%check
make test

%files
%doc Changes CLAUDE.md README.md docs/BUGS docs/TODO
%{_bindir}/cover
%{_bindir}/cpancover
%{_bindir}/gcov2perl
%{perl_vendorarch}/Devel/
%{perl_vendorarch}/auto/Devel/
%{_mandir}/man1/cover.1*
%{_mandir}/man1/cpancover.1*
%{_mandir}/man1/gcov2perl.1*
%{_mandir}/man3/Devel::Cover*.3*

%changelog
%autochangelog
