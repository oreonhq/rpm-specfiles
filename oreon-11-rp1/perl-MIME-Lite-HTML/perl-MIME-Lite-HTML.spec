%global source0_hash db603ccbf6653bcd28cfa824d72e511ead019fc8afb9f1854ec872db2d3cd8da

Name:           perl-MIME-Lite-HTML
Version:        1.24
Release:        42%{?dist}
Summary:        Provide routine to transform a HTML page in a MIME-Lite mail
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Lite-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/MIME/MIME-Lite-HTML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test)

%description
This module is a Perl mail client interface for sending message that
support HTML format and build them for you.. This module provides routine to
transform an HTML page in a MIME::Lite mail. So you need this module to use
MIME-Lite-HTML possibilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MIME-Lite-HTML-%{version}
chmod a-x README Changes HTML.pm
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8 && \
touch -r Changes Changes.utf8 && \
mv -f Changes.utf8 Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# The 2 following tests are broken by MIME::Lite 3.029
# Headers order is not quaranteed so relying on that to test the module is
# doomed to fail.
# Relevant bugs :
# MIME::Lite::HTML : http://rt.cpan.org/Public/Bug/Display.html?id=86020
# MIME::Lite : https://rt.cpan.org/Public/Bug/Display.html?id=79944
rm -f t/20create_image_part.t t/50generic.t 
make test

%files
%doc Changes COPYING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
