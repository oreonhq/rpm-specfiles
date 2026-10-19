%global source0_hash ef1df66e8bd5cee004473231423cf2033450b8f2955f2020628361ff80a5675e
Name:           ack
Version:        3.10.0
Release:        1%{?dist}
Summary:        A Grep-like source code search tool
License:        Artistic-2.0
URL:            http://beyondgrep.com/
Source0:        https://github.com/beyondgrep/ack3/archive/v%{version}/ack3-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Basename) >= 1.00015
Requires:       perl(Config)
Requires:       perl(File::Next) >= 1.18
Requires:       perl(List::Util)
Requires:       perl(Pod::Usage) >= 1.26
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Next\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Template)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(filetest)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Ack is a grep-like search tool designed for use with large heterogeneous
trees of source code.  It searchs recursively and ignores common version
control directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ack3-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
make completion.bash
make completion.zsh
%install
%{make_install}
install -D -p -m 0644 completion.bash %{buildroot}%{bash_completions_dir}/ack
install -D -p -m 0644 completion.zsh  %{buildroot}%{zsh_completions_dir}/_ack
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
