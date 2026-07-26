%global source0_hash 2dce1d68fde99d53db9ca43e211b69b169ba2efaecf87a55cb33a9336047c96d

Name:           perl-Email-Simple
Version:        2.218
Release:        9%{?dist}
Summary:        Simple parsing of RFC2822 message format and headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Dependencies
Requires:       perl(Email::Date::Format)

%description
"Email::Simple" is the first deliverable of the "Perl Email Project", a
reaction against the complexity and increasing bugginess of the
"Mail::*" modules. In contrast, "Email::*" modules are meant to be
simple to use and to maintain, pared to the bone, fast, minimal in their
external dependencies, and correct.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Simple.3*
%{_mandir}/man3/Email::Simple::Creator.3*
%{_mandir}/man3/Email::Simple::Header.3*

%changelog
%autochangelog
