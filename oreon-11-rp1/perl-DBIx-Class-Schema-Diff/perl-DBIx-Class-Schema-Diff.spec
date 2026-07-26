%global source0_hash 3bbb4480f27ecd213ce4780ab568d1ca3783b2611cb38c72c1189b4a0549ebe3

Name:           perl-DBIx-Class-Schema-Diff
Version:        1.13
Release:        16%{?dist}
Summary:        Identify differences between two DBIx::Class schemas
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-Schema-Diff
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANSTYN/DBIx-Class-Schema-Diff-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Array::Diff)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Layout)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
General-purpose schema differ for DBIx::Class to identify changes between
two DBIC Schemas. Currently tracks added/deleted/changed events and deep
diffing across 5 named types of source data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Schema-Diff-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README README.md
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
%autochangelog
