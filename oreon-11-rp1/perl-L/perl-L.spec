%global source0_hash c95602033822822392f1f812a9540af6153d8a96247dfddd1b839f7cdeef760c
Name:           perl-L
Version:        1.0.1
%global cpan_version v%{version}
Release:        1%{?dist}
Summary:        Perl extension to load module automatically in one-liner
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/L
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SONGMU/L-%{cpan_version}.tar.gz
BuildArch:      noarch
Provides:       perl(L) = %{version}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(L\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This loads perl modules automatically for use in one-liners.

The module is dangerous, so don't use this module in other perl modules,
scripts or production-ready code. This should be used only in one-liners.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n L-%{cpan_version}

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
