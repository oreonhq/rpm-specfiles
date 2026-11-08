# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0fff1f02c61b7098a6d2eb9698a052cf00b87becf2705d2d1f0d395f8d87a7e3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           perl-Oreon-VSP
Version:        0.001
Release:        1%{?dist}
Summary:        Perl version normalization for RPM
License:        GPL-3.0-or-later
URL:            https://ppisar.fedorapeople.org/Fedora-VSP/
Source0:        https://ppisar.fedorapeople.org/Fedora-VSP/Fedora-VSP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
%if %{defined perl_bootstrap}
BuildRequires:  perl-macros
%else
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
BuildRequires:  oreon-rpm-macros
Provides:       perl(Oreon::VSP) = %{version}
%if %{defined perl_bootstrap}
Requires:       perl(strict)
Requires:       perl(warnings)
%endif

%description
This module provides functions for normalizing Perl version strings for
Oreon Package (RPM) based Linux distributions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256

%setup -q -n Fedora-VSP-%{version}
mkdir -p lib/Oreon
mv lib/Fedora/VSP.pm lib/Oreon/VSP.pm
rmdir lib/Fedora
sed -i \
    -e 's|Fedora::VSP|Oreon::VSP|g' \
    -e 's|lib/Fedora/VSP.pm|lib/Oreon/VSP.pm|g' \
    lib/Oreon/VSP.pm Makefile.PL MANIFEST t/version.t
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

