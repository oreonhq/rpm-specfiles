%global source0_hash 68be8751f72daa6061b19084ec01ab78e382e6e461a70336ba3ca34ad23336ac

Name:           perl-Dist-Zilla-Plugin-ModuleBuildTiny
Version:        0.020
Release:        3%{?dist}
Summary:        Build a Build.PL that uses Module::Build::Tiny
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ModuleBuildTiny
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Dist-Zilla-Plugin-ModuleBuildTiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Config)
# Module::Build::Tiny version in META is from a previous version.
# Zilla::Plugin::ModuleBuildTiny::version() outputs a minimal
# Module::Build::Tiny version which depends on a content of the maintained
# project code. The highest one is:
BuildRequires:  perl(Module::Build::Tiny) >= 0.044
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla) >= 4.300039
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::BuildPL)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:  perl(experimental)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Perl)
BuildRequires:  perl(MooseX::Types::Moose)
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
Requires:       perl(Dist::Zilla::File::InMemory)
Requires:       perl(Dist::Zilla::Role::BuildPL)
Requires:       perl(Dist::Zilla::Role::FileGatherer)
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla::Role::TextTemplate)
# Zilla::Plugin::ModuleBuildTiny::version() outputs a minimal
# Module::Build::Tiny version which depends on a content of the maintained
# project code. The highest one is:
Requires:       perl(Module::Build::Tiny) >= 0.044

%description
This Dist::Zilla plugin will create a Build.PL for installing the
distribution using Module::Build::Tiny.

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

%setup -q -n Dist-Zilla-Plugin-ModuleBuildTiny-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Tests Dist::Zilla::Tester creates a temporary directories in CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Dist
%dir %{perl_vendorlib}/Dist/Zilla
%dir %{perl_vendorlib}/Dist/Zilla/Plugin
%{perl_vendorlib}/Dist/Zilla/Plugin/ModuleBuildTiny.pm
%{_mandir}/man3/Dist::Zilla::Plugin::ModuleBuildTiny.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
