%global source0_hash 1d6ae66da2767520c21fbf12c538f1007ab27445d92c8eac763653f2b8849ebf

Name:           perl-Data-Record
Version:        0.02
Release:        33%{?dist}
Summary:        "split" on steroids
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Record
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Record-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::More) >= 0.6
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)

%description
Sometimes we need data split into records and a simple split on the
input record separator ($/) or some other value fails because the values
we're splitting on may allowed in other parts of the data. Perhaps
they're quoted. Perhaps they're embedded in other data which should not
be split up.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Record-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
