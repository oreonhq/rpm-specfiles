%global source0_hash 59a1c7173cac30db131c5f13fa3840f718588eef9b579352ffe156b550716d7c
Name:           perl-Feature-Compat-Try
Version:        0.05
Release:        1%{?dist}
Summary:        Make try/catch syntax available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Feature-Compat-Try
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Feature-Compat-Try-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Feature::Compat::Try)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Syntax::Keyword::Try)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module makes syntax support for try/catch control flow easily available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Feature-Compat-Try-%{version}
%oreon_prep
%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
