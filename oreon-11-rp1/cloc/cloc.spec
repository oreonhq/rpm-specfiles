%global source0_hash a8fac35f4cf42728765580ba11afc2568ad205509a22204663f526169548436d
Name:           cloc
Version:        2.10
Release:        1%{?dist}
Summary:        Count lines of code
License:        GPL-2.0-or-later
URL:            https://github.com/AlDanial/cloc
Source0:        https://github.com/AlDanial/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Pod-Checker
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
%description
A tool to count lines of code in various languages from a given directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}/Unix
%oreon_prep
%install
%make_install
%oreon_autofiles main

%check

sed -i -e '/01_opts.t/d' Makefile
sed -i -e '/02_git.t/d' Makefile
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
