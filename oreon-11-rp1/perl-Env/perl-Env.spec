%global base_version 1.04
Name:           perl-Env
Version:        1.06
Release:        521%{?dist}
Summary:        Perl module that imports environment variables as scalars or arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Env-%{base_version}.tar.gz
BuildArch:      noarch
# Unbundled from perl 5.34.0
Patch0:         Env-1.04-Upgrade-to-1.05.patch
# Unbundled from perl 5.37.11
Patch1:         Env-1.05-Upgrade-to-1.06.patch
# oreon url source checksums begin
%global source0_sha256 d94a3d412df246afdc31a2199cbd8ae915167a3f4684f7b7014ce1200251ebb0
%global source0_file Env-1.04.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Tie::Array)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
Perl maintains environment variables in a special hash named %%ENV. For when
this access method is inconvenient, the Perl module Env allows environment
variables to be treated as scalar or array variables.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Env-1.04.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d94a3d412df246afdc31a2199cbd8ae915167a3f4684f7b7014ce1200251ebb0" || { echo "oreon: Source0 SHA256 mismatch for Env-1.04.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Env-%{base_version}
%patch -P0 -p1
%patch -P1 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Env*
%{_mandir}/man3/Env*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.06-521
- Prepare for Oreon 11 (RP1)
