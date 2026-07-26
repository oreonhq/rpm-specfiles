%global source0_hash 09931d2af56bfcc4f67430e204daefc910e0ac5cfb280f2426a8ac2b48a8bb9b

Name:           perl-Mail-Alias
Version:        1.15
Release:        12%{?dist}
Summary:        Module for manipulating e-mail alias files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Alias
Source0:        https://cpan.metacpan.org/authors/id/J/JI/JIK/Mail-Alias-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(vars)

%description
This module allows direct manipulation of various types of E-Mail
Alias files. The primary use of Mail::Alias is for manipulating alias
files in the SENDMAIL alias file format. Additionally it is possible
to read some other formats and to convert between various alias file
formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Alias-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
