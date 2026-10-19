%global source0_hash 6d64d3be1429cc1eb4e88a8f2022fec910ea3e0792da4fe58d3edf7695c46ca2
Name:           perl-GD
Version:        2.86
Release:        1%{?dist}
Summary:        Perl interface to the GD graphics library
License:        GPL-1.0-or-later OR Artistic-2.0
URL:            https://metacpan.org/release/GD
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/GD-%{version}.tar.gz
Patch1:         GD-2.77-cflags.patch
Patch2:         GD-2.84-XPM.patch
Requires:       gd >= 2.0.28
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(GD::Polygon\\)$
%{?perl_default_filter}
Provides:       perl(GD)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a auto-loadable interface module for GD, a popular library
for creating and manipulating PNG files. With this library you can
create PNG images on the fly or modify existing files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n GD-%{version}

# Upstream wants -Wformat=1 but we don't
%patch -P 1

# Don't disable XPM support if GD config doesn't explicitly require -lX11
%patch -P 2

# Fix shellbangs in sample scripts
perl -pi -e 's|/usr/local/bin/perl\b|%{__perl}|' \
      demos/{*.{pl,cgi},truetype_test}
chmod -c -x demos/png2jpeg.pl

%build

perl Makefile.PL \
      INSTALLDIRS=vendor \
      NO_PACKLIST=1 \
      NO_PERLLOCAL=1 \
      OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test TEST_VERBOSE=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
