%global source0_hash c4753d5a35f147eede09cdbd5e6d627dde3bdaaabfe9e56f2cff72b72d19979b

Name:           perl-Object-Realize-Later
Version:        4.00
Release:        2%{?dist}
Summary:        Delayed creation of objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Realize-Later
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Object-Realize-Later-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Log::Report) >= 1.42
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test)
BuildArch:      noarch

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

%check
make test

%files
%doc README.md
%{perl_vendorlib}/Object/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
