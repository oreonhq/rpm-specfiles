%global source0_hash ce87ae26c61a65f7f52f716f5ef6baa63b125332c7aee072f56ee13bbb74edc0

Name:           perl-Class-Date
Version:        1.1.17
Release:        26%{?dist}
Summary:        Class for easy date and time manipulation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Date
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Class-Date-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Env::C)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  tzdata

Requires:       perl(Date::Parse)
Requires:       perl(Env::C)
Requires:       tzdata

%description
This module is intended to provide a general-purpose date and datetime type
for perl. You have a Class::Date class for absolute date and datetime, and
have a Class::Date::Rel class for relative dates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Date-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
