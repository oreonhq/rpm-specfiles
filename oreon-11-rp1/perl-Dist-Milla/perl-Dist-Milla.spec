%global source0_hash 27f08742d8e024de2c9b6372a87dfa26bbced4d4c816cc32a65aca22d36dd86d

Name:           perl-Dist-Milla
Version:        1.0.22
Release:        8%{?dist}
Summary:        CPAN distribution builder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Milla
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Milla-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Dist::Zilla::App version from Dist::Zilla in META
# Dist::Zilla::App 6 not used at tests
# Dist::Zilla::Plugin::InlineFiles not used at tests
# Dist::Zilla::Plugin::StaticInstall not used at tests
# Dist::Zilla::Role::AfterMint not used at tests
# Dist::Zilla::Role::MetaProvider not used at tests
# Dist::Zilla::Role::MintingProfile::ShareDir not used at tests
# Dist::Zilla::Role::PluginBundle::Config::Slicer not used at tests
# Dist::Zilla::Role::PluginBundle::Easy not used at tests
# Dist::Zilla::Role::PluginBundle::PluginRemover not used at tests
# Dist::Zilla::Role::TextTemplate not used at tests
# File::pushd not used at tests
# Git::Wrapper not used at tests
# Moose not used at tests
# namespace::autoclean not used at tests
# parent not used at tests
# version not used at tests
# Additional plugins defined in META, this is a plugin bundle:
# Dist::Zilla::Plugin::CheckChangesHasContent not used at tests
# Dist::Zilla::Plugin::ConfirmRelease not used at tests
# Dist::Zilla::Plugin::CopyFilesFromBuild 0.163040 not used at tests
# Dist::Zilla::Plugin::CopyFilesFromRelease not used at tests
# Dist::Zilla::Plugin::ExecDir not used at tests
# Dist::Zilla::Plugin::ExtraTests not used at tests
# Dist::Zilla::Plugin::Git::Contributors 0.009 not used at tests
# Dist::Zilla::Plugin::Git::GatherDir not used at tests
# Dist::Zilla::Plugin::Git::Init 2.012 not used at tests
# Dist::Zilla::Plugin::GithubMeta not used at tests
# Dist::Zilla::Plugin::License not used at tests
# Dist::Zilla::Plugin::LicenseFromModule 0.05 not used at tests
# Dist::Zilla::Plugin::Manifest not used at tests
# Dist::Zilla::Plugin::MetaJSON not used at tests
# Dist::Zilla::Plugin::MetaYAML not used at tests
# Dist::Zilla::Plugin::ModuleBuildTiny not used at tests
# Dist::Zilla::Plugin::NameFromDirectory 0.04 not used at tests
# Dist::Zilla::Plugin::NextRelease not used at tests
# Dist::Zilla::Plugin::PodSyntaxTests not used at tests
# Dist::Zilla::Plugin::Prereqs::FromCPANfile 0.06 not used at tests
# Dist::Zilla::Plugin::ReadmeAnyFromPod not used at tests
# Dist::Zilla::Plugin::ReadmeFromPod not used at tests
# Dist::Zilla::Plugin::ReversionOnRelease 0.04 not used at tests
# Dist::Zilla::Plugin::ShareDir not used at tests
# Dist::Zilla::Plugin::Test::Compile not used at tests
# Dist::Zilla::Plugin::TestRelease not used at tests
# Dist::Zilla::Plugin::UploadToCPAN not used at tests
# Dist::Zilla::Plugin::VersionFromMainModule not used at tests
# Dist::Zilla::PluginBundle::Git not used at tests
# Module::CPANfile 0.9025 not used at tests
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Dist::Zilla::App version from Dist::Zilla in META
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
# Additional plugins defined in META, this is a plugin bundle:
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

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Dist::Zilla::App\\)$

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
# Remove an unintentional manual,
# <https://github.com/miyagawa/Dist-Milla/issues/45>
rm %{buildroot}/%{_mandir}/man3/auto::share::module::Dist-Zilla-MintingProfile-Milla::default::Module.pm.template.3pm
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{_bindir}/milla
%dir %{perl_vendorlib}/auto
%dir %{perl_vendorlib}/auto/share
%dir %{perl_vendorlib}/auto/share/module
%{perl_vendorlib}/auto/share/module/Dist-Zilla-MintingProfile-Milla
%dir %{perl_vendorlib}/Dist
%{perl_vendorlib}/Dist/Milla
%{perl_vendorlib}/Dist/Milla.pm
%{perl_vendorlib}/Dist/Zilla
%{perl_vendorlib}/Milla.pm
%{_mandir}/man1/milla.*
%{_mandir}/man3/Dist::Milla.*
%{_mandir}/man3/Dist::Milla::*
%{_mandir}/man3/Dist::Zilla::*
%{_mandir}/man3/Milla.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
