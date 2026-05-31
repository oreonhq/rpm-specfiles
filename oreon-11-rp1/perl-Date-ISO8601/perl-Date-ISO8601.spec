%global source0_hash 84bef53cc808bd11830fbb434c9836c3dc4b24a58db878f5073db198fb9a586c

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Date_ISO8601_enables_optional_test
%else
%bcond_with perl_Date_ISO8601_enables_optional_test
%endif

Name:           perl-Date-ISO8601
Version:        0.005
Release:        24%{?dist}
Summary:        Three ISO 8601 numerical calendars
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-ISO8601
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-ISO8601-%{version}.tar.gz



BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
%if %{with perl_Date_ISO8601_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
# Dependencies
Requires:       perl(Exporter)

%description
The international standard ISO 8601 "Data elements and interchange formats
- Information interchange - Representation of dates and times" defines
three distinct calendars by which days can be labeled. It also defines
textual formats for the representation of dates in these calendars. This
module provides functions to convert dates between these three calendars
and Chronological Julian Day Numbers, which is a suitable format to do
arithmetic with. It also supplies functions that describe the shape of
these calendars, to assist in calendrical calculations. It also supplies
functions to represent dates textually in the ISO 8601 formats. ISO 8601
also covers time of day and time periods, but this module does nothing
relating to those parts of the standard; this is only about labeling days.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Date-ISO8601-%{version}

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
%{perl_vendorlib}/Date/
%{_mandir}/man3/Date::ISO8601.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.005-24
- Prepare for Oreon 11 (RP1)
