%global source0_hash 827bce3c45c2777331cba201e31801945aeeb18c59aed3d94c2b2adb209d954a
%bcond_with perl_DateTime_TimeZone_SystemV_enables_optional_test
Name:           perl-DateTime-TimeZone-SystemV
Version:        0.010
Release:        1%{?dist}
Summary:        System V and POSIX timezone strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-TimeZone-SystemV
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-SystemV-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DateTime_TimeZone_SystemV_enables_optional_test}
%endif
Provides:       perl(DateTime::TimeZone::SystemV)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
An instance of this class represents a timezone that was specified by means
of a System V timezone recipe or the POSIX extended form of the same
syntax. These can express a plain offset from Universal Time, or a system
of two offsets (standard and daylight saving time) switching on a yearly
cycle according to certain types of rule.

This class implements the DateTime::TimeZone interface, so that its instances
can be used with DateTime objects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-TimeZone-SystemV-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.010-25
- Prepare for Oreon 11 (RP1)
