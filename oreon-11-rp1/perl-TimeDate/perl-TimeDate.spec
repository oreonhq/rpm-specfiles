# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash baddd0306ae2e86e9ec28d3de5439e514643e80b3735e43bd0fbb426d73304de
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?rhel} || 0%{?oreon}
%bcond_with perl_TimeDate_enables_optional_test
%else
%bcond_without perl_TimeDate_enables_optional_test
%endif

Name:           perl-TimeDate
Version:        2.35
Epoch:          1
Release:        1%{?dist}
Summary:        A Perl module for time and date manipulation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TimeDate
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/TimeDate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(utf8)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
%if %{with perl_TimeDate_enables_optional_test}
BuildRequires:  perl(Pod::Checker)
%endif

%description
This module includes a number of smaller modules suited for
manipulation of time and date strings with Perl. In particular, the
Date::Format and Date::Parse modules can display and read times and
dates in various formats, providing a more reliable interface to
textual representations of points in time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256
%setup -q -n TimeDate-%{version}
%if %{without perl_TimeDate_enables_optional_test}
    rm t/pod-valid.t
    perl -i -ne 'print $_ unless m{\At/pod-valid\.t\b}' MANIFEST
%endif
chmod -x lib/Date/Language/{Russian_cp1251,Russian_koi8r,Turkish}.pm

for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_TimeDate_enables_optional_test}
    rm %{buildroot}%{_libexecdir}/%{name}/t/pod-valid.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files 
%doc README Changes SECURITY.md
%license LICENSE
%dir %{perl_vendorlib}/Date/
%{perl_vendorlib}/Date/Format*
%{perl_vendorlib}/Date/Language*
%{perl_vendorlib}/Date/Parse.pm
%dir %{perl_vendorlib}/Time/
%{perl_vendorlib}/Time/Zone.pm
%{perl_vendorlib}/TimeDate.pm
%{_mandir}/man3/Date::Format*.3*
%{_mandir}/man3/Date::Language*.3*
%{_mandir}/man3/Date::Parse*.3*
%{_mandir}/man3/Time::Zone*.3*
%{_mandir}/man3/TimeDate*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
