%global source0_hash 0915ff951c49dc5aff2ad386439a1baff54f00a33aa666594e446cdbf51ff1ac
Name:           perl-Clownfish-CFC
Version:        0.6.3
Release:        1%{?dist}
Summary:        Compiler for Apache Clownfish
License:        Apache-2.0
URL:            https://metacpan.org/release/Clownfish-CFC
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Clownfish-CFC-%{version}.tar.gz
Patch0:         Clownfish-CFC-0.6.0-Use-system-lemon-if-possible.patch
Patch1:         Clownfish-CFC-0.6.1-Segment-ExtUtils-PkgConfig-output-into-arguments.patch
Requires:       perl(Devel::PPPort) >= 3.14
Requires:       perl(ExtUtils::CBuilder) >= 0.18
Requires:       perl(ExtUtils::CBuilder::Platform::Windows::GCC)
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 3.00
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\([^)]*\\)$
# oreon:deps
BuildRequires:  cmark-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CBuilder::Platform::Windows::GCC)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
