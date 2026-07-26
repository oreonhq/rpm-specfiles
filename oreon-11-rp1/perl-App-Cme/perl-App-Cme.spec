%global source0_hash 1887982d329cbd890e249a47d7c3827f9d70482ce1199609d39432799f68fcc8

Name:           perl-App-Cme
Version:        1.044
Release:        1%{?dist}
Summary:        Check or edit configuration data with Config::Model
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/App-Cme
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/App-Cme-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.34
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config::Model) >= 2.148
# Config::Model::CursesUI - not used at test
# Config::Model::FuseUI - Fuse is not packaged yet
BuildRequires:  perl(Config::Model::Lister)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
# Config::Model::SimpleUI - not used at test
# Config::Model::TermUI - not used at test
# Config::Model::TkUI - not used at test
# Config::Model::Utils::GenClassPod - not used at test
# Data::Dumper - not used at test
BuildRequires:  perl(Encode)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::HomeDir)
# JSON - not used at test
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(open)
BuildRequires:  perl(Path::Tiny) >= 0.125
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
# Tk - not used at test
# Tk::ErrorDialog - not used at test
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML::PP)
# Tests
BuildRequires:  perl(App::Cmd::Tester)
BuildRequires:  perl(Config::Model::Backend::Yaml)
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(lib)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Term::ANSIColor) >= 2.01
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::More)
# Test::Perl::Critic - optional test
Requires:       perl(Config::Model::Backend::Yaml)
Requires:       perl(Config::Model::CursesUI)
Requires:       perl(Config::Model::FuseUI)
Requires:       perl(Config::Model::SimpleUI)
Requires:       perl(Config::Model::TermUI)
Requires:       perl(Config::Model::TkUI)
Requires:       perl(Tk)
Requires:       perl(Tk::ErrorDialog)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Model\\)\s*$

%description
cme and Config::Model are quite modular. The configuration data that you
can edit depend on the other Config::Model distributions installed on your
system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Cme-%{version}
perl -MConfig -pi -e '!s|\A#!.*perl\b|$Config{startperl}|' bin/cme

%build
perl Build.PL installdirs=vendor
./Build

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install bash_completion script
install -D -m 0644 contrib/bash_completion.cme %{buildroot}%{_sysconfdir}/bash_completion.d/cme

# Install tests - copy tests to tmp
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm %{buildroot}/%{_libexecdir}/%{name}/t/perl-critic.t
rm %{buildroot}/%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset AUTHOR_TESTING
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README.pod
%{_bindir}/cme
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Cme*
%{_mandir}/man1/cme*
%{_mandir}/man3/App::Cme*
%{_sysconfdir}/bash_completion.d

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
