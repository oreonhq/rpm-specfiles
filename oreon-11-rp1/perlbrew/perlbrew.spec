%global source0_hash 7f775fd7922d0ca29650965815f2f362241372a8decc5f6e1b90f757aaffd41c

Name:           perlbrew
Version:        1.01
Release:        4%{?dist}
Summary:        Manage perl installations in your $HOME
License:        MIT
URL:            https://metacpan.org/release/App-perlbrew
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/App-perlbrew-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
# Run-time
BuildRequires:  perl(Capture::Tiny) >= 0.48
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN::Perl::Releases) >= 5.20230720
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PatchPerl) >= 2.08
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.22
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(local::lib) >= 2.000014
BuildRequires:  perl(overload)
#BuildRequires:  perl(Pod::Markdown) >= 2.002
BuildRequires:  perl(Pod::Usage) >= 1.69
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(ok)
BuildRequires:  perl(Path::Class) >= 0.33
BuildRequires:  perl(Test2::Plugin::IOEvents)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::ClassicCompare)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Mock)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception) >= 0.32
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::NoWarnings) >= 1.04
BuildRequires:  perl(Test::Output) >= 1.03
BuildRequires:  perl(Test::Spec) >= 0.47
#BuildRequires:  perl(Test::TempDir::Tiny) >= 0.016
BuildRequires:  wget
Requires:       perl(Capture::Tiny) >= 0.48
Requires:       perl(CPAN::Perl::Releases) >= 5.20230720
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Devel::PatchPerl) >= 2.00
Requires:       perl(ExtUtils::MakeMaker) >= 7.22
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(FindBin)
Requires:       perl(local::lib) >= 2.000014
Requires:       perl(Pod::Usage) >= 1.68
Requires:       curl

# maybe someone expects to find
Provides:       perl-App-perlbrew = %{version}-%{release}

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(test2_helpers.pl\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(PerlbrewTestHelpers\\)

%description
perlbrew is a program to automate the building and installation of perl in
the users HOME. At the moment, it installs everything to ~/perl5/perlbrew,
and requires you to tweak your PATH by including a bashrc/cshrc file it
provides. You then can benefit from not having to run 'sudo' commands to
install cpan modules because those are installed inside your HOME too. It's
almost like an isolated perl environments.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-perlbrew-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
perl -V
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Few tests used ./script/perlbrew
mkdir %{buildroot}%{_libexecdir}/%{name}/script
ln -s %{_bindir}/perlbrew %{buildroot}%{_libexecdir}/%{name}/script
chmod 755 %{buildroot}%{_libexecdir}/%{name}/t/fake-bin/curl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
