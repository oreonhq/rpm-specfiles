%global source0_hash 27ba13f0d9512929166bbd8c9ef95d90d630fc80f0c9a1b7458891055e9282a4
Name:           perl-Class-Singleton
Version:        1.6
Release:        1%{?dist}
Summary:        Implementation of a "Singleton" class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Singleton
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Singleton-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Class::Singleton)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is the Class::Singleton module. A Singleton describes an object class
that can have only one instance in any system. An example of a Singleton
might be a print spooler or system registry. This module implements a
Singleton class from which other classes can be derived. By itself, the
Class::Singleton module does very little other than manage the
instantiation of a single object. In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Singleton-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6-15
- Prepare for Oreon 11 (RP1)
