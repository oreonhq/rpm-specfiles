%global source0_hash 0f024be8d409a6e614c3199f547d1fac016c43378cc8bb1f19c2e91ba8891b6a
%bcond_without perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test
Name:           perl-Dist-Zilla-Plugin-Git-Contributors
Version:        0.039
Release:        1%{?dist}
Summary:        Add contributor names from git to your distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git-Contributors
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-Contributors-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Dist::Zilla) >= 4.300039
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Git::Wrapper) >= 0.038
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Git::Wrapper\\)(| >= 0\\.035)$
%global __requires_exclude %{__requires_exclude}|^perl\\(GitSetup\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((GitSetup|My::Git::Wrapper)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Weaver::Section::Contributors)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Unicode::Collate)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Dist::Zilla plugin that extracts all names and email addresses
from git commits in your repository and adds them to the distribution
metadata under the x_contributors key.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
Requires:       perl(Dist::Zilla::Plugin::PodWeaver)
Requires:       perl(Module::Runtime::Conflicts)
Requires:       perl(Moose::Conflicts)
Requires:       perl(Pod::Weaver::Section::Contributors)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Git-Contributors-%{version}
%if !%{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
for T in t/04-podweaver-warning.t t/zzz-check-breaks.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdir=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dist-Zilla-Plugin-Git-Contributors-tests -f %{oreon_filedir}/perl-Dist-Zilla-Plugin-Git-Contributors-tests.list

%changelog

%autochangelog
