%global source0_hash e263c03b36c3fa60d9edca39c72332036c75bbaeb8e69630e10e321d1a985133
Name:       git-autofixup
Version:    0.005000
Release:        1%{?dist}
Summary:        Autofixup - create fixup commits for topic branches
License:    Artistic-2.0
URL:        https://github.com/torbiak/git-autofixup/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TORBIAK/App-Git-Autofixup-%{version}.tar.gz
BuildArch:  noarch
Requires:       git-core
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  git-core
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-macros
# /oreon:deps
%description
git-autofixup parses hunks of changes in the working directory out of \
git diff output and uses git blame to assign those hunks to commits in \
<revision>..HEAD, which will typically represent a topic branch, and then \
creates fixup commits to be used with git rebase --interactive --autosquash. \
It is assumed that hunks near changes that were previously committed to \
the topic branch are related.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-Git-Autofixup-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

git config --global init.defaultBranch master
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
