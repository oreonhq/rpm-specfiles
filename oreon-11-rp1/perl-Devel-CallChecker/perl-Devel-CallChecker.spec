%global source0_hash 66de557a97a88609f82a0aad9ad3597d1d3333b68e732c9100839e06914dcbe4
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Devel_CallChecker_enables_optional_test
%else
%bcond_with perl_Devel_CallChecker_enables_optional_test
%endif
Name:           perl-Devel-CallChecker
Version:        0.010
Release:        1%{?dist}
Summary:        Custom op checking attached to subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-CallChecker
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHINGO/Devel-CallChecker-%{version}.tar.gz
%if %{with perl_Devel_CallChecker_enables_optional_test}
%endif
Requires:       perl(DynaLoader)
Requires:       perl(DynaLoader::Functions) >= 0.001
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((t::LoadXS|t::WriteHeader)\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Devel::CallChecker)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(DynaLoader::Functions)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module makes some new features of the Perl 5.14.0 C API available to
XS modules running on older versions of Perl. The features are centered
around the function cv_set_call_checker, which allows XS code to attach a
magical annotation to a Perl subroutine, resulting in resolvable calls to
that subroutine being mutated at compile time by arbitrary C code. This
module makes cv_set_call_checker and several supporting functions
available. (It is possible to achieve the effect of cv_set_call_checker
from XS code on much earlier Perl versions, but it is painful to achieve
without the centralized facility.)

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-CallChecker-%{version}
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
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Devel-CallChecker-tests -f %{oreon_filedir}/perl-Devel-CallChecker-tests.list

%changelog

%autochangelog
