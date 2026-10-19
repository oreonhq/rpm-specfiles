%global source0_hash 24064b227481737b65d95e2dab5b677b90c720f8e9a19d28b2152728617c24ed
Name:           perlbrew
Version:        1.02
Release:        1%{?dist}
Summary:        Manage perl installations in your $HOME
License:        MIT
URL:            https://metacpan.org/release/App-perlbrew
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/App-perlbrew-%{version}.tar.gz
BuildArch:      noarch
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
Provides:       perl-App-perlbrew = %{version}-%{release}
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(test2_helpers.pl\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(PerlbrewTestHelpers\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPAN::Perl::Releases)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::PatchPerl)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test2::Plugin::IOEvents)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::ClassicCompare)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Mock)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(ok)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  wget
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir %{buildroot}%{_libexecdir}/%{name}/script
ln -s %{_bindir}/perlbrew %{buildroot}%{_libexecdir}/%{name}/script
chmod 755 %{buildroot}%{_libexecdir}/%{name}/t/fake-bin/curl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perlbrew-tests -f %{oreon_filedir}/perlbrew-tests.list

%changelog

%autochangelog
