%global source0_hash 5e8e424671a0b2f1d9dff30e5f99087e7555880eb5d79a328b31f4cd4992983d
%{bcond_with perl_DynaLoader_Functions_enables_optional_test}
Name:           perl-DynaLoader-Functions
Version:        0.004
Release:        1%{?dist}
Summary:        Deconstructed dynamic C library loading
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DynaLoader-Functions
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_DynaLoader_Functions_enables_optional_test}
%endif
Requires:       perl(Carp)
Requires:       perl(DynaLoader)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(VMS::Filespec\\)
Provides:       perl(DynaLoader::Functions)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a function-based interface to dynamic loading as used
by Perl. Some details of dynamic loading are very platform-dependent, so
correct use of these functions requires the programmer to be mindful of the
space of platform variations.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::Spec)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DynaLoader-Functions-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -fr %{buildroot}%{_libexecdir}/%{name}/t/pod*
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
%{_fixperms} -c %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-DynaLoader-Functions-tests -f %{oreon_filedir}/perl-DynaLoader-Functions-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.004-8
- Prepare for Oreon 11 (RP1)
