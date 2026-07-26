%global source0_hash d30ba7f2ce512f5820d6dd51c6e2d02bbc1bf7d3ee07a0b7282b1cef9a2e72cd

# Execute extra test
%bcond_with perl_DateTime_Format_Flexible_enables_extra_test

Name:       perl-DateTime-Format-Flexible
Version:    0.37
Release:    4%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Flexibly parse strings and turn them into DateTime objects
Source:     https://cpan.metacpan.org/authors/id/T/TH/THINC/DateTime-Format-Flexible-%{version}.tar.gz
Url:        https://metacpan.org/release/DateTime-Format-Flexible
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.74
BuildRequires:  perl(DateTime::Infinite)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
# Extra tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(t::lib::helper\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(t::lib::helper\\)

%description
If you have ever had to use a program that made you type in the date a certain
way and thought "Why can't the computer just figure out what date I wanted?",
this module is for you.

DateTime::Format::Flexible attempts to take any string you give it and parse
it into a DateTime object.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n DateTime-Format-Flexible-%{version}
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{002_pod,003_podcoverage}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset DFF_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DFF_DEBUG
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
export TEST_POD=1
%else
export TEST_POD=0
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes example/ README TODO
%dir %{perl_vendorlib}/DateTime
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorlib}/DateTime/Format/Flexible
%{perl_vendorlib}/DateTime/Format/Flexible.pm
%{_mandir}/man3/DateTime::Format::Flexible.*
%{_mandir}/man3/DateTime::Format::Flexible::*.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
