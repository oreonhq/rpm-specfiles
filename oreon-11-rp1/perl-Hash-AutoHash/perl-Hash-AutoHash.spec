%global source0_hash c4dafb86d10666700dbdc863b221c3ff56523cb3b3cbb7d2501216fb708edf52
Name:           perl-Hash-AutoHash
Version:        1.17
Release:        24%{?dist}
Summary:        Object-oriented access to real and tied hashes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-AutoHash
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Hash-AutoHash-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp) >= 1.2
Requires:       perl(List::MoreUtils) >= 0.33
Requires:       perl(Tie::Hash) >= 1.04
Requires:       perl(Tie::ToObject) >= 0.03
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::MoreUtils|Tie::Hash|Tie::ToObject)\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Content)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Hash::MultiValue)
BuildRequires:  perl(Tie::ToObject)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is yet another Perl module that lets you access or change the elements of
a hash using methods with the same name as the element's key. It follows in
the footsteps of Hash::AsObject, Hash::Inflator, Data::OpenStruct::Deep,
Object::AutoAccessor, and probably others. The main difference between this
module and its forebears is that it supports tied hashes, in addition to
regular hashes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-AutoHash-%{version}

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
