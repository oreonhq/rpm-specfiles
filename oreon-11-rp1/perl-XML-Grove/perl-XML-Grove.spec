%global source0_hash fcb66d7df4ac29cb0edc1ea62c1750702caa6a86fc94790a94fcb1a36bd0d117

%global cpan_version 0.46alpha
Name:           perl-XML-Grove
Epoch:          1
Version:        0.46
Release:        0.26.alpha%{?dist}
Summary:        Simple access to infoset of parsed XML, HTML, or SGML instances

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Grove
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/XML-Grove-%{cpan_version}.tar.gz
Patch1:         perl-XML-Grove-test.patch
# Patch is based on upstream changes
# see http://perl-xml.cvs.sourceforge.net/perl-xml/XML-Grove/COPYING?revision=1.2&view=markup
Patch2:         perl-XML-Grove-fix-COPYING.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Data::Grove)
BuildRequires:  perl(Data::Grove::Visitor)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::Parser::PerlSAX)

%description
XML::Grove is a tree-based object model for accessing the information
set of parsed or stored XML, HTML, or SGML instances. XML::Grove
objects are Perl hashes and arrays where you access the properties of
the objects using normal Perl syntax.

# Remove bogus and redundant provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(My(HTML|Visitor)\\)|^perl\\(XML::Grove\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser::PerlSAX\\)$

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Grove-%{cpan_version}
%patch -P1 -p1 -b .test
%patch -P2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog Changes COPYING DOM README examples/
%doc %{perl_vendorlib}/XML/DOM-ecmascript.pod
%{perl_vendorlib}/XML/Grove*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
