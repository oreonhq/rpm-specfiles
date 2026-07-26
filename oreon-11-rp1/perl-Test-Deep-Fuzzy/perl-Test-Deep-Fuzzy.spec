%global source0_hash f5c94fdd836b0d07187e297556986b0888d2cd5d136251962eed427580394daf

Name:           perl-Test-Deep-Fuzzy
Version:        0.01
Release:        21%{?dist}
Summary:        Fuzzy number comparison with Test::Deep
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Deep-Fuzzy
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARUPA/Test-Deep-Fuzzy-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(B)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Math::Round)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Cmp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Test::Deep::Fuzzy provides fuzzy number comparison with Test::Deep.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Deep-Fuzzy-%{version}

%build
perl ./Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
