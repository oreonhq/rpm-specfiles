%global source0_hash 6bac0e659f71e239d3dd09b2d370f9dbea301fc6e76f3b64552da5c3978ede4f
Name:           perl-Module-Manifest-Skip
Version:        0.24
Release:        1%{?dist}
Summary:        MANIFEST.SKIP Manangement for Modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Manifest-Skip
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Manifest-Skip-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::ShareDir)
Requires:       perl(File::Spec)
Requires:       perl(Moo) >= 0.091013
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestModuleManifestSkip\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestModuleManifestSkip\\)$
Provides:       perl(Module::Manifest::Skip)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp -a share %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/release-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Manifest-Skip-tests -f %{oreon_filedir}/perl-Module-Manifest-Skip-tests.list

%changelog

%autochangelog
