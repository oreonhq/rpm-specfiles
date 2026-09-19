%global source0_hash 6142679580150a891f7d32232b5e31e2b4e5e53e8a6fa9cbeecb5c23814f1422

Name:           perl-XML-Validator-Schema
Version:        1.10
Release:        47%{?dist}
Summary:        Validate XML against a subset of W3C XML Schema
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Validator-Schema
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Validator-Schema-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Tree::DAG_Node)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::SAX) >= 0.12
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(XML::SAX::ParserFactory)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.47
# Optional tests
BuildRequires:  perl(XML::SAX::Writer)
Requires:       perl(XML::SAX) >= 0.12

%description
This module allows you to validate XML documents against a W3C XML Schema.
This module does not implement the full W3C XML Schema recommendation
(http://www.w3.org/XML/Schema), but a useful subset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Validator-Schema-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ANNOUNCE Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
