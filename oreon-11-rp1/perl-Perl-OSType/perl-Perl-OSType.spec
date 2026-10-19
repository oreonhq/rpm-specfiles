%global source0_hash e7ed4994b5d547cb23aadb84dc6044c5eb085d5a67a6c5624f42542edd3403b2
%bcond_without perl_Perl_OSType_enables_optional_test
Name:		perl-Perl-OSType
Version:	1.010
Release:        1%{?dist}
Summary:        Map Perl operating system names to generic types
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-OSType
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-OSType-%{version}.tar.gz
Patch2:		Perl-OSType-1.010-stopwords.patch
BuildArch:	noarch
Provides:       perl(Perl::OSType)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Modules that provide OS-specific behaviors often need to know if the current
operating system matches a more generic type of operating systems. For example,
'linux' is a type of 'Unix' operating system and so is 'freebsd'.

This module provides a mapping between an operating system name as given by $^O
and a more generic type. The initial version is based on the OS type mappings
provided in Module::Build and ExtUtils::CBuilder (thus, Microsoft operating
systems are given the type 'Windows' rather than 'Win32').

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-OSType-%{version}

# More stopwords for the spell checker
%patch -P 2

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.010-522
- Prepare for Oreon 11 (RP1)
