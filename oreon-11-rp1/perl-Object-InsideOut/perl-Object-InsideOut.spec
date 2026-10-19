%global source0_hash 9dfd6ca2822724347e0eb6759d00709425814703ad5c66bdb6214579868bcac4
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Object-InsideOut
Version:        4.05
Release:        1%{?dist}
Summary:        Comprehensive inside-out object support module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-InsideOut
Source0:        https://cpan.metacpan.org/modules/by-module/Object/Object-InsideOut-%{version}.tar.gz
BuildArch:      noarch
%if %{undefined perl_bootstrap}
%endif
Requires:       perl(Data::Dumper) >= 2.131
Requires:       perl(Scalar::Util) >= 1.23
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Object::InsideOut\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Scalar::Util\\)
%if %{defined perl_bootstrap}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Math::Random::MT::Auto\\)
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Random::MT::Auto)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Want)
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides comprehensive support for implementing classes using the
inside-out object model.

This module implements inside-out objects as anonymous scalar references that
are blessed into a class with the scalar containing the ID for the object
(usually a sequence number). Object data (i.e., fields) are stored within the
class's package in either arrays indexed by the object's ID, or hashes keyed
to the object's ID.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-InsideOut-%{version}

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
