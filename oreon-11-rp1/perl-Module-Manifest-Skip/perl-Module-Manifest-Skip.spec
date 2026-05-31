%global source0_hash 2c5fc7860c44f7d3a049b624b248112b146761775d92e5e431eaa60e880513be

Name:           perl-Module-Manifest-Skip
Version:        0.23
Release:        35%{?dist}
Summary:        MANIFEST.SKIP Manangement for Modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Manifest-Skip
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Manifest-Skip-%{version}.tar.gz
# Adapt to changes in Moo-2.004000, bug #1826148,
# <https://github.com/ingydotnet/module-manifest-skip-pm/issues/7>
Patch0:         Module-Manifest-Skip-0.23-Adapt-to-changes-in-Moo-2.004000.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moo) >= 0.091013
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(File::ShareDir)
Requires:       perl(File::Spec)
Requires:       perl(Moo) >= 0.091013
Requires:       perl(warnings)

# Remove under-speficied dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$
# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestModuleManifestSkip\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestModuleManifestSkip\\)$

%description
CPAN module authors use a MANIFEST.SKIP file to exclude certain well known
files from getting put into a generated MANIFEST file, which would cause them
to go into the final distribution package.

The packaging tools try to automatically skip things for you, but if you add
one of your own entries, you have to add all the common ones yourself.  This
module attempts to make all of this boring process as simple and reliable as
possible.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Manifest-Skip-%{version}
%patch -P0 -p1
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
# share dir is for testing
cp -a share %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/release-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some test files writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23-35
- Prepare for Oreon 11 (RP1)
