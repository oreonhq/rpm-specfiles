%global source0_hash 2077c9a420e3c0659b61298bff4ede1269120cf690bfeb35f49f6e6c6be8ee43
Name:           perl-DateTime-Format-DateManip
Version:        0.04
Release:        1%{?dist}
Summary:        Convert Date::Manip to DateTime and vice versa
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-DateManip
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBENNETT/dt-fmt-datemanip/DateTime-Format-DateManip-%{version}.tar.gz
Patch0:         DateTime-Format-DateManip-01conversion.patch
Patch1:         DateTime-Format-DateManip-0.04-Set-system-time-zone-in-test.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DateTime::Format::DateManip is a class that knows how to convert between
Date::Manip dates and durations and DateTime and DateTime::Duration
objects. Recurrences are note yet supported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-DateManip-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
