%global source0_hash 0b7786e3cc92e062f12ec1b969742d8490aa1adbc37f7f3389434575ef3ab724
Name:           perl-App-GitHooks
Version:        1.9.0
Release:        1%{?dist}
Summary:        Extensible plugins system for git hooks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-GitHooks
Source0:        https://cpan.metacpan.org/modules/by-module/App/App-GitHooks-v%{version}.tar.gz
BuildArch:      noarch
Requires:       git-core >= 1.7.4.1
# oreon:deps
BuildRequires:  findutils
BuildRequires:  git-core
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(Data::Validate::Type)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git::Repository)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Encoding)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Git)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires::Git)
BuildRequires:  perl(Test::Type)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
App::GitHooks is an extensible and easy to configure git hooks framework
that supports many plugins.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-GitHooks-v%{version}
# Do no use /usr/bin/env in shellbangs
find -type f -exec sed -i -e \
    's|\(#!\)\{0,1\}/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|g' \
    {} +

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export LC_ALL=C.UTF-8
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
