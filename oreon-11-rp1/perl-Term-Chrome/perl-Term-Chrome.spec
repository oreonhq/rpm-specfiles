%global source0_hash 90bf175a60b6768b0e9375ac16efc85900058c3af62e52dc8e87b18d98a04c83
Name:           perl-Term-Chrome
Version:        2.01
Release:        1%{?dist}
Summary:        DSL for colors and other terminal chrome
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Chrome
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Term-Chrome-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Is)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

export EXTENDED_TESTING=1
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
