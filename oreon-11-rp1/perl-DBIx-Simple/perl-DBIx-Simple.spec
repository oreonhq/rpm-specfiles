%global source0_hash 46d311aa2ce08907401c56119658426dbb044c5a40de73d9a7b79bf50390cae3

Name:           perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.37
Release:        26%{?dist}
# This license is a little weird. It used to be in the Public Domain until after 1.32.
# Now, it is released under any OSI approved license.
# Since that is a sort of metalicense (and we do not want to encourage it), we will just choose
# MIT for maximum compatibility.
License:        MIT
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz 
URL:            https://metacpan.org/release/DBIx-Simple
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1.21
# DBIx::XHTML_Table - not used for test
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(overload)
# SQL::Abstract - not used for test
BuildRequires:  perl(SQL::Interp)
BuildRequires:  perl(strict)
# Text::Table - not used for test
# Tests
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::More)
Requires:       perl(DBI) >= 1.21
Requires:       perl(DBIx::XHTML_Table)
Requires:       perl(SQL::Abstract)
Requires:       perl(SQL::Interp)
Requires:       perl(Text::Table)

%{?perl_default_filter}

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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
