%global source0_hash 357fc75ba7a49cc5613c30a84898545bd330b697b8ed37be1916bbd72ac35147

Name:           perl-Class-AutoClass
Version:        1.56
Release:        21%{?dist}
Summary:        Define classes and objects for Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-AutoClass
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Class-AutoClass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.2
BuildRequires:  perl(Hash::AutoHash::Args) >= 1.18
BuildRequires:  perl(Storable) >= 2.3
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(IO::Scalar) >= 2.11
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util) >= 1.23
BuildRequires:  perl(Test::Deep) >= 0.11
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Content) >= 0.0.6
Requires:       perl(Carp) >= 1.2
Requires:       perl(Hash::AutoHash::Args) >= 1.18
Requires:       perl(Storable) >= 2.3
Requires:       perl(warnings)
# Renamed from perl-AutoClass-1.56-4.fc30
Provides:       perl-AutoClass = %{version}-%{release}
Obsoletes:      perl-AutoClass < 1.56-5

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|Hash::AutoHash::Args|Storable)\\)$

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

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
