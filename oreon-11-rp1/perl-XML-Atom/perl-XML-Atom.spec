%global source0_hash 4e593896a6f6e7cf2a796895108db567653589ffabf929a1e458a7bf6dbb0b2d
Name:           perl-XML-Atom
Version:        0.43
Release:        1%{?dist}
Summary:        Atom feed and API implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Atom
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/XML-Atom-%{version}.tar.gz
Patch0:         enable-unicode-tests.patch
BuildArch:      noarch
Requires:       perl(HTML::Parser)
Requires:       perl(XML::LibXML) >= 1.69
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Atom-Server -f %{oreon_filedir}/perl-XML-Atom-Server.list

%changelog

%autochangelog
