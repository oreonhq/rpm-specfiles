%global source0_hash d4c6e9d47448486b746b6b6cb562db88c1802d588f63f6ddeccf7305f3738e81
Name:           perl-Regexp-Pattern-License
Version:        3.11.2
Release:        1%{?dist}
Summary:        Regular expressions for legal licenses
License:        GPL-3.0-or-later
BuildArch:      noarch
URL:            https://metacpan.org/release/Regexp-Pattern-License
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/Regexp-Pattern-License-v%{version}.tar.gz
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Regexp::Pattern)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Regexp::Pattern)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(open)
BuildRequires:  perl(re::engine::RE2)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Regexp::Pattern::License provides a hash of regular expression patterns related
to legal software licenses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Regexp-Pattern-License-v%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
