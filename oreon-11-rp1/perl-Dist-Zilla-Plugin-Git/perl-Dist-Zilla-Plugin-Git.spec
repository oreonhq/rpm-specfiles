%global source0_hash 8393f591673f1c0ee765c8a42cb8ddca86a01e8e109e87dc4b069b3184b42420
%bcond_without perl_Dist_Zilla_Plugin_Git_enables_optional_test
Name:           perl-Dist-Zilla-Plugin-Git
Version:        2.052
Release:        2%{?dist}
Summary:        Update your git repository after release
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
%endif
Requires:       perl(DateTime)
Requires:       perl(Dist::Zilla::Plugin::GatherDir) >= 4.200016
Requires:       perl(Dist::Zilla::Role::AfterBuild)
Requires:       perl(Dist::Zilla::Role::AfterMint)
Requires:       perl(Dist::Zilla::Role::AfterRelease)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::GitConfig)
Requires:       perl(Dist::Zilla::Role::PluginBundle)
Requires:       perl(Dist::Zilla::Role::VersionProvider)
Requires:       perl(Version::Next)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.8\\.|^perl\\(Dist::Zilla\\) >= 2\\.|perl\\(Git::Wrapper\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Util\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Dist::Zilla::Plugin::MyTestArchiver|Git::Wrapper|Util)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  git-core
BuildRequires:  gnupg
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Plugin::Config::Git)
BuildRequires:  perl(Dist::Zilla::Plugin::GatherDir)
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
BuildRequires:  perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::GitConfig)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(Dist::Zilla::Tester)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatchouli)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Version::Next)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This set of plugins for Dist::Zilla can do interesting things for module
authors using Git (http://git-scm.com/) to track their work.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Dist::Zilla::Role::Releaser)
Requires:       perl(Git::Wrapper) >= 0.021
%if %{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
Requires:       gnupg
Requires:       perl(Dist::Zilla::Plugin::Config::Git)
Requires:       perl(Module::Runtime::Conflicts)
Requires:       perl(Moose::Conflicts)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Git-%{version}
%if !%{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
rm t/push-gitconfig.t
perl -i -ne 'print $_ unless m{\A\Qt/push-gitconfig.t\E\b}' MANIFEST
%endif
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR="$(mktemp -d)"
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
unset V
exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset V
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dist-Zilla-Plugin-Git-tests -f %{oreon_filedir}/perl-Dist-Zilla-Plugin-Git-tests.list

%changelog

%autochangelog
