%global source0_hash 90bf175a60b6768b0e9375ac16efc85900058c3af62e52dc8e87b18d98a04c83

Name:           perl-Term-Chrome
Version:        2.01
Release:        24%{?dist}
Summary:        DSL for colors and other terminal chrome
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Chrome
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Term-Chrome-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::Is) >= 20140823
BuildRequires:  perl(Test::More) >= 0.96
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Requires) >= 0.05
# Optional tests:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Test::Synopsis) >= 0.14

%description
Term::Chrome is a domain-specific language (DSL) for terminal decoration
(colors and other attributes) in Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Chrome-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export EXTENDED_TESTING=1
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
