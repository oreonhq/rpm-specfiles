%global source0_hash e78a116feb2ebd04de31a8d8707c65e8e15a64aa8999a40fea305e3909bd6533
%undefine __cmake_in_source_build
Name:           nexus
Version:        4.4.3
Release:        21%{?dist}
Summary:        Libraries and tools for the NeXus scientific data file format
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            http://www.nexusformat.org/
Source0:        https://github.com/nexusformat/code/archive/v%{version}/code-v%{version}.tar.gz
Patch0:         nexus-fix-version.patch
Patch1:         nexus-el6-fortran-flags.patch
Patch2:         nexus-fix-nxtranslate-xml.patch
Requires:       hdf5
Requires:       hdf
Requires:       mxml
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hdf-devel
BuildRequires:  hdf5-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)
BuildRequires:  python-docutils
# /oreon:deps
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
rm %{buildroot}%{_libdir}/libNeXus.a
rm %{buildroot}%{_libdir}/libNeXusCPP.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n nexus-devel -f %{oreon_filedir}/nexus-devel.list
%files -n nexus-tools -f %{oreon_filedir}/nexus-tools.list

%changelog

%autochangelog
