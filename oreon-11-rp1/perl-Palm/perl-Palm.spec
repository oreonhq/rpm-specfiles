%global source0_hash 2e082c51eccaf1398a37a3e4b753818768d8cd4276c9d2e72a258b30357ae4fb

Name:           perl-Palm
Version:        1.400
Release:        32%{?dist}
Summary:        Palm OS utility functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Palm
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Palm::PDB)
BuildRequires:  perl(Palm::Raw)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Provides:       perl-p5-Palm = %{version}-%{release}
Obsoletes:      perl-p5-Palm =< 1.013-4
%{?perl_default_filter}

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

%check
make test

%files
%license LICENSE
%doc Changes FAQ README TODO examples
%{perl_vendorlib}/Palm*
%{_mandir}/man3/Palm*

%changelog
%autochangelog
