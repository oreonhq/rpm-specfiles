%global source0_hash 35af09a95aefbf16495894710098bf2185a84f39019b697bab97d4bb967107a5
Name:           perl-Class-DBI-Plugin-RetrieveAll
Version:        1.04
Release:        53%{?dist}
Summary:        More complex retrieve_all() for Class::DBI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Plugin-RetrieveAll
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Class-DBI-Plugin-RetrieveAll-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(Class::DBI::Plugin)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Class::DBI::Plugin)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Plugin-RetrieveAll-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
