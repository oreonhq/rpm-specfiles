%global source0_hash 7e52bc12f893663ea6b0cf4f4dda4350af4cead6e137b7bd7eebc2371df728b7
%global commit  0dcf187a159c365b6d4e4e0ed5849f7b706da408
%global date    20181018
%global forgeurl https://github.com/coin-or/Csdp
%global octavedir %{_datadir}/octave/site/m/Csdp
Name:           csdp
Version:        6.2.0
Summary:        C library for SemiDefinite Programming
%forgemeta
License:        EPL-2.0 AND Knuth-CTAN
Release:        1%{?dist}
URL:            %{forgeurl}/wiki
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/Csdp-%{commit}.tar.gz
Source1:        Csdp.INDEX
Source2:        %{name}.1
Source3:        %{name}-theta.1
Source4:        %{name}-graphtoprob.1
Source5:        %{name}-complement.1
Source6:        %{name}-rand_graph.1
Patch:          %{name}-ansi-c.patch
ExcludeArch:    %{ix86}
Provides:       coin-or-Csdp = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
CSDP is a library of routines that implements a predictor corrector variant of
the semidefinite programming algorithm of Helmberg, Rendl, Vanderbei, and
Wolkowicz.  The main advantages of this code are that it is written to be used
as a callable subroutine, it is written in C for efficiency, the code runs in
parallel on shared memory multiprocessor systems, and it makes effective use
of sparsity in the constraint matrices.

%package devel
Summary:        Header files for CSDP
License:        EPL-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coin-or-Csdp-devel = %{version}-%{release}
%description devel
This package contains the header files necessary to develop programs that use
the CSDP library.

%package tools
Summary:        Command line tools for working with CSDP
License:        EPL-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coin-or-Csdp-tools = %{version}-%{release}
%description tools
This package contains command-line wrappers around the CSDP library, including
a solver, a program for computing the Lovasz Theta number of a graph, and some
graph manipulation programs.

Note that "csdp-" has been prefixed to some of the binary names, due to the
generic nature of the names.

%package octave
Summary:        Octave interface to CSDP
License:        EPL-2.0
Requires:       %{name}-tools = %{version}-%{release}, octave
BuildArch:      noarch
%description octave
This package contains an Octave interface to the C library for SemiDefinite
Programming.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

CFLAGS='%{build_cflags} -I../include -I%{_includedir}/flexiblas -DNOSHORTS -DUSESIGTERM -DUSEGETTIME -DBIT64 -DHIDDENSTRLEN -DCSDP_NEED_BLAS'
LIBS='%{build_ldflags} -L../lib -lsdp'
sed -i -e "s|^CFLAGS=.*|CFLAGS=${CFLAGS}|" \
       -e "s|^LIBS=.*|LIBS=${LIBS} -lflexiblas -lm|" \
    solver/Makefile theta/Makefile
cd lib
gcc ${CFLAGS} -DUSEOPENMP -fopenmp -fPIC -shared -Wl,--soname=libsdp.so.6 *.c \
  -o libsdp.so.%{version} %{build_ldflags} -lgomp -lflexiblas -lm
ln -s libsdp.so.%{version} libsdp.so.6
ln -s libsdp.so.6 libsdp.so
cd ../solver
%make_build CFLAGS="$CFLAGS" LIBS="$LIBS"
cd ../theta
gcc $CFLAGS -c complement.c
gcc $CFLAGS -o complement %{build_ldflags} complement.o
gcc $CFLAGS -c rand_graph.c
gcc $CFLAGS -o rand_graph %{build_ldflags} rand_graph.o
%make_build CFLAGS="$CFLAGS" LIBS="$LIBS"
%install
mkdir -p %{buildroot}%{_libdir}
cp -pP lib/libsdp* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
cp -p solver/csdp %{buildroot}%{_bindir}
cp -p theta/theta %{buildroot}%{_bindir}/csdp-theta
cp -p theta/graphtoprob %{buildroot}%{_bindir}/csdp-graphtoprob
cp -p theta/complement %{buildroot}%{_bindir}/csdp-complement
cp -p theta/rand_graph %{buildroot}%{_bindir}/csdp-rand_graph
mkdir -p %{buildroot}%{_includedir}/csdp
cp -p include/*.h %{buildroot}%{_includedir}/csdp
mkdir -p %{buildroot}%{octavedir}
cp -p matlab/*.m %{buildroot}%{octavedir}
cp -p %{SOURCE1} %{buildroot}%{octavedir}/INDEX
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
  %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n csdp-devel -f %{oreon_filedir}/csdp-devel.list
%files -n csdp-tools -f %{oreon_filedir}/csdp-tools.list
%files -n csdp-octave -f %{oreon_filedir}/csdp-octave.list

%changelog

%autochangelog
