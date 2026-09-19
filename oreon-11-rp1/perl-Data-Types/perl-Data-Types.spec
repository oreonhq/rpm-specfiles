%global source0_hash 860751feb79b7dfc1af71c4b7fe920220ec6d31c4ab9402b8f178f7f4b8293c1

Name:           perl-Data-Types
Version:        0.17
Release:        21%{?dist}
Summary:        Validate and convert data types
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Types
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Data-Types-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.17
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(vars)

%description
This module exports a number of functions that are useful for validating
and converting data types. It is intended for use in applications where
data types are more important than they typically are in Perl -- e.g.,
database applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Types-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -a \( -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
