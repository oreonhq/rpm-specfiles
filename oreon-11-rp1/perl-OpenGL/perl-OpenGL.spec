%global source0_hash f0a02809699e27a93f2721747d2dc0c133d685002c48f435aa0496b32d82c182

%global cpanversion 0.70

Name:           perl-OpenGL
Version:        %{cpanversion}00
Release:        33%{?dist}
Summary:        Perl OpenGL bindings
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://sourceforge.net/projects/pogl/
# <https://cpan.metacpan.org/authors/id/C/CH/CHM/OpenGL-%%{cpanversion}.tar.gz>
# stripped from a non-free files using ./repackage.sh %%{version} command,
# bug #1612850, <https://sourceforge.net/p/pogl/bugs/27/>
Source0:        OpenGL-%{cpanversion}_repackaged.tar.gz
# GPLv2-licensed code for generating Source0 from an upstream tarball,
# bug #1612850, <https://sourceforge.net/p/pogl/bugs/27/>
Source1:        repackage.sh
Patch0:         0001-Don-t-check-current-display-for-extensions.patch
BuildRequires:  gcc
# gcc-c++ for libstdc++.so linked in Makefile.PL
BuildRequires:  gcc-c++
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  freeglut-devel
BuildRequires:  libICE-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Perl bindings to implementations of OpenGL and GLUT, providing virtually all
of the OpenGL 1.0, and 1.1 functions, and most of 1.2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n OpenGL-%{cpanversion}
%patch -P0 -p1
# Unbundle GL headers
find include -type f  \! -name glprocs.h -exec rm {} +
# Remove executable bits
find -type f -exec chmod a-x {} +

%build
# This is basically not a test, but an interactive demo
mv test.pl demo.pl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
   dist=NO_EXCLUSIONS verbose
# Certain OpenGL calls may not be present in our OpenGL
# implementation, let us just ignore them.
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/OpenGL*
%{_mandir}/man3/*
%license COPYRIGHT
%doc CHANGES KNOWN_PROBLEMS README Release_Notes
%doc SUPPORTS TODO demo.pl

%changelog
%autochangelog
