%global source0_hash 11dcc5b22ae99f3e1b81c2372de11de8bd6d7c8c9d1a19d23136dd0143b428fc

Name:           perl-DBICx-AutoDoc
Version:        0.09
Release:        26%{?dist}
Summary:        Generate automatic documentation of DBIx::Class::Schema objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/DBICx-AutoDoc
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/DBICx-AutoDoc-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Relationship::Helpers)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
DBICx::AutoDoc is a utility that can automatically generate documentation
for your DBIx::Class schemas. It works by collecting information from
several sources and arranging it into a format that makes it easier to deal
with from templates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBICx-AutoDoc-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{_bindir}/dbicx-autodoc
%{_mandir}/man1/dbicx-autodoc.1.gz
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
%autochangelog
