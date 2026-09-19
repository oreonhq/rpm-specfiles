%global source0_hash 3bbe6fddc09e27f94951f49641d5cfa6c1d1c60f688f0aa7fedbe33f4a01e65d

# Add a support for Date::Manip time objects
%bcond_without perl_DateTimeX_Easy_enables_Date_Manip
# Add a support for ICal time format
%bcond_without perl_DateTimeX_Easy_enables_ical

Name:       perl-DateTimeX-Easy
Version:    0.092
Release:    4%{?dist}
# lib/DateTimeX/Easy.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                          GPL-1.0-or-later OR Artistic-1.0-Perl
# README:                           GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Parse a date/time string using the best method available
Source:     https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/DateTimeX-Easy-%{version}.tar.gz
Url:        https://metacpan.org/release/DateTimeX-Easy
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Flexible)
BuildRequires:  perl(DateTime::Format::Natural)
# 2.63 minimal version in META is superfluous
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(vars)
# YAML not used, CPAN RT#144022
# Optional run-time:
# DateTime::Format::DateManip has been made optional due to instability
%if %{with perl_DateTimeX_Easy_enables_ical}
BuildRequires:  perl(DateTime::Format::ICal)
%endif
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
%if %{with perl_DateTimeX_Easy_enables_Date_Manip}
Suggests:       perl(DateTime::Format::DateManip)
%endif
%if %{with perl_DateTimeX_Easy_enables_ical}
Recommends:     perl(DateTime::Format::ICal)
%endif

# Do not export dependency on private module
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTimeX::Easy::DateParse\\)

%description
DateTimeX::Easy makes DateTime object creation quick and easy. It uses a
variety of DateTime::Format packages to do the bulk of the parsing, with
some custom tweaks to smooth out the rough edges (mainly concerning
timezone detection and selection).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n DateTimeX-Easy-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README
%dir %{perl_vendorlib}/DateTimeX
%{perl_vendorlib}/DateTimeX/Easy
%{perl_vendorlib}/DateTimeX/Easy.pm
%{_mandir}/man3/DateTimeX::Easy.*
%{_mandir}/man3/DateTimeX::Easy::*.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
