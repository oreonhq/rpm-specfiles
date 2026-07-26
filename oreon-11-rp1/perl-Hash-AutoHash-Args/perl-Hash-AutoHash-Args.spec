%global source0_hash 0c4e499831b83e5dace2e3669e8ee4c8559861343e1349d0e20cedc95ff8b3e7

Name:           perl-Hash-AutoHash-Args
Version:        1.18
Release:        24%{?dist}
Summary:        Object-oriented processing of keyword-based argument lists
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-AutoHash-Args
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Hash-AutoHash-Args-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.2
BuildRequires:  perl(Hash::AutoHash) >= 1.17
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash) >= 1.04
# Tests:
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(File::Basename) >= 2.82
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils) >= 0.33
BuildRequires:  perl(Test::Deep) >= 0.11
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(Test::Pod::Content) >= 0.0.6
Requires:       perl(Carp) >= 1.2
Requires:       perl(Hash::AutoHash) >= 1.17
Requires:       perl(Tie::Hash) >= 1.04

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|Hash::AutoHash|Tie::Hash)\\)$

%description
This Perl class simplifies the handling of keyword argument lists. It replaces
Class::AutoClass::Args.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-AutoHash-Args-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
