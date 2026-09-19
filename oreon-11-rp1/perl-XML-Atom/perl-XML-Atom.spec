%global source0_hash 4e593896a6f6e7cf2a796895108db567653589ffabf929a1e458a7bf6dbb0b2d

Name:           perl-XML-Atom
Version:        0.43
Release:        14%{?dist}
Summary:        Atom feed and API implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/XML-Atom
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-%{version}.tar.gz
# enable unicode tests (we have LibXML)
Patch0:         enable-unicode-tests.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
# Run-time:
# Apache::Constants not used at tests
BuildRequires:  perl(base)
# CGI not used at tests
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# HTML::Parser not used at tests
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.69
# XML::XPath not needed if XML::LibXML is available
# Optional run-time:
# DateTime::Format::Atom not used
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser)
# Optional tests:
# DateTime::Format::Atom not yet packaged
# not automatically detected
Requires:       perl(HTML::Parser)
Requires:       perl(XML::LibXML) >= 1.69

%{?perl_default_filter}

%description
Atom is a syndication, API, and archiving format for web blogs and other
data. XML::Atom implements the feed format as well as a client for the API.

%package Server
Summary:        Server for the Atom API
Requires:       perl(Apache::Constants)
Requires:       perl(CGI)

%description Server
XML::Atom::Server Perl module provides a base class for Atom API servers. It
handles all core server processing, both the SOAP and REST formats of the
protocol, and WSSE authentication. It can also run as either a mod_perl
handler or as part of a CGI program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Atom-%{version}
%patch -P 0 -p1

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%exclude %{perl_vendorlib}/XML/Atom/Server.pm
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/XML::Atom::Server.3*

%files Server
%doc Changes README
%license LICENSE
%{perl_vendorlib}/XML/Atom/Server.pm
%{_mandir}/man3/XML::Atom::Server.3*

%changelog
%autochangelog
