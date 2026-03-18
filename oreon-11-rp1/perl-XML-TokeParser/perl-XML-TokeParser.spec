Name:           perl-XML-TokeParser
Version:        0.05
Release:        48%{?dist}
Summary:        Simplified interface to XML::Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/XML-TokeParser
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/XML-TokeParser-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(XML::Catalog)
BuildRequires:  perl(XML::Parser) >= 2
Requires:       perl(IO::File)
Requires:       perl(XML::Catalog)
Requires:       perl(XML::Parser) >= 2

%{?perl_default_filter}

%description
XML::TokeParser provides a procedural ("pull mode") interface to
XML::Parser in much the same way that Gisle Aas' HTML::TokeParser provides
a procedural interface to HTML::Parser. XML::TokeParser splits its XML
input up into "tokens," each corresponding to an XML::Parser event.

%prep
%setup -q -n XML-TokeParser-%{version}
find . -type f | xargs sed -i -e 's/\r//'
find . -type f | xargs chmod 0644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO TokeParser.xml
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.05-48
- Prepare for Oreon 11 (RP1)
