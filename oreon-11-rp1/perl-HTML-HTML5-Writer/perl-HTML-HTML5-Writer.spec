%global source0_hash 5376f37884b21b7424018e97088dfa64ccc5517ab687238b0d01da601c69b420
Name:           perl-HTML-HTML5-Writer
Version:        0.201
Release:        1%{?dist}
Summary:        Output a DOM as HTML5
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-HTML5-Writer
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Writer-%{version}.tar.gz
Patch0:         HTML-HTML5-Writer-0.201-Break-build-cycle-with-Module-Package-RDF.patch
BuildArch:      noarch
Requires:       perl(XML::LibXML) >= 1.60
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This Perl module outputs XML::LibXML::Node objects as HTML5 strings. It works
well on DOM trees that represent valid HTML/XHTML documents; less well on
other DOM trees.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-HTML5-Writer-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
