%global source0_hash 89c3debceeceae8764f45d74023f8fbeee2d88399af67541dbdaa0b2bf2711a9
Name:           perl-String-CamelCase
Version:        0.04
Release:        23%{?dist}
Summary:        Convert underscore_text to CamelCase and back
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-CamelCase
Source0:        https://cpan.metacpan.org/authors/id/H/HI/HIO/String-CamelCase-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module exports two functions to convert underscore_text to CamelCase and
back again.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-CamelCase-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
