%global source0_hash b2c391cd5463577efc76d8bfb28ead2b3d4e3a6fa92db0ef34c00dc9f4cfa707
Name:           perl-Test-Run-CmdLine
Version:        0.0132
Release:        1%{?dist}
Summary:        Run TAP tests from command line using the Test::Run module
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-MIT
URL:            https://metacpan.org/release/Test-Run-CmdLine
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-CmdLine-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::Getopt::Basic) >= 0.26
Requires:       perl(Test::Run::Obj) >= 0.0126
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Run::Obj\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Getopt::Basic)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Run::Base)
BuildRequires:  perl(Test::Run::Iface)
BuildRequires:  perl(Test::Run::Obj)
BuildRequires:  perl(Test::Run::Trap::Obj)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
These Perl modules allow one to run TAP tests and analyze them from the
command line using the Test::Run module. It provides runprove tool with
command line facilities similar to Test::Harness' prove tool.

%package examples
Summary:        Examples for Test::Run::CmdLine Perl module
License:        LicenseRef-Callaway-BSD
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description examples
BSD-licensed and quite large examples for %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Run-CmdLine-%{version}
find lib -type f -exec chmod 0644 {} +
# Remove unwanted files
rm --interactive=never examples/eumm-and-test-manifest/MyModule/.cvsignore
perl -i -ne 'print $_ unless m{^examples/eumm-and-test-manifest/MyModule/.cvsignore}' MANIFEST
# Correct shellbangs in examples
perl -MConfig -pi -e 's|^#!perl |$Config{startperl} |' \
    examples/eumm-and-test-manifest/MyModule/t/*.t

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Run-CmdLine-examples -f %{oreon_filedir}/perl-Test-Run-CmdLine-examples.list

%changelog

%autochangelog
