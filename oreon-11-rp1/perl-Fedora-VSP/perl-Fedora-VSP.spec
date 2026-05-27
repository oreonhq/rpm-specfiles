%global source0_hash 0fff1f02c61b7098a6d2eb9698a052cf00b87becf2705d2d1f0d395f8d87a7e3

Name:           perl-Fedora-VSP
Version:        0.001
Release:        38%{?dist}
Summary:        Perl version normalization for RPM
License:        GPL-3.0-or-later
URL:            https://ppisar.fedorapeople.org/Fedora-VSP/
Source0:        https://ppisar.fedorapeople.org/Fedora-VSP/Fedora-VSP-0.001.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
%if %{defined perl_bootstrap}
BuildRequires:  perl-macros
%else
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
%if %{defined perl_bootstrap}
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
Requires:       perl(strict)
Requires:       perl(warnings)
Provides:       perl(Fedora::VSP) = %{version}
%endif

%description
This module provides functions for normalizing Perl version strings for
Red Hat Package (RPM) based Linux distributions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Fedora-VSP-%{version}
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.001-38
- Prepare for Oreon 11 (RP1)
