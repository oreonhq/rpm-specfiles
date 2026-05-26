Name:           perl-XML-DOM
Version:        1.46
Release:        28%{?dist}
Summary:        DOM extension to XML::Parser

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-DOM
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-DOM-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8ba24b0b459b01d6c5e5b0408829c7d5dfe47ff79b3548c813759048099b175e
%global source0_file XML-DOM-1.46.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Parser) >= 2.30
BuildRequires:  perl(XML::RegExp)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::Parser::PerlSAX) >= 0.07
Requires:       perl(XML::Parser) >= 2.30
Obsoletes:      perl-libxml-enno <= 1.02

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(XML::XQL::Node\\)

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'DOM', that allows XML::Parser to build an Object
Oriented data structure with a DOM Level 1 compliant interface. For a
description of the DOM (Document Object Model), see
<http://www.w3.org/DOM/>.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/XML-DOM-1.46.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8ba24b0b459b01d6c5e5b0408829c7d5dfe47ff79b3548c813759048099b175e" || { echo "oreon: Source0 SHA256 mismatch for XML-DOM-1.46.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n XML-DOM-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc BUGS Changes README
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::*.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.46-28
- Prepare for Oreon 11 (RP1)
