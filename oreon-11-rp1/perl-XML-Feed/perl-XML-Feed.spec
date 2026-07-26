%global source0_hash 80d093ffbcaaeaa71f437758d010d7e748ec76d1f3e30e742354572cb725b1cc

Name:           perl-XML-Feed
Version:        1.0.0
Release:        2%{?dist}
Summary:        Syndication feed parser and auto-discovery
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-Feed
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-v%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(DateTime::Format::Flexible)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Feed::Find)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::Fetch)
BuildRequires:  perl(XML::Atom::Content) >= 0.38
BuildRequires:  perl(XML::Atom::Entry) >= 0.38
BuildRequires:  perl(XML::Atom::Feed) >= 0.38
BuildRequires:  perl(XML::LibXML) >= 1.66
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirement
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::RSS) >= 1.47
BuildRequires:  perl(XML::RSS::LibXML)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(vars)
Requires:       perl(Class::ErrorHandler)
Requires:       perl(XML::RSS) >= 1.47

%?perl_default_filter

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds. It also
implements feed auto-discovery for finding feeds, given a URI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Feed-v%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc ChangeLog.md README eg
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
%autochangelog
