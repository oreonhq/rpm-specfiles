%global source0_hash ae1886050d9ca21223c073e2870abdc80dc30e3f55289a11c37da3820a8321ff
Name:           perl-File-Find-Rule-Perl
Version:        1.16
Release:        1%{?dist}
Summary:        Common rules for searching for Perl things
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Rule-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Find-Rule-Perl-%{version}.tar.gz
Patch0:         0001-File-Find-Rule-Perl-1.16-fedora.patch
BuildArch:      noarch
Provides:       perl(File::Find::Rule::Perl)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
Common rules for searching for Perl things.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-Find-Rule-Perl-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-12
- Prepare for Oreon 11 (RP1)
