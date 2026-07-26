%global source0_hash 02d4408d8698db18ca66ce9a947a331043f38ae77ce7188b35dfbacab9d8e8e2

Name:           perl-HTML-WikiConverter
Version:        0.68
Release:        48%{?dist}
Summary:        Perl module to convert HTML to wiki markup
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-WikiConverter
Source0:        https://cpan.metacpan.org/authors/id/D/DI/DIBERRI/HTML-WikiConverter-%{version}.tar.gz
Patch0:         HTML-WikiConverter-0.68-diberri.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# CGI::Application used by Test::Pod::Coverage test
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CSS) >= 1.07
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
# Getopt::Long not used at tests
# HTML::Element 3.18 version from HTML::Tree in META.yml
BuildRequires:  perl(HTML::Element) >= 3.18
BuildRequires:  perl(HTML::Entities) >= 1.27
BuildRequires:  perl(HTML::Tagset) >= 3.04
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Params::Validate) >= 0.77
# Pod::Usage 1.16 not used at tests
# Tie::IxHash used by Test::Pod::Coverage test
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(URI::Escape)
# XML::Writer used by Test::Pod::Coverage test
BuildRequires:  perl(XML::Writer)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(CSS) >= 1.07
# HTML::Element 3.18 version from HTML::Tree in META.yml
Requires:       perl(HTML::Element) >= 3.18
Requires:       perl(HTML::Entities) >= 1.27
Requires:       perl(HTML::Tagset) >= 3.04
Requires:       perl(Params::Validate) >= 0.77
Requires:       perl(URI) >= 1.35

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((CSS|HTML::Element|HTML::Entities|HTML::Tagset|Params::Validate|URI)\\)$

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML source
into a variety of wiki markups, called wiki "dialects". 

This package contains the perl modules; install the "html2wiki" package for the
application itself.

%package -n html2wiki
Summary:        Convert HTML to wiki markup
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Params::Validate) >= 0.77
Requires:       perl(Pod::Usage) >= 1.16

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Usage\\)$

%description -n html2wiki
A command line tool to convert pages in HTML to Wiki markup. Various wiki
dialects are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-WikiConverter-%{version}
%patch -P0
find webapp-install cgi/* -type f | xargs chmod 0644

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README webapp-install cgi
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n html2wiki
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
