%global source0_hash 357fc75ba7a49cc5613c30a84898545bd330b697b8ed37be1916bbd72ac35147
Name:           perl-Class-AutoClass
Version:        1.56
Release:        1%{?dist}
Summary:        Define classes and objects for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-AutoClass
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Class-AutoClass-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp) >= 1.2
Requires:       perl(Hash::AutoHash::Args) >= 1.18
Requires:       perl(Storable) >= 2.3
Requires:       perl(warnings)
Provides:       perl-AutoClass = %{version}-%{release}
Obsoletes:      perl-AutoClass < 1.56-5
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|Hash::AutoHash::Args|Storable)\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::AutoHash::Args)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Content)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Class::AutoClass is yet another module that generates standard 'get' and 'set'
methods for Perl classes. It also handles initialization of object and class
data from parameter lists or defaults, and arranges for object creation and
initialization to occur in top-down, textbook order even in the presence of
multiple inheritance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-AutoClass-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
