%global source0_hash 491ea1fb977de1c440d0a0c085f5148c11bbc39b4f5bc68ae5a5727399b07e08
Name:           perl-Image-Xbm
Version:        1.11
Release:        4%{?dist}
Summary:        Load, create, manipulate and save xbm image files in Perl
License:        LGPL-2.0-only AND GPL-1.0-only AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Image-Xbm
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Xbm-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Image::Xbm)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Image::Base)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
This class module provides basic load, manipulate and save functionality for
the xbm file format.  It inherits from Image::Base which provides additional
manipulation functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Image-Xbm-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
