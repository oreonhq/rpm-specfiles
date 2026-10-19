%global source0_hash 75ff1c8c98e8c0537692645cd62d2a4c48ab097b1d4a5ea42a25305098d7fd39
Name:		perl-Module-Find
Version:	0.17
Release:        3%{?dist}
Summary:        Find and use installed modules in a (sub)category
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Module-Find
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Find-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Exporter)
Provides:       perl(Module::Find)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plug-in modules. You can differentiate
between looking in the category itself or in all subcategories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Find-%{version}

# Generate Changes file from POD
perldoc -t Find.pm |
	perl -n -e 'if (/^HISTORY/ ... !/^[[:space:]]/) { print if /^[[:space:]]/ }' > Changes
touch --reference=Find.pm Changes

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

%autochangelog
