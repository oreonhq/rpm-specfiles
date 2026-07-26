%global source0_hash a184ca241caf97c57fd37f18e0fe686ef79cfe8eede7e31d93f3e636ed011169

Name:           perl-HTML-HTML5-Parser
Version:        0.992
Release:        12%{?dist}
Summary:        Parse HTML reliably
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-HTML5-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
# These Encode modules do not exist, CPAN RT#118661
# Encode::EUCJP1997 does not exist
# Encode::GLJIS1978 does not exist
# Encode::GLJIS1983 does not exist
# Encode::GLJIS1997 does not exist
# Encode::GLJIS1997Swapped does not exist
# Encode::ShiftJIS1997 does not exist
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(HTML::HTML5::Entities) >= 0.002
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.94
BuildRequires:  perl(XML::LibXML::Devel)
# Optional run-time:
BuildRequires:  perl(XML::LibXML::Devel::SetLineNumber)
# Tests:
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.61
BuildRequires:  perl(Test::Requires)
# Optional tests:
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(URI::Escape)
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter)
Requires:       perl(HTML::HTML5::Entities) >= 0.002
Requires:       perl(XML::LibXML) >= 1.94
Recommends:     perl(XML::LibXML::Devel::SetLineNumber)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTML::HTML5::Entities|XML::LibXML)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(HTML::HTML5::Parser::TagSoupParser\\)$

%description
HTML parser with XML::LibXML-like DOM interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-HTML5-Parser-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS NEWS README TODO examples
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
