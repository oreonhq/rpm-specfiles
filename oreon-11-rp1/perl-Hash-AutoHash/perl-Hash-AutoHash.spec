%global source0_hash c4dafb86d10666700dbdc863b221c3ff56523cb3b3cbb7d2501216fb708edf52

Name:           perl-Hash-AutoHash
Version:        1.17
Release:        24%{?dist}
Summary:        Object-oriented access to real and tied hashes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-AutoHash
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NATG/Hash-AutoHash-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp) >= 1.2
BuildRequires:  perl(List::MoreUtils) >= 0.33
BuildRequires:  perl(Scalar::Util) >= 1.23
BuildRequires:  perl(Tie::Hash) >= 1.04
BuildRequires:  perl(Tie::ToObject) >= 0.03
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(lib)
BuildRequires:  perl(Storable) >= 2.3
BuildRequires:  perl(Test::Deep) >= 0.11
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(Test::Pod::Content) >= 0.0.6
BuildRequires:  perl(Tie::Hash::MultiValue) >= 1.02
Requires:       perl(Carp) >= 1.2
Requires:       perl(List::MoreUtils) >= 0.33
Requires:       perl(Tie::Hash) >= 1.04
Requires:       perl(Tie::ToObject) >= 0.03

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::MoreUtils|Tie::Hash|Tie::ToObject)\\)$

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

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
