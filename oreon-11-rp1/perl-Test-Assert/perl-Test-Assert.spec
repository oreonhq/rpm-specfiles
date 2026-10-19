%global source0_hash cfa36da96c504331ff2026747ba47d477efe835cf6cf234ee10cb05fa9fb8ba4
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Test_Assert_enables_release_test
%global debug_package %{nil}
%global gnupghome %(mktemp --directory)
Name:		perl-Test-Assert
Version:	0.0504
Release:        1%{?dist}
Summary:        Assertion methods for those who like JUnit
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Assert
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Assert-%{version}.tar.gz
Source1:	C0B10A5B.pub
Patch0:		Test-Assert-0.0504-Critic.patch
BuildArch:	noarch
%if %{with perl_Test_Assert_enables_release_test}
%endif
Provides:       perl(Exception::Assertion)
Provides:       perl(Test::Assert)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exception::Base)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Symbol::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Unit::Lite)
BuildRequires:  perl(constant)
BuildRequires:  perl(constant::boolean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%if %{with perl_Test_Assert_enables_release_test}
export GNUPGHOME=%{gnupghome}
RELEASE_TESTS="$(echo xt/*.t)"
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/copyright.t||')"
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/pod_spell.t||')"
RELEASE_TESTS="$(echo $RELEASE_TESTS | sed 's|xt/perlcritic.t||')"
[ -f MYMETA.yml ] && mv MYMETA.yml ..
[ -f MYMETA.json ] && mv MYMETA.json ..
RELEASE_TESTING=1 ./Build test --test_files "$RELEASE_TESTS"
[ -f ../MYMETA.yml ] && mv ../MYMETA.yml .
[ -f ../MYMETA.json ] && mv ../MYMETA.json .
patch -p0 < %{P:0}
./Build test --test_files xt/perlcritic.t
patch -p0 -R < %{P:0}
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
