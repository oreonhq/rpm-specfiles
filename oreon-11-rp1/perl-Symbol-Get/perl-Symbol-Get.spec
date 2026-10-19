%global source0_hash 5595ddf7876d17fb470dd3bbb2a89ed6d8f2a1f57d9450b49fba207761582a5d
Name:           perl-Symbol-Get
Version:        0.12
Release:        1%{?dist}
Summary:        Read Perl’s symbol table programmatically
License:        MIT
URL:            https://metacpan.org/dist/Symbol-Get
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/Symbol-Get-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(Call::Context)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Occasionally I have need to reference a variable programmatically. This
module facilitates that by providing an easy, syntactic-sugar-y,
read-only interface to the symbol table.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Symbol-Get-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
