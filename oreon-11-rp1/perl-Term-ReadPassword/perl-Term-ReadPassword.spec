%global source0_hash e1a866345b35f9ffef7d0037e13d6d4cb280310089f98c20713880bc70fb4323

Name:           perl-Term-ReadPassword
Version:        0.11
Release:        49%{?dist}
Summary:        Asking the user for a password
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ReadPassword
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHOENIX/Term-ReadPassword-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(vars)
# Tests only
# -

%description
This module lets you ask the user for a password in the traditional way,
from the keyboard, without echoing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-ReadPassword-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
