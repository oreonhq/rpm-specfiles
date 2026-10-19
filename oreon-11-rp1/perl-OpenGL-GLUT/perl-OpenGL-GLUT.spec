%global source0_hash 0db77a18c672b1e15f89c7d5c6b643bcc8d1a8bf3dd946b72ddc6fde9ff887fe
Name:           perl-OpenGL-GLUT
Version:        0.7201
Release:        1%{?dist}
Summary:        Perl bindings to GLUT/FreeGLUT GUI toolkit
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/OpenGL-GLUT
Source0:        OpenGL-GLUT-%{version}_repackaged.tar.gz
Source1:        repackage.sh
Patch0:         OpenGL-GLUT-0.72-Don-t-check-current-display-for-extensions.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
OpenGL::GLUT is the alpha release of a stand-alone module for GLUT/FreeGLUT
bindings extracted from code in the original Perl OpenGL module. The
purpose is to make this functionality available independent of the legacy
OpenGL module for use with OpenGL::Modern.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n OpenGL-GLUT-%{version}
%patch -P0 -p1
# Unbundle GL headers
find include -type f -delete
# Remove executable bits
find -type f -exec chmod a-x {} +

%build

mv test.pl demo.pl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
    dist=NO_EXCLUSIONS NO_PACKLIST=1 NO_PERLLOCAL=1 verbose
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
