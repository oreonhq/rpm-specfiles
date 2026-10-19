%global source0_hash 97391d8cb840162c8a4baf0eab73d8d1768982fbc19a4c2b9a569f58f93b08a0
%global metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%global FullName SVGPDF
Name: perl-%{FullName}
Summary:        SVG support for Perl PDF::API2 and similar
License: BSD-2-Clause
Version: 0.091.1
Release:        1%{?dist}
Source0:        %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}
BuildArch: noarch
Requires: perl(:VERSION) >= 5.26.0
%global __requires_exclude ^perl\\(SVGPDF::
%global __provides_exclude ^perl\\(SVGPDF::
%{?perl_default_filter}
Provides: perl(SVGPDF) = %{version}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::LoadLines)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Image::Info)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(PDF::API2)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-libs
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
