%global source0_hash b2c391cd5463577efc76d8bfb28ead2b3d4e3a6fa92db0ef34c00dc9f4cfa707

Name:           perl-Test-Run-CmdLine
Version:        0.0132
Release:        16%{?dist}
Summary:        Run TAP tests from command line using the Test::Run module
# lib and other code:   MIT
# bin/runprove:         GPL+ or Artistic
## sub-packaged:
# examples:             BSD
# Automatically converted from old format: (GPL+ or Artistic) and MIT - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-MIT
URL:            https://metacpan.org/release/Test-Run-CmdLine
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-CmdLine-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
# Prefer Module::Build over ExtUtils::Maker because the Test::Run::Builder
# uses Module::Build too
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Moose)
# MooseX::Getopt::Basic version from unused MooseX::Getopt in META
BuildRequires:  perl(MooseX::Getopt::Basic) >= 0.26
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.12
BuildRequires:  perl(Test::Run::Base)
BuildRequires:  perl(Test::Run::Iface)
# Test::Run::Obj version taken from unused Test::Run::Core specified in META
BuildRequires:  perl(Test::Run::Obj) >= 0.0126
BuildRequires:  perl(Test::Run::Trap::Obj)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(YAML::XS)
# Test:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(mro)
BuildRequires:  perl(Test::More)
# MooseX::Getopt::Basic version from unused MooseX::Getopt in META
Requires:       perl(MooseX::Getopt::Basic) >= 0.26
Requires:       perl(Test::Run::Obj) >= 0.0126

# Ignore dependencies in documentation
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Run::Obj\\)$

%description
These Perl modules allow one to run TAP tests and analyze them from the
command line using the Test::Run module. It provides runprove tool with
command line facilities similar to Test::Harness' prove tool.

%package examples
Summary:        Examples for Test::Run::CmdLine Perl module
# lib and other code:   MIT
# bin/runprove:         GPL+ or Artistic
# examples:             BSD
# Automatically converted from old format: BSD - review is highly recommended.
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

%check
./Build test

%files
%license LICENSE
%doc Changes docs README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files examples
%doc examples

%changelog
%autochangelog
