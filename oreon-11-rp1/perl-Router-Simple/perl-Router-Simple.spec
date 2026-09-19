%global source0_hash 334615620f38eee15620ccdbf2dbd8b0a403ba1610e5b27d51737d8b0fb0c89d

Name:           perl-Router-Simple
Version:        0.17
Release:        32%{?dist}
Summary:        Simple HTTP router
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Router-Simple
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Router-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Router::Simple is a simple router class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Router-Simple-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Router
%{_mandir}/man3/*

%changelog
%autochangelog
