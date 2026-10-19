%global source0_hash c4753d5a35f147eede09cdbd5e6d627dde3bdaaabfe9e56f2cff72b72d19979b
Name:           perl-Object-Realize-Later
Version:        4.00
Release:        1%{?dist}
Summary:        Delayed creation of objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Realize-Later
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Object-Realize-Later-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module helps you implementing delay loading of object-data.  While
creating a stub-object, Object::Realize::Later simulates you got the
real data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Realize-Later-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
