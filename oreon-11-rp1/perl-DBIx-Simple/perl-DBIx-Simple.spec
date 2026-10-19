%global source0_hash 46d311aa2ce08907401c56119658426dbb044c5a40de73d9a7b79bf50390cae3
Name:           perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.37
Release:        26%{?dist}
License:        MIT
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz
URL:            https://metacpan.org/release/DBIx-Simple
BuildArch:      noarch
Requires:       perl(DBI) >= 1.21
Requires:       perl(DBIx::XHTML_Table)
Requires:       perl(SQL::Abstract)
Requires:       perl(SQL::Interp)
Requires:       perl(Text::Table)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(SQL::Interp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Simple-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
