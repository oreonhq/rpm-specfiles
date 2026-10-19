%global source0_hash 1d6ae66da2767520c21fbf12c538f1007ab27445d92c8eac763653f2b8849ebf
Name:           perl-Data-Record
Version:        0.02
Release:        1%{?dist}
Summary:        "split" on steroids
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Record
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Record-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
