%global source0_hash 6142679580150a891f7d32232b5e31e2b4e5e53e8a6fa9cbeecb5c23814f1422
Name:           perl-XML-Validator-Schema
Version:        1.10
Release:        1%{?dist}
Summary:        Validate XML against a subset of W3C XML Schema
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Validator-Schema
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-Validator-Schema-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(XML::SAX) >= 0.12
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tree::DAG_Node)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
