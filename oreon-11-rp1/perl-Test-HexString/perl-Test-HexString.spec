%global source0_hash 7d4c4cdc192f2594dc78ff75eb2cf4d0561f794b36ee0eacee8c4a1aa8a03f40
Name:           perl-Test-HexString
Version:        0.03
Release:        1%{?dist}
Summary:        Test binary strings with hex dump diagnostics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HexString
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-HexString-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::Builder)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This testing module provides a single function, is_hexstr(), which asserts
that the given string matches what was expected. When the strings match
(i.e. compare equal using the eq operator), the behaviour is identical to
the usual is() function provided by Test::More.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-HexString-%{version}

%build

%{__perl} Build.PL installdirs=vendor
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
