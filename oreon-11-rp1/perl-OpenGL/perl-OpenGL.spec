%global source0_hash f0a02809699e27a93f2721747d2dc0c133d685002c48f435aa0496b32d82c182
%global cpanversion 0.70
Name:           perl-OpenGL
Version:        %{cpanversion}00
Release:        33%{?dist}
Summary:        Perl OpenGL bindings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://sourceforge.net/projects/pogl/
Source0:        OpenGL-%{cpanversion}_repackaged.tar.gz
Source1:        repackage.sh
Patch0:         0001-Don-t-check-current-display-for-extensions.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
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
BuildRequires:  sed
# /oreon:deps
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

mv test.pl demo.pl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
   dist=NO_EXCLUSIONS verbose
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
