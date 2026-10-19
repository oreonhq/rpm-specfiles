%global source0_hash db603ccbf6653bcd28cfa824d72e511ead019fc8afb9f1854ec872db2d3cd8da
Name:           perl-MIME-Lite-HTML
Version:        1.24
Release:        1%{?dist}
Summary:        Provide routine to transform a HTML page in a MIME-Lite mail
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Lite-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/MIME/MIME-Lite-HTML-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Test)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

rm -f t/20create_image_part.t t/50generic.t 
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
