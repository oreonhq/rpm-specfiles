Name:           perl-SGMLSpm
Version:        1.03ii
Release:        66%{?dist}
Summary:        Perl library for parsing the output of nsgmls

License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/SGMLSpm
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMEGG/SGMLSpm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
Requires:       openjade

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.


%prep
%setup -q -n SGMLSpm

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}
make install_system \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    PERL5DIR=$RPM_BUILD_ROOT%{perl_vendorlib}


%files
%doc README COPYING
%{_bindir}/sgmlspl
%{perl_vendorlib}/SGMLS*
%{perl_vendorlib}/skel.pl


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.03ii-66
- Prepare for Oreon 11 (RP1)
