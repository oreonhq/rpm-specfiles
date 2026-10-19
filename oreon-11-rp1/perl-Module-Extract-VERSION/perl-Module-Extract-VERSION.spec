%global source0_hash 172b345e3b65b19697a0ac513fe6ac1f20ef8fe5ed3d88cd425c2b4febc45df5
Name:		perl-Module-Extract-VERSION
Version:	1.119
Release:        3%{?dist}
Summary:        Extract a module version without running code
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-VERSION
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-VERSION-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Safe)
Requires:	perl(version) >= 0.86
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::Manifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module lets you pull out of module source code the version number for the
module. It assumes that there is only one $VERSION in the file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Extract-VERSION-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
