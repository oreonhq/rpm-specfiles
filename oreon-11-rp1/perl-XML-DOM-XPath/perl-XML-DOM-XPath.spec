%global source0_hash 0173a74a515211997a3117a47e7b9ea43594a04b865b69da5a71c0886fa829ea

Name:           perl-XML-DOM-XPath
Version:        0.14
Release:        51%{?dist}
Summary:        Perl extension to add XPath support to XML::DOM, using XML::XPath engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-DOM-XPath
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-DOM-XPath-%{version}.tar.gz
Patch0:         XML-DOM-XPath-0.14-Remove-deprecated-pragma-encoding.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(XML::XPathEngine) >= 0.10
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(warnings)
Requires:       perl(XML::XPathEngine) >= 0.10

# Remove provides which clash with symbols from perl-XML-DOM
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(XML::DOM::(Attr|Comment|Document)\\)
%global __provides_exclude %__provides_exclude|perl\\(XML::DOM::(Element|Namespace|Node|ProcessingInstruction|Text)\\)
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::XPathEngine\\)$

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This
is often much easier than relying only on getElementsByTagName.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-DOM-XPath-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
