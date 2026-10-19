%global source0_hash dc7774268b1471feec6a71c0251a20e589b47d00af984ee938e5bb77398373a8
Name:           perl-RDF-Trine-Node-Literal-XML
Version:        0.16
Release:        1%{?dist}
Summary:        RDF node class for XML literals
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-Trine-Node-Literal-XML
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-Trine-Node-Literal-XML-%{version}.tar.gz
Patch0:         RDF-Trine-Node-Literal-XML-0.16-Disable-release-management-in-Makefile.PL.patch
BuildArch:      noarch
Requires:       libxml2 >= 2.6.27
Requires:       perl(RDF::Trine::Error) >= 0.111
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(RDF::Trine::Error\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(RDF::Trine::Error)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
