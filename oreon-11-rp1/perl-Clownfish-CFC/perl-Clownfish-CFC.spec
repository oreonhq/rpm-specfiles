%global source0_hash 0915ff951c49dc5aff2ad386439a1baff54f00a33aa666594e446cdbf51ff1ac

Name:           perl-Clownfish-CFC
Version:        0.6.3
Release:        32%{?dist}
Summary:        Compiler for Apache Clownfish
# other files:          ASL 2.0
## Unbundled
# lemon:                ASL 2.0
# modules/CommonMark:   BSD and MIT
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Clownfish-CFC
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/Clownfish-CFC-%{version}.tar.gz
# Use system lemon, <https://issues.apache.org/jira/browse/CLOWNFISH-60>
Patch0:         Clownfish-CFC-0.6.0-Use-system-lemon-if-possible.patch
# Handle pkg-config output with multiple arguments, bug #1416443,
# <https://issues.apache.org/jira/browse/CLOWNFISH-113>
Patch1:         Clownfish-CFC-0.6.1-Segment-ExtUtils-PkgConfig-output-into-arguments.patch
# There is charmonizer.c which is becoming a separate project
# <https://git-wip-us.apache.org/repos/asf/lucy-charmonizer.git>. However,
# lucy-charmonizer has not yet been released
# <http://lucy.apache.org/download.html>. Also Clownfish-CFC'c
# lib/Clownfish/CFC/Perl/Build/Charmonic.pm still relies on
# the local location. charmonizer.c is used only at build time.
# Therefore I'm not going to unbudle the charmonizer.c now.
BuildRequires:  cmark-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Modules from buildlib and Clownfish::CFC::Perl::Build::Charmonic from lib
# are used for building
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort) >= 3.14
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# Clownfish not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.18
# Yes, ExtUtils::CBuilder::Platform::Windows::GCC is required
BuildRequires:  perl(ExtUtils::CBuilder::Platform::Windows::GCC)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.00
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Test::More)
# Clownfish not used. I believe it's used only when Clownfish-CFC is called
# from the Clownfish. Adding symetric dependency between Clownfish-CFC and
# Clownfish would create a cycle which is not desired for bulding and
# idempotent at run-time.
Requires:       perl(Devel::PPPort) >= 3.14
Requires:       perl(ExtUtils::CBuilder) >= 0.18
# Yes, ExtUtils::CBuilder::Platform::Windows::GCC is required
Requires:       perl(ExtUtils::CBuilder::Platform::Windows::GCC)
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 3.00

# Filter non-versioned provides. Clownfish/CFC.pm extends name spaces of all
# the other modules that are defined with version in their respective files.
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\([^)]*\\)$

%description
This is a compiler for Apache Clownfish.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Clownfish-CFC-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Unbundle lemon
rm -rf lemon
sed -i -e '/^lemon\//d' MANIFEST
# Unbundle cmark
rm -rf modules/CommonMark
sed -i -e '/^modules\/CommonMark\//d' MANIFEST

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS" \
    --with_system_cmark=1
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc CONTRIBUTING.md NOTICE README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Clownfish*
%{_mandir}/man3/*

%changelog
%autochangelog
