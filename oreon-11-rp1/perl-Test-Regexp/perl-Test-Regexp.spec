%global source0_hash 35cb41df5c5017835b89b853d5a44e25e6da973b450e1edca51bba70e7041e54
Name:		perl-Test-Regexp
Version:	2017040101
Release:        1%{?dist}
Summary:        Test your regular expressions
License:	MIT
URL:		https://metacpan.org/release/Test-Regexp
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Regexp-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Test::Regexp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(charnames)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is intended to test your regular expressions. Given a subject
string and a regular expression (a.k.a. pattern), the module not only tests
whether the regular expression completely matches the subject string, it
performs a utf8::upgrade or utf8::downgrade on the subject string and
performs the tests again, if necessary. Furthermore, given a pattern with
capturing parenthesis, it checks whether all captures are present, and in the
right order. Both named and unnamed captures are checked.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Regexp-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
