%global source0_hash aa9662a441e2174db77d55491621c4dc3a88fd2a594d4a79d842faee30e332d5
Name:           perl-Net-eBay
Version:        0.66
Release:        1%{?dist}
Summary:        Perl Interface to XML based eBay API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-eBay
Source0:        https://cpan.metacpan.org/authors/id/I/IC/ICHUDOV/Net-eBay-%{version}.tar.gz
Patch0:         Net-eBay-0.61-Do-use-non-existent-IgorBusinessRules.patch
BuildArch:      noarch
Requires:       perl(LWP::Protocol::https)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime::Precise)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::PrettyPrinter)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Format)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Dumper)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module helps user to easily execute queries against eBay's XML API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-eBay-%{version}
%patch -P0 -p1
# Skip Test::Pod::Coverage tests because they are not useful and fail,
# CPAN RT#97511
rm t/pod-coverage.t
perl -i -ne 'print $_ unless m{^t\/pod-coverage.t$}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
