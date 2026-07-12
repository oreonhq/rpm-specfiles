%global source0_hash 51c2204450538c4887bb0371a0abe935ddda3483aba982f2359179682da7f2bb

Name:           perl-Module-Install-TestBase
Version:        0.86
Release:        37%{?dist}
Summary:        Module::Install support for Test::Base
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-TestBase
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-TestBase-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Filter::Util::Call not used at tests
# The Module::Install::Base version constrain is phony, bug #1134351,
# <https://github.com/ingydotnet/module-install-testbase-pm/issues/2>
BuildRequires:  perl(Module::Install::Base)
# Spiffy not used at tests
# Test::Base 0.86 not used at tests
# Test::Base::Filter not used at tests
# Test::Builder not used at tests
# Test::Builder::Module not used at tests
# Test::More not used at tests
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::More)
# Test::Pod not used
Requires:   perl(Filter::Util::Call)
Requires:   perl(Spiffy)
Requires:   perl(Test::Base) >= 0.86
Requires:   perl(Test::Base::Filter)
Requires:   perl(Test::Builder)
Requires:   perl(Test::Builder::Module)
Requires:   perl(Test::More)
# Module::Install::TestBase splitted from Test-Base in 0.85
Conflicts:  perl-Test-Base < 0.85

Provides:       perl(Module::Install::TestBase)
%description
This Perl module adds the use_test_base directive to Module::Install. Now you
can get full Test-Base support for you module with no external dependency on
Test::Base.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-TestBase-%{version}
# Remove release tests
rm t/release-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/release-pod-syntax.t}' MANIFEST

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
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib/Module/Install
# t/000-compile-modules.t inspect ./lib, but rpmbuild follows symlinks
# and that would place identical Provides to main and tests subpackage.
# Fortunatelly the test only needs a file name. Hence create an empty file.
# Bug #2063919.
touch %{buildroot}%{_libexecdir}/%{name}/lib/Module/Install/TestBase.pm
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
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/Module
%dir %{perl_vendorlib}/Module/Install
%{perl_vendorlib}/Module/Install/TestBase.*
%{_mandir}/man3/Module::Install::TestBase.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
