%global source0_hash 25ebbdb2444a0a599ae5e7a457d75e09efcdf3266a5c5700b1403ccb7488a4f3

Name:           perl-HTML-TreeBuilder-XPath
Version:        0.14
Release:        42%{?dist}
Summary:        Add XPath support to HTML::TreeBuilder
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-TreeBuilder-XPath
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/HTML-TreeBuilder-XPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::XPathEngine) >= 0.12

%{?filter_setup:
%filter_from_provides /perl(HTML::Element)/d
%?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTML::Element\\)

%description
This module adds typical XPath methods to HTML::TreeBuilder, to make it
easy to query a document.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TreeBuilder-XPath-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
