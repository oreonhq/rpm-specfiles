%global source0_hash 04497d2592f8f811bc66f4e32f6da8fe443086f8c27b8ba7bce395bf82f0f9fb
Name:           perl-Git-Repository
Version:        1.326
Release:        1%{?dist}
Summary:        Perl interface to Git repositories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Git-Repository
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/Git-Repository-%{version}.tar.gz
BuildArch:      noarch
Requires:       git
Requires:       perl(Git::Version::Compare) >= 1.001
Requires:       perl(System::Command) >= 1.118
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Git::Version::Compare|Test::Requires::Git|System::Command)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}perl\\((Git::Repository::Plugin::Hello(|2)|MyGit::Hello)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  git
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Version::Compare)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(System::Command)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires::Git)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Git::Repository is a Perl interface to Git, for scripted interactions with
repositories. It's a low-level interface that allows calling any Git
command, whether porcelain or plumbing, including bidirectional commands
such as git commit-tree.

%package -n perl-Test-Git
Summary:        Helper functions for test scripts using Git
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Git::Version::Compare) >= 1.001
Conflicts:      perl-Git-Repository < 1.325-12
%description -n perl-Test-Git
Test::Git provides a number of helpful functions when running test scripts that
require the creation and management of a Git repository.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl-Test-Git = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Requires::Git) >= 1.005
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Git-Repository-%{version}
# Remove always skipped tests
for F in t/author-distmeta.t t/author-pod-coverage.t t/author-pod-syntax.t t/test-all-git.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t t/sudo.pl; do
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Test-Git usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Git -f %{oreon_filedir}/perl-Test-Git.list
%files -n perl-Git-Repository-tests -f %{oreon_filedir}/perl-Git-Repository-tests.list

%changelog

%autochangelog
