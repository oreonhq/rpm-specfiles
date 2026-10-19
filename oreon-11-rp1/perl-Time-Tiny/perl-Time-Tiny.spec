%global source0_hash 00f7b231dedf170067903584c6e9b5e3ae9d11c4a66ac20ce0eb3d38b7d19282
Name:           perl-Time-Tiny
Version:        1.08
Release:        1%{?dist}
Summary:        Time object, with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Time-Tiny-%{version}.tar.gz
BuildArch:      noarch
Patch0:         Time-Tiny-1.08-Fixed-test-for-DateTime-Locale-1.33.patch
Requires:       perl(Carp)
Requires:       perl(DateTime)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Time::Tiny implements an extremely lightweight object that represents
a time, without any time data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Tiny-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
