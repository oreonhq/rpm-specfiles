%global source0_hash a184ca241caf97c57fd37f18e0fe686ef79cfe8eede7e31d93f3e636ed011169
Name:           perl-HTML-HTML5-Parser
Version:        0.992
Release:        12%{?dist}
Summary:        Parse HTML reliably
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-HTML5-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Parser-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter)
Requires:       perl(HTML::HTML5::Entities) >= 0.002
Requires:       perl(XML::LibXML) >= 1.94
Recommends:     perl(XML::LibXML::Devel::SetLineNumber)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTML::HTML5::Entities|XML::LibXML)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(HTML::HTML5::Parser::TagSoupParser\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Devel)
BuildRequires:  perl(XML::LibXML::Devel::SetLineNumber)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
