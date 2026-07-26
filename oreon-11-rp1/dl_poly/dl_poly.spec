%global source0_hash 3bbfb0c17d53bfedc7a83aa7b64c428168e82d7db321e3c6a6ab2fa1f56ee565

# Copyright (c) 2013, 2014, 2015 Dave Love, Liverpool University
# The licence for this file is as for the package itself.

# fixme: look at shipping example/benchmark data (~ 40MB total)

%global _lto_fflags %nil

# Allow -march=native if you want to rebuild
%bcond_with native

%ifarch %java_arches
%global java 1
%endif

Name:		dl_poly
Version:	1.10
Release:	27%{?dist}
Summary:	General purpose classical molecular dynamics (MD) simulation
License:	BSD-3-Clause
URL:		https://gitlab.com/DL_POLY_Classic
# NB, the numbers in this URL change when it's updated, but the version doesn't
Source0:	https://gitlab.com/DL_POLY_Classic/dl_poly/-/archive/RELEASE-%(echo %version|tr . -)/%{name}-%{version}.tar.gz
Source1:	dl_poly-makefile
Source2:	dl_poly.desktop
# Change executable
Patch2:		dl_poly-javaexec.patch
BuildRequires:	gcc-gfortran %{?java:java-devel} openmpi-devel desktop-file-utils
BuildRequires:	mpich-devel
BuildRequires: make
Requires:	%{name}-common = %{version}-%{release}
ExcludeArch:   i686

%global base_description \
DL_POLY Classic is a general purpose molecular dynamics simulation\
package developed at Daresbury Laboratory by W. Smith, T.R. Forester\
and I.T. Todorov.  It is based on the package DL_POLY_2, which was\
originally developed by the Computational Chemistry Group, (CCG) at\
Daresbury Laboratory under the auspices of the Engineering and\
Physical Sciences Research Council (EPSRC) for (CCP5), the EPSRC's\
Collaborative Computational Project for the Computer Simulation of\
Condensed Phases.\
\
DL_POLY Classic achieves parallelisation using the Replicated Data strategy\
which is suitable for homogeneous, distributed-memory, parallel\
computers.  The code is useful for simulations of up to 30,000 atoms\
with good parallel performance on up to 100 processors, though in some\
circumstances it can exceed or fail to reach these limits.\
\
Reference: I.T. Todorov, W. Smith, K. Trachenko & M.T. Dove,\
Journal of Materials Chemistry, (2006) 16, 1911-1918

%description
%{base_description}

%package common
Summary: General purpose classical molecular dynamics (MD) simulation - common files
BuildArch: noarch

%description common
Common files for %name.
This package contains, principally the "utility" source and data files.

%package doc
Summary: Documentation for %name and %{name}-gui
BuildArch: noarch

%description doc
Documentation for %{name} and %{name}-gui.

%package openmpi
Summary: General purpose classical molecular dynamics (MD) simulation - openmpi version
Requires: openmpi%{_isa}, %{name}-common = %{version}-%{release}

%description openmpi
%{base_description}

This is a parallel version using openmpi.

%package mpich
Summary: General purpose classical molecular dynamics (MD) simulation - mpich version
Requires: mpich%{_isa}, %{name}-common = %{version}-%{release}

%description mpich
%{base_description}

This is a parallel version using mpich.

%if 0%{?java}
%package gui
Summary: GUI for %name
Requires: java-25, jpackage-utils
BuildArch: noarch

%description gui
This package provides the Java-based graphical user interface for %name.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# The tarball directory is like
# dl_poly-RELEASE-1-10-565a1de4234430452c8248426ca2fa15d532334d
%setup -q -n %(tar ft %SOURCE0|head -n1|sed s,/,,)
rm java/GUI.jar
cp %{SOURCE1} source/Makefile

%patch -P2 -p1

%build
# Serial version no longer builds.  Reported to Bill Smith, but no fix
# forthcoming.
%if %{with native}
%global native NATIVE=-march=native
%else
%global native NATIVE=
%endif
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global aam -fallow-argument-mismatch
%endif
export FFLAGS="%build_fflags -O3 -ffast-math $(NATIVE) -Wno-unused-variable %{?aam}"
export LDFLAGS="%build_ldflags"
# Parallel make fails.  Extra opt flags are from the original.
%global dobuild \
mkdir $MPI_COMPILER;\
%make_build -j1 build PAR=1 %native; \
mv ../execute/DLPOLY.X $MPI_COMPILER/%{name}$MPI_SUFFIX

cd source

%{_openmpi_load}
%{dobuild}
%{_openmpi_unload}
rm  basic_comms.o merge_tools.o pass_tools.o
make clean
%{_mpich_load}
%{dobuild}
%{_mpich_unload}

%if 0%{?java}
cd ../java
sh build
cat <<+ >%{name}_gui
#!/bin/sh
exec java -jar %{_javadir}/DL_POLY_GUI.jar
+
cd ..
%endif
cat <<+ >README.running
Use the environment modules command
  module load <mpi>-%{_arch}
to put the %{name}_<mpi> parallel executable on your path,
where <mpi> may be openmpi or mpich.  In a batch job You may
need to source /etc/profile.d/modules.sh or /etc/profile.d/modules.csh
first.
+

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/%name
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/openmpi/bin
install source/openmpi*/%{name}_* $RPM_BUILD_ROOT%{_libdir}/openmpi/bin
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/mpich/bin
install source/mpich*/%{name}_* $RPM_BUILD_ROOT%{_libdir}/mpich/bin
cp data/README README.data
chmod 644 utility/dl2xyz
cp -a utility $RPM_BUILD_ROOT%{_datadir}/%{name}
%if 0%{?java}
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 java/GUI.jar $RPM_BUILD_ROOT%{_javadir}/DL_POLY_GUI.jar
install -m 755 java/%{name}_gui $RPM_BUILD_ROOT%{_bindir}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
%endif
chmod 644 LICENCE.pdf manual/JavaGUI.pdf

%check
# Would depend on shipping at least some data files, per fixme above

%files common
%license LICENCE.pdf
%doc README.data README
%{_datadir}/%{name}

%files doc
%license LICENCE.pdf
%doc manual/USRMAN.pdf

%if 0%{?java}
%files gui
%license LICENCE.pdf
%{_javadir}/DL_POLY_GUI.jar
%{_bindir}/%{name}_gui
%doc README manual/JavaGUI.pdf
%{_datadir}/applications/*
%endif

%files openmpi
%{_libdir}/openmpi/bin/*

%files mpich
%{_libdir}/mpich/bin/*

%changelog
%autochangelog
