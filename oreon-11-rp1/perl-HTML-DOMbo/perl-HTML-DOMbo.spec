%global source0_hash 5971ab88db5a283a439cede83ef71f0b539f682867210fdce7262518087895a4

Name:           perl-HTML-DOMbo
Version:        3.10
Release:        50%{?dist}
Summary:        Convert between XML::DOM and {XML/HTML}::Element trees
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-DOMbo
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-DOMbo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Element)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(XML::Element)
Requires:       perl(XML::Element)

%{?perl_default_filter}

%description
This class puts a method into HTML::Element called to_XML_DOM, and puts
into the class XML::DOM::Node two methods, to_HTML_Element and
to_XML_Element.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-DOMbo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
