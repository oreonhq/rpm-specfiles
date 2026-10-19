%global source0_hash 2dce1d68fde99d53db9ca43e211b69b169ba2efaecf87a55cb33a9336047c96d
Name:           perl-Email-Simple
Version:        2.218
Release:        1%{?dist}
Summary:        Simple parsing of RFC2822 message format and headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Simple-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Email::Date::Format)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
