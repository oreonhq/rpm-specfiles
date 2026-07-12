%global source0_hash cfa36da96c504331ff2026747ba47d477efe835cf6cf234ee10cb05fa9fb8ba4

 # Run release test
%if ! (0%{?rhel} && 0%{?rhel} < 8)
%bcond_without perl_Test_Assert_enables_release_test
%else
%bcond_with perl_Test_Assert_enables_release_test
%endif

# noarch, but to avoid *.list files interfering with signature test
%global debug_package %{nil}

# Store keys in a temp directory
%global gnupghome %(mktemp --directory)

Name:		perl-Test-Assert
Version:	0.0504
Release:	46%{?dist}
Summary:	Assertion methods for those who like JUnit
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Assert
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Assert-%{version}.tar.gz
# Upstream signing key, bug #1118362
Source1:	C0B10A5B.pub
Patch0:		Test-Assert-0.0504-Critic.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(constant::boolean) >= 0.02
BuildRequires:	perl(Exception::Base) >= 0.21
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol::Util) >= 0.0202
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(parent)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Unit::Lite) >= 0.11
# Release Tests
%if %{with perl_Test_Assert_enables_release_test}
BuildRequires:	patch
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Test::CheckChanges)
BuildRequires:	perl(Test::Distribution)
BuildRequires:	perl(Test::Kwalitee)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Signature)
BuildRequires:	perl(Test::Spelling), hunspell-en
%endif
# Dependencies
# (none)

Provides:       perl(Exception::Assertion)
Provides:       perl(Test::Assert)
%description
This class provides a set of assertion methods useful for writing tests.
The API is based on JUnit4 and Test::Unit and the methods die on failure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Assert-%{version}

# Drop exec bits and avoid doc-file dependencies
chmod -c -x eg/*

# Import upstream's GPG key so we don't need to fetch it from a keyserver
# when running the signature test
export GNUPGHOME=%{gnupghome}
gpg2 --import %{SOURCE1}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
# === MAIN TEST SUITE === #

./Build test

# ===  RELEASE TESTS  === #
%if %{with perl_Test_Assert_enables_release_test}

export GNUPGHOME=%{gnupghome}
RELEASE_TESTS="$(echo xt/*.t)"

# Don't run the copyright test as it will fail after the year of module release
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/copyright.t||')"

# Don't run the spelling test yet as we need to add extra stopwords
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/pod_spell.t||')"

# Don't run the perlcritic test yet as we need to patch the code
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/perlcritic.t||')"

# Signature test would fail on recent distros due to presence of MYMETA.*
[ -f MYMETA.yml ] && mv MYMETA.yml ..
[ -f MYMETA.json ] && mv MYMETA.json ..

RELEASE_TESTING=1 ./Build test --test_files "$RELEASE_TESTS"

# Put any MYMETA.* files back where they were
[ -f ../MYMETA.yml ] && mv ../MYMETA.yml .
[ -f ../MYMETA.json ] && mv ../MYMETA.json .

# Patch the code to tidy it and turn off one check before running the perlcritic test
patch -p0 < %{P:0}
./Build test --test_files xt/perlcritic.t
patch -p0 -R < %{P:0}

# Fix the POD Spell test and run it
mv xt/pod_spellrc xt/pod_spellrc.orig
(
	cat xt/pod_spellrc.orig
	echo "'fail'"
	echo "JUnit4"
	echo "value1"
	echo "value2"
) > xt/pod_spellrc
./Build test --test_files xt/pod_spell.t
mv xt/pod_spellrc.orig xt/pod_spellrc

%endif

%clean
rm -rf %{buildroot} %{gnupghome}

%files
%license LICENSE
%doc Changes README eg/
%{perl_vendorlib}/Exception/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Exception::Assertion.3*
%{_mandir}/man3/Test::Assert.3*

%changelog
%autochangelog
