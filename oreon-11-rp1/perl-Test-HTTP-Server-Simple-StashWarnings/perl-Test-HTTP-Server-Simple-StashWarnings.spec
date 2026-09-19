%global source0_hash ac754c43399308604a2065ec715697798979135a993972b9590a878fddd1b6b1

Name:           perl-Test-HTTP-Server-Simple-StashWarnings
Version:        0.04
Release:        47%{?dist}
Summary:        Catch your forked server's warnings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HTTP-Server-Simple-StashWarnings
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESSE/Test-HTTP-Server-Simple-StashWarnings-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.34
BuildRequires:  perl(Test::HTTP::Server::Simple)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(NEXT)
BuildRequires:  perl(Storable)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

BuildRequires:  perl(inc::Module::Install)

%description
Warnings are an important part of any application. Your web application
should warn the user when something is amiss.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-HTTP-Server-Simple-StashWarnings-%{version}
rm -r inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
