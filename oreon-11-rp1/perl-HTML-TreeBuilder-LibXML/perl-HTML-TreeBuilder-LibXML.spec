%global source0_hash 057773f848bf08cff672ca3837c1932f868a63bd6d80a483ab70ca61869df3b4
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-HTML-TreeBuilder-LibXML
Version:        0.28
Release:        1%{?dist}
Summary:        HTML::TreeBuilder and XPath compatible interface with libxml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-TreeBuilder-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTML-TreeBuilder-LibXML-%{version}.tar.gz
BuildArch:      noarch
%if 0%{!?perl_bootstrap:1}
%endif
Requires:       perl(HTML::TreeBuilder::XPath) >= 0.14
Requires:       perl(XML::LibXML) >= 1.7
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::LibXML\\)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Web::Scraper)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
