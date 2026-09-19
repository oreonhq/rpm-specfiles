%global source0_hash dc7774268b1471feec6a71c0251a20e589b47d00af984ee938e5bb77398373a8

Name:           perl-RDF-Trine-Node-Literal-XML
Version:        0.16
Release:        21%{?dist}
Summary:        RDF node class for XML literals
# Makefile.PL:  GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-Trine-Node-Literal-XML
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-Trine-Node-Literal-XML-%{version}.tar.gz
# Remove build-time dependencies not needed for packaging
Patch0:         RDF-Trine-Node-Literal-XML-0.16-Disable-release-management-in-Makefile.PL.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  libxml2 >= 2.6.27
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(XML::LibXML)
# Run-time:
BuildRequires:  perl(base)
# RDF::Trine::Error version from RDF::Trine in META
BuildRequires:  perl(RDF::Trine::Error) >= 0.111
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
Requires:       libxml2 >= 2.6.27
# RDF::Trine::Error version from RDF::Trine in META
Requires:       perl(RDF::Trine::Error) >= 0.111

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(RDF::Trine::Error\\)$

%description
This Perl module encapsulates XML literals into RDF objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RDF-Trine-Node-Literal-XML-%{version}
%patch -P0 -p1
# Remove bunlded modules
rm -rf inc/*
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
