%global source0_hash c79030436a84827ea68173b13c36ac951a5170a54f1dd8f523506b674f2b9e0e

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_DateTime_TimeZone_Tzfile_enables_optional_test
%else
%bcond_with perl_DateTime_TimeZone_Tzfile_enables_optional_test
%endif

Name:           perl-DateTime-TimeZone-Tzfile
Version:        0.011
Release:        25%{?dist}
Summary:        Tzfile (zoneinfo) timezone files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-TimeZone-Tzfile
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-Tzfile-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(DateTime::TimeZone::SystemV) >= 0.009
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File) >= 1.13
BuildRequires:  perl(IO::Handle) >= 1.08
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
%if %{with perl_DateTime_TimeZone_Tzfile_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
# Dependencies
Requires:       perl(DateTime::TimeZone::SystemV) >= 0.009

Provides:       perl(DateTime::TimeZone::Tzfile)
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

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::TimeZone::Tzfile.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.011-25
- Prepare for Oreon 11 (RP1)
