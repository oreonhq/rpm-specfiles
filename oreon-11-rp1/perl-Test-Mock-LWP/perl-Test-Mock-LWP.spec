%global source0_hash b72921b747458fd1648677158dac90d1f2360dc7bddc277639c2fa390f9780fc

Name:           perl-Test-Mock-LWP
Version:        0.08
Release:        36%{?dist}
Summary:        Easy mocking of LWP packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Mock-LWP
Source0:        https://cpan.metacpan.org/authors/id/L/LU/LUKEC/Test-Mock-LWP-%{version}.tar.gz
# Disable unused features in a build script
Patch0:         Test-Mock-LWP-0.08-Disable-autoinstalling-the-dependencies.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::MockObject) >= 1.08
# Tests:
BuildRequires:  perl(Test::More) >= 0.42
Requires:       perl(Test::MockObject) >= 1.08

# Hide private redefinitions
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((HTTP::(Request|Response)|LWP::UserAgent)\\)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::MockObject\\)$

%description
A mocking library for testing of code based around LWP.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Mock-LWP-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
