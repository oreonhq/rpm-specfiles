%global source0_hash 97391d8cb840162c8a4baf0eab73d8d1768982fbc19a4c2b9a569f58f93b08a0

# -*- rpm-spec -*-

%global metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%global FullName SVGPDF

Name: perl-%{FullName}
Summary: SVG support for Perl PDF::API2 and similar
License: BSD-2-Clause
Version: 0.091.1
Release: %autorelease
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.26.0

BuildRequires: make
BuildRequires: perl(:VERSION)
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.24
BuildRequires: perl(File::LoadLines) >= 1.044
BuildRequires: perl(File::Temp)
BuildRequires: perl(Image::Info) >= 1.42
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Math::Trig)
BuildRequires: perl(Object::Pad) >= 0.78
BuildRequires: perl(PDF::API2) >= 2.043
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl-libs

# The only module of interest for the outer world is SVGPDF.
%global __requires_exclude ^perl\\(SVGPDF::
%global __provides_exclude ^perl\\(SVGPDF::
%{?perl_default_filter}
# Can't seem to get this right...
Provides: perl(SVGPDF) = %{version}

%description
This module processes SVG data and produces one or more PDF XObjects
to be placed in a PDF document.

This module is intended to be used with PDF::Builder, PDF::API2 and
other compatible perl PDF packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md
%license LICENSE.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
