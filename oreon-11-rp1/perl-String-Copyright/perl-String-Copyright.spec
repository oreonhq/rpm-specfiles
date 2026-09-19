%global source0_hash 2e4d42405a00400891da361352498b38d9baae26d8d279c3d4e7e4626805b575

Name:           perl-String-Copyright
Version:        0.003014
Release:        9%{?dist}
Summary:        Representation of text-based copyright statements
License:        GPL-3.0-or-later

URL:            https://metacpan.org/release/String-Copyright
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/String-Copyright-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Number::Range)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(Set::IntSpan)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
String::Copyright Parses common styles of copyright statements and serializes
in normalized format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n String-Copyright-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::Copyright*.*

%changelog
%autochangelog
