%global source0_hash c79030436a84827ea68173b13c36ac951a5170a54f1dd8f523506b674f2b9e0e
%bcond_with perl_DateTime_TimeZone_Tzfile_enables_optional_test
Name:           perl-DateTime-TimeZone-Tzfile
Version:        0.011
Release:        1%{?dist}
Summary:        Tzfile (zoneinfo) timezone files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-TimeZone-Tzfile
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-Tzfile-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DateTime_TimeZone_Tzfile_enables_optional_test}
%endif
Requires:       perl(DateTime::TimeZone::SystemV) >= 0.009
Provides:       perl(DateTime::TimeZone::Tzfile)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(DateTime::TimeZone::SystemV)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
An instance of this class represents a timezone that was encoded in a file
in the tzfile(5) format. These can express arbitrary patterns of offsets
from Universal Time, changing over time. Offsets and change times are
limited to a resolution of one second.

This class implements the DateTime::TimeZone interface, so that its instances
can be used with DateTime objects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-TimeZone-Tzfile-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.011-25
- Prepare for Oreon 11 (RP1)
