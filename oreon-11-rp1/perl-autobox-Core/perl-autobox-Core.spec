%global source0_hash a9c396ebfaf8dcb881324a93d7d1a4dcd19c5e82fccc2ec6ee7a2aad324bd4e7

Name:           perl-autobox-Core
Version:        1.33
Release:        28%{?dist}
Summary:        Core functions exposed as methods in primitive types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/autobox-Core
Source0:        https://cpan.metacpan.org/modules/by-module/autobox/autobox-Core-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(autobox) >= 2.71
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Want) >= 0.26
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests only
BuildRequires:  perl(Test::Output)
# Dependencies
Requires:       perl(autobox) >= 2.71
Requires:       perl(Want) >= 0.26

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(autobox\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Want\\)$

%description
The autobox module lets you call methods on primitive data types such as
scalars and arrays.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n autobox-Core-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/autobox/
%{_mandir}/man3/autobox::Core.3*

%changelog
%autochangelog
