%global source0_hash 057773f848bf08cff672ca3837c1932f868a63bd6d80a483ab70ca61869df3b4

Name:           perl-HTML-TreeBuilder-LibXML
Version:        0.28
Release:        5%{?dist}
Summary:        HTML::TreeBuilder and XPath compatible interface with libxml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-TreeBuilder-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-TreeBuilder-LibXML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(HTML::TreeBuilder::XPath) >= 0.14
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(XML::LibXML) >= 1.7

# perl-Web-Scraper requires HTML::TreeBuilder::LibXML so don't pull
# in this optional test requirement when bootstrapping (#982293)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Web::Scraper)
%endif

# not picked up by rpm deptracker
Requires:       perl(HTML::TreeBuilder::XPath) >= 0.14
Requires:       perl(XML::LibXML) >= 1.7

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::LibXML\\)

%description
HTML::TreeBuilder::XPath is a libxml based compatible interface to
HTML::TreeBuilder, which could be slow for a large document.
HTML::TreeBuilder::LibXML is drop-in-replacement for HTML::TreeBuilder::XPath.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TreeBuilder-LibXML-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
