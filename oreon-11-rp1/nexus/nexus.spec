%global source0_hash e78a116feb2ebd04de31a8d8707c65e8e15a64aa8999a40fea305e3909bd6533

# Undefine CMake in-source builds in order to be consistent with f33+
%undefine __cmake_in_source_build

Name:           nexus
Version:        4.4.3
Release:        21%{?dist}
Summary:        Libraries and tools for the NeXus scientific data file format

# The entire source code is GPLv2+ except nxdir which is MIT
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            http://www.nexusformat.org/
Source0:        https://github.com/nexusformat/code/archive/v%{version}/code-v%{version}.tar.gz
# Fix the version reported by the library
#   (see https://github.com/nexusformat/code/issues/437)
Patch0:         nexus-fix-version.patch
# Remove an additional flag that doesn't work in the EL6 version of gfortran
Patch1:         nexus-el6-fortran-flags.patch
# Back port fix from master branch
Patch2:         nexus-fix-nxtranslate-xml.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++ 
BuildRequires:  hdf5-devel
BuildRequires:  hdf-devel
BuildRequires:  make
BuildRequires:  python-docutils

Requires:       hdf5
Requires:       hdf
Requires:       mxml

%description
NeXus is common data format for neutron, x-ray, and muon science. This
package provides tools and libraries for accessing these files.  The on disk
representation is based upon either HDF4, HDF5 or XML

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hdf5-devel
Requires:       hdf-devel

%description    devel
The %{name}-devel package contains header files for
developing applications that use %{name}

%package        tools
Summary:        Applications for reading and writing NeXus files.
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       readline
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)

%description    tools
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n code-%{version}
%patch -P0 -p1 -b .fix-version

%if 0%{?el6}
# Fortran flag not supported on EL6
%patch -P1 -p1 -b .el6-flags
%endif

%patch -P2 -p1 -b .nxtranslate

%build
%cmake \
       -DENABLE_HDF5=1 \
       -DENABLE_HDF4=1 \
       -DENABLE_CXX=1 \
       -DENABLE_APPS=1 .
%cmake_build

%install
%cmake_install
# Remove the static libraries 
rm %{buildroot}%{_libdir}/libNeXus.a
rm %{buildroot}%{_libdir}/libNeXusCPP.a

%files
%license COPYING
%doc %{_datadir}/doc/NeXus/README.doc
%{_libdir}/libNeXus.so.1*
%{_libdir}/libNeXusCPP.so.1*

%files devel
%license COPYING
%{_includedir}/nexus/
%{_libdir}/pkgconfig/
%{_libdir}/libNeXus.so
%{_libdir}/libNeXusCPP.so

%files tools
%{_bindir}/nxbrowse
%{_bindir}/nxconvert
%{_bindir}/nxsummary
%{_bindir}/nxtranslate
%{_bindir}/nxtraverse
%{_mandir}/man1/nxbrowse.1.gz
%{_mandir}/man1/nxconvert.1.gz 
%{_mandir}/man1/nxsummary.1.gz
# MIT
%license %{_datadir}/doc/NeXus/programs/nxdir/LICENSE
%doc %{_datadir}/doc/NeXus/programs/nxdir/CHANGES
%doc %{_datadir}/doc/NeXus/programs/nxdir/README
%doc %{_datadir}/doc/NeXus/programs/nxdir/TODO
%{_bindir}/nxdir
%{_mandir}/man1/nxdir.1.gz  

%changelog
%autochangelog
