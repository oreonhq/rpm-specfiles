%global source0_hash 2e082c51eccaf1398a37a3e4b753818768d8cd4276c9d2e72a258b30357ae4fb
Name:           perl-Palm
Version:        1.400
Release:        32%{?dist}
Summary:        Palm OS utility functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Palm
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl-p5-Palm = %{version}-%{release}
Obsoletes:      perl-p5-Palm =< 1.013-4
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Palm::PDB)
BuildRequires:  perl(Palm::Raw)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides functions and handlers to manipulate files used
by Palm PDAs (AddressBook, ToDo, Memo, ...).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Palm-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
