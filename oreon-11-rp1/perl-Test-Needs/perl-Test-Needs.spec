# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 923ffdc78fcba96609753e4bae26b0ba0186893de4a63cd5236e012c7c90e208
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Test-Needs
Version:        0.002010
Release:        1%{?dist}
Summary:        Skip tests when modules not available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Needs
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Test-Needs-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Event)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestAPI\\)$

%description
Skip test scripts if modules are not available. The requested modules will
be loaded, and optionally have their versions checked. If the module is
missing, the test script will be skipped. Modules that are found but fail
to compile will exit with an error rather than skip.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256
%setup -q -n Test-Needs-%{version}
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
