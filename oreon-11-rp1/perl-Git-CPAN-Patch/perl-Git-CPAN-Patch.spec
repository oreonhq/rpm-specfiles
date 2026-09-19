%global source0_hash 8b1bfe0afa63f709a3de225db752551a56a6d99c4666b5fc5b5663c11bcbea0e

Name:           perl-Git-CPAN-Patch
Summary:        Patch CPAN modules using Git
Version:        2.5.0
Release:        11%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Git-CPAN-Patch-%{version}.tar.gz
URL:            https://metacpan.org/release/Git-CPAN-Patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Archive::Any)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(autodie)
BuildRequires:  perl(BackPAN::Index)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::ParseDistribution)
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::chmod)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Repository)
BuildRequires:  perl(List::Pairwise)
# BuildRequires:  perl(LWP::Simple)
# BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MetaCPAN::API)
BuildRequires:  perl(MetaCPAN::Client)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::App)
BuildRequires:  perl(MooseX::App::Command)
BuildRequires:  perl(MooseX::App::Role)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Tiny)
# BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
# Tests only
BuildRequires:  git
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DDP)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Git::Repository::Plugin::AUTOLOAD)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       git
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::ParseDistribution)
Requires:       perl(File::Copy)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::Protocol::ftp)
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::UserAgent)

%{?perl_default_filter}

%description
Git::CPAN::Patch provides a suite of git commands aimed at making trivially
easy the process of grabbing any distribution off CPAN, stuffing it in a
local git repository and, once gleeful hacking has been perpetrated,
sending back patches to its maintainer.

This package provides the backend Perl modules required.  For the git
commands, etc, please install the git-cpan-patch package.

%package -n git-cpan-patch
Summary:        Patch CPAN modules using Git
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl-Git-CPAN-Patch = %{version}-%{release}
Requires:       git, git-email

%description -n git-cpan-patch
git-cpan-patch provides a suite of git commands aimed at making trivially
easy the process of grabbing any distribution off CPAN, stuffing it in a
local git repository and, once gleeful hacking has been perpetrated,
sending back patches to its maintainer.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       git
Requires:       perl(Git::Repository::Plugin::AUTOLOAD)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Git-CPAN-Patch-%{version}
# Fix shellbang
perl -MConfig -pi -e 's|^#!/usr/bin/env perl|$Config{startperl} |' bin/git-cpan
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# upstream now installs to /usr/bin; we still prefer /usr/libexec/git-core
install -d -m 0755 %{buildroot}%{_libexecdir}/git-core
mv %{buildroot}/%{_bindir}/* %{buildroot}%{_libexecdir}/git-core/

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_libexecdir}/git-core/git-cpan %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
git config --global user.email "perl-Git-CPAN-Patch-owner@fedoraproject.org"
git config --global user.name "perl-Git-CPAN-Patch Owner"
git config --global init.defaultBranch "development"
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
git config --global user.email "perl-Git-CPAN-Patch-owner@fedoraproject.org"
git config --global user.name "perl-Git-CPAN-Patch Owner"
git config --global init.defaultBranch "development"
make test

%files
%license LICENSE
%doc AUTHOR_PLEDGE Changes README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n git-cpan-patch
%license LICENSE
%doc AUTHOR_PLEDGE Changes README.mkdn
%{_libexecdir}/git-core
%{_mandir}/man1/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
