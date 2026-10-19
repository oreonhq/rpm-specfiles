%global source0_hash 0c4e499831b83e5dace2e3669e8ee4c8559861343e1349d0e20cedc95ff8b3e7
Name:           perl-Hash-AutoHash-Args
Version:        1.18
Release:        1%{?dist}
Summary:        Object-oriented processing of keyword-based argument lists
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-AutoHash-Args
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Hash-AutoHash-Args-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp) >= 1.2
Requires:       perl(Hash::AutoHash) >= 1.17
Requires:       perl(Tie::Hash) >= 1.04
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|Hash::AutoHash|Tie::Hash)\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::AutoHash)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Content)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
