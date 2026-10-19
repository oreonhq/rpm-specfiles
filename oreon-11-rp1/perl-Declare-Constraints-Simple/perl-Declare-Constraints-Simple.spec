%global source0_hash db77ae8d8e0afb76e6f1bfa9ef3a316718907e827ff181c8c0ad6a9f3dd80f36
Name:		perl-Declare-Constraints-Simple
Version:	0.03
Release:        1%{?dist}
Summary:        Declarative Validation of Data Structures
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Declare-Constraints-Simple
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHAYLON/Declare-Constraints-Simple-%{version}.tar.gz
Patch0:		Declare-Constraints-Simple-0.03-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:	noarch
%global __requires_exclude ^perl\\(Declare::Constraints::Simple-Library\\)
Provides:       perl(Declare::Constraints::Simple)
Provides:       perl(Declare::Constraints::Simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Declare-Constraints-Simple-%{version}

# Fix install when no '.' in @INC (CPAN RT#121709)
%patch -P 0 -p1

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
