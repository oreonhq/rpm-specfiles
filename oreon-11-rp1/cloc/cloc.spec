%global source0_hash 8099b6275c124f662690f2db3581cd2ad4e9ad4e08332288719838ded00d1da5

Name:           cloc
Version:        2.08
Release:        1%{?dist}
Summary:        Count lines of code
License:        GPL-2.0-or-later
URL:            https://github.com/AlDanial/cloc
Source0:        https://github.com/AlDanial/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  perl-generators
# Runtime
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
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl-interpreter
BuildRequires:  perl-Pod-Checker
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
A tool to count lines of code in various languages from a given directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}/Unix

%install
%make_install

%check
# Fail with tests about issue #132
sed -i -e '/01_opts.t/d' Makefile
# Requires a git submodule
sed -i -e '/02_git.t/d' Makefile
make test

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
