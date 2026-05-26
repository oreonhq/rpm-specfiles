Name:           perl-SGMLSpm
Version:        1.03ii
Release:        66%{?dist}
Summary:        Perl library for parsing the output of nsgmls

License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/SGMLSpm
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMEGG/SGMLSpm-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 f06895c0206dada9f9e7f07ecaeb6a3651fd648f4820f49c1f76bfeaec2f2913
%global source0_file SGMLSpm-1.03ii.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
Requires:       openjade

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/SGMLSpm-1.03ii.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f06895c0206dada9f9e7f07ecaeb6a3651fd648f4820f49c1f76bfeaec2f2913" || { echo "oreon: Source0 SHA256 mismatch for SGMLSpm-1.03ii.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
