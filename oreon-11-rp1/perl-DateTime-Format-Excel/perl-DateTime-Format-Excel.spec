%global source0_hash 3ca4e72ceccfd1c9290fccd17006184a87183cb34e86a0136a7853a16558b113
%global pkgname DateTime-Format-Excel
Summary:        Convert between DateTime and Excel dates
Name:		perl-DateTime-Format-Excel
Epoch:		1
Version:	0.31
Release:        44%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABURS/%{pkgname}-%{version}.tar.gz
Patch0:		perl-DateTime-Format-Excel-0.31-versioning.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Excel uses a different system for its dates than most Unix programs.
This module allows to convert between a few of the Excel raw formats
and DateTime objects, which can then be further converted via any of
the other DateTime::Format::* modules, or with DateTime's methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
sed -e 's/\r//g' Changes > Changes.new
touch -c -r Changes Changes.new
mv -f Changes.new Changes
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
