%global source0_hash 4e78b7e4dd231b5571a48cd0ee1b63953f5e34790c9d020e1595a7c7d0abbe49
Name: 		perl-Cache-Simple-TimedExpiry
Version: 	0.27
Release:        51%{?dist}
Summary:        A lightweight cache with timed expiration
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Cache-Simple-TimedExpiry
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESSE/Cache-Simple-TimedExpiry-%{version}.tar.gz
BuildArch: 	noarch
Patch0:         Cache-Simple-TimedExpiry-0.27-Fix-building-on-Perl-without-dot-in-INC.patch
Requires:       perl(Data::Dumper)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  findutils
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A lightweight cache with timed expiration

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-Simple-TimedExpiry-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
