%global source0_hash 2b3e871715fdfb108591fb1cfa38319d3d046e4c117bcb58ead312afddfbd158
Name:           perl-Parse-ErrorString-Perl
Version:        0.27
Release:        1%{?dist}
Summary:        Module for parsing error messages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-ErrorString-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Parse-ErrorString-Perl-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl-diagnostics
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::POM\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-diagnostics
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Parse error messages from the perl interpreter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-ErrorString-Perl-%{version}

# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\// d' MANIFEST

%build

perl Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
