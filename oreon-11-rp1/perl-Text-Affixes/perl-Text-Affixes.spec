%global source0_hash 7d0808f7194d7a68786fee8fedc36414c69029c460cc41efe608d2bbfb3dcc5e

Name:           perl-Text-Affixes
Summary:        Prefixes and suffixes analysis of text
Version:        0.09
Release:        30%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Affixes
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COG/Text-Affixes-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%{?perl_default_filter}

%description
Provides methods for prefixes and suffixes analysis of text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Affixes-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{_mandir}/man3/Text::Affixes.3pm*
%{perl_vendorlib}/Text

%changelog
%autochangelog
