%global source0_hash 27f08742d8e024de2c9b6372a87dfa26bbced4d4c816cc32a65aca22d36dd86d
Name:           perl-Dist-Milla
Version:        1.0.22
Release:        1%{?dist}
Summary:        CPAN distribution builder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Milla
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Milla-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::Zilla::App) >= 6
Requires:       perl(Dist::Zilla::Plugin::InlineFiles)
Requires:       perl(Dist::Zilla::Plugin::StaticInstall)
Requires:       perl(Dist::Zilla::Role::AfterMint)
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::MintingProfile::ShareDir)
Requires:       perl(Dist::Zilla::Role::PluginBundle::Config::Slicer)
Requires:       perl(Dist::Zilla::Role::PluginBundle::Easy)
Requires:       perl(Dist::Zilla::Role::PluginBundle::PluginRemover)
Requires:       perl(Dist::Zilla::Role::TextTemplate)
Requires:       perl(Dist::Zilla::Plugin::CheckChangesHasContent)
Requires:       perl(Dist::Zilla::Plugin::ConfirmRelease)
Requires:       perl(Dist::Zilla::Plugin::CopyFilesFromBuild) >= 0.163040
Requires:       perl(Dist::Zilla::Plugin::CopyFilesFromRelease)
Requires:       perl(Dist::Zilla::Plugin::ExecDir)
Requires:       perl(Dist::Zilla::Plugin::ExtraTests)
Requires:       perl(Dist::Zilla::Plugin::Git::Contributors) >= 0.009
Requires:       perl(Dist::Zilla::Plugin::Git::GatherDir)
Requires:       perl(Dist::Zilla::Plugin::Git::Init) >= 2.012
Requires:       perl(Dist::Zilla::Plugin::GithubMeta)
Requires:       perl(Dist::Zilla::Plugin::License)
Requires:       perl(Dist::Zilla::Plugin::LicenseFromModule) >= 0.05
Requires:       perl(Dist::Zilla::Plugin::Manifest)
Requires:       perl(Dist::Zilla::Plugin::MetaJSON)
Requires:       perl(Dist::Zilla::Plugin::MetaYAML)
Requires:       perl(Dist::Zilla::Plugin::ModuleBuildTiny)
Requires:       perl(Dist::Zilla::Plugin::NameFromDirectory) >= 0.04
Requires:       perl(Dist::Zilla::Plugin::NextRelease)
Requires:       perl(Dist::Zilla::Plugin::PodSyntaxTests)
Requires:       perl(Dist::Zilla::Plugin::Prereqs::FromCPANfile) >= 0.06
Requires:       perl(Dist::Zilla::Plugin::ReadmeAnyFromPod) >= 0.163250
Requires:       perl(Dist::Zilla::Plugin::ReadmeFromPod) >= 0.37
Requires:       perl(Dist::Zilla::Plugin::ReversionOnRelease) >= 0.04
Requires:       perl(Dist::Zilla::Plugin::ShareDir)
Requires:       perl(Dist::Zilla::Plugin::Test::Compile)
Requires:       perl(Dist::Zilla::Plugin::TestRelease)
Requires:       perl(Dist::Zilla::Plugin::UploadToCPAN)
Requires:       perl(Dist::Zilla::Plugin::VersionFromMainModule)
Requires:       perl(Dist::Zilla::PluginBundle::Git)
Requires:       perl(Module::CPANfile) >= 0.9025
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Dist::Zilla::App\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Milla is a Dist::Zilla profile. It is a collection of Dist::Zilla plugin
bundle, Dist::Zilla minting profile and a command line wrapper. It is designed
around the "Convention over Configuration" philosophy, and by default doesn't
rewrite module files nor requires you to change your work flow at all.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Milla-v%{version}
# Remove author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax\.t}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
rm %{buildroot}/%{_mandir}/man3/auto::share::module::Dist-Zilla-MintingProfile-Milla::default::Module.pm.template.3pm
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dist-Milla-tests -f %{oreon_filedir}/perl-Dist-Milla-tests.list

%changelog

%autochangelog
