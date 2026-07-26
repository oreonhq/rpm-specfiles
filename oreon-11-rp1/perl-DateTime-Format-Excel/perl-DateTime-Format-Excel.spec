%global source0_hash 3ca4e72ceccfd1c9290fccd17006184a87183cb34e86a0136a7853a16558b113

%global pkgname DateTime-Format-Excel

Summary:	Convert between DateTime and Excel dates
Name:		perl-DateTime-Format-Excel
Epoch:		1
Version:	0.31
Release:	44%{?dist}
# lib/DateTime/Format/Excel.pm -> GPL+ or Artistic
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/%{pkgname}
Source:		https://cpan.metacpan.org/authors/id/A/AB/ABURS/%{pkgname}-%{version}.tar.gz
Patch0:		perl-DateTime-Format-Excel-0.31-versioning.patch
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Run-time
BuildRequires:	perl(Carp)
BuildRequires:	perl(DateTime) >= 0.18
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Tests
BuildRequires:	perl(Test::More) >= 0.47
# Optional tests
BuildRequires:	perl(Test::Pod) >= 0.95
BuildArch:	noarch

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

# Remove any non-unix line breaks
sed -e 's/\r//g' Changes > Changes.new
touch -c -r Changes Changes.new
mv -f Changes.new Changes

%check
make test

%files
%license Artistic COPYING
%doc Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
