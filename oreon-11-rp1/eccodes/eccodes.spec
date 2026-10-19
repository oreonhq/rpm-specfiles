%global source1_hash 8fb321f092cc26007ecee80cbac490eb4cec0d54b87e3a20dbdc92c4dac1f434
%global source0_hash 62e8fa5ca137d138189a5fdd6d5b2205c89cc26338e3f4286aba3d89b49c9f9a
%if 0%{?el8}
%undefine __cmake_in_source_build
%endif
Name:           eccodes
Version:        2.48.0
Release:        1%{?dist}
Summary:        WMO data format decoding and encoding
%global so_version       0.1
%global so_version_f90   0.1
%global datapack_date    20250202
%global final_grib_api_version 1.28.1-1%{?dist}
%ifarch i686 ppc64 armv7hl
  %global obsolete_grib_api 0
%else
  %global obsolete_grib_api 1
%endif
License:        Apache-2.0
URL:            https://confluence.ecmwf.int/display/ECC/ecCodes+Home
Source0:        https://confluence.ecmwf.int/download/attachments/45757960/eccodes-%{version}-Source.tar.gz
Source1:        https://get.ecmwf.int/repository/test-data/eccodes/eccodes_test_data.tar.gz#/eccodes_test_data_%{datapack_date}.tar.gz
Source2:        eccodes_create_man_pages.sh
Patch1:         eccodes-soversion.patch
Requires: %{name}-data = %{version}-%{release}
%if 0%{obsolete_grib_api}
Obsoletes:      grib_api < %{final_grib_api_version}
%endif
ExcludeArch: i686
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  help2man
BuildRequires:  jasper-devel
BuildRequires:  libaec-devel
BuildRequires:  libaec-static
BuildRequires:  libpng-devel
BuildRequires:  netcdf-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
# /oreon:deps
%description
ecCodes is a package developed by ECMWF which provides an application
programming interface and a set of tools for decoding and encoding messages
in the following formats:

 *  WMO FM-92 GRIB edition 1 and edition 2
 *  WMO FM-94 BUFR edition 3 and edition 4 
 *  WMO GTS abbreviated header (only decoding).

A useful set of command line tools provide quick access to the messages. C,
and Fortran 90 interfaces provide access to the main ecCodes functionality.

ecCodes is an evolution of GRIB-API.  It is designed to provide the user with
a simple set of functions to access data from several formats with a key/value
approach.

For GRIB encoding and decoding, the GRIB-API functionality is provided fully
in ecCodes with only minor interface and behaviour changes. Interfaces for C,
and Fortran 90 are all maintained as in GRIB-API.  However, the
GRIB-API Fortran 77 interface is no longer available.

In addition, a new set of functions with the prefix "codes_" is provided to
operate on all the supported message formats. These functions have the same
interface and behaviour as the "grib_" functions. 

A selection of GRIB-API tools has been included in ecCodes (ecCodes GRIB
tools), while new tools are available for the BUFR (ecCodes BUFR tools) and
GTS formats. The new tools have been developed to be as similar as possible
to the existing GRIB-API tools maintaining, where possible, the same options
and behaviour. A significant difference compared with GRIB-API tools is that
bufr_dump produces output in JSON format suitable for many web based
applications.

#####################################################
%package devel
Summary:    Contains ecCodes development files
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gcc-gfortran%{?_isa}
Requires:   jasper-devel%{?_isa}
%if 0%{obsolete_grib_api}
Obsoletes:  grib_api-devel < %{final_grib_api_version}
%endif
%description devel
Header files and libraries for ecCodes.

#####################################################
%package data
Summary:    Data needed by the eccodes library and tools
BuildArch:  noarch
%description data
This package provides all tables and definitions needed
to encode and decode grib and bufr files, and includes
both the official WMO tables and a number of often used
local definitions by ECMWF and other meteorological centers.

#####################################################
# include a LUA scriptlet as suggested on:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
# to assist in replacing a directory by a symlink

%pretrans -n eccodes-data -p <lua>

-- This should solve a problem where directories were replaced
-- by symbolic links when upgrading eccodes from 2.41.0 to 2.42.0
problematic_dirs = {
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/1",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/110",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/174",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/2",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/20",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/21",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/221",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/222",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/223",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/225",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/226",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/227",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/228",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/229",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/230",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/231",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/232",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/233",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/234",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/235",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/236",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/237",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/31",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/41",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/42",
    "/usr/share/eccodes/definitions/bufr/tables/0/local/8/78/64",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/10",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/11",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/12",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/7",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/8",
    "/usr/share/eccodes/definitions/bufr/tables/0/wmo/9"}
for index, path in ipairs(problematic_dirs) do
  print("handling path:" .. index .. ":" .. path)
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if status then
      print("renamed:" .. path .. " to " .. path .. ".rpmmoved")
    end
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
        if status then
          print("renamed:" .. path .. ".rpmmoved to " .. path .. ".rpmmoved." .. suffix)
        end
      end
      os.rename(path, path .. ".rpmmoved")
      print("renamed:" .. path .. " to " .. path .. ".rpmmoved")
    end
  end
end
--#####################################################
%package doc
Summary:    Documentation and example code
BuildArch:  noarch
%description doc
This package contains the html documentation for ecCodes
and a fair number of example programs and scripts to use it
in C, and Fortran 90.

#####################################################
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-Source -p1

# unpack the test data below build
mkdir -p %{_vpath_builddir}
pushd %{_vpath_builddir}
tar xf %SOURCE1
popd

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DINSTALL_LIB_DIR=%{_lib} \
       -DENABLE_ECCODES_OMP_THREADS=ON \
       -DENABLE_JPG=ON \
       -DENABLE_PNG=ON \
       -DENABLE_FORTRAN=ON \
       -DENABLE_NETCDF=ON \
       -DECCODES_INSTALL_EXTRA_TOOLS=ON \
       -DENABLE_EXTRA_TESTS=ON \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
       -DECCODES_SOVERSION=%{so_version} \
       -DECCODES_SOVERSION_F90=%{so_version_f90} \
       -DCMAKE_Fortran_FLAGS="-fPIC"
%cmake_build
cp fortran/eccodes_constants.h %{_vpath_builddir}/fortran/
cp fortran/grib_api_constants.h %{_vpath_builddir}/fortran/
%install
%cmake_install
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}/
rm %{buildroot}%{_datadir}/%{name}/definitions/installDefinitions.sh
mkdir -p %{buildroot}%{_datadir}/doc/%{name}/
cp -r html %{buildroot}%{_datadir}/doc/%{name}/
mkdir -p %{buildroot}%{_datadir}/doc/%{name}/examples/C
cp examples/C/*.c %{buildroot}%{_datadir}/doc/%{name}/examples/C
mkdir -p %{buildroot}%{_datadir}/doc/%{name}/examples/F90
cp examples/F90/*.f90 %{buildroot}%{_datadir}/doc/%{name}/examples/F90
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} \
%{SOURCE2} %{_vpath_builddir}/bin \
           %{_vpath_builddir}/man
mkdir -p %{buildroot}%{_datadir}/man/man1
cp %{_vpath_builddir}/man/*.1 %{buildroot}%{_datadir}/man/man1
chmod 644 AUTHORS LICENSE
sed -i 's|^libs=.*$|libs=-L${libdir} -leccodes|g' %{buildroot}/%{_libdir}/pkgconfig/eccodes.pc
sed -i 's|^libs=.*$|libs=-L${libdir} -leccodes_f90 -leccodes|g' %{buildroot}/%{_libdir}/pkgconfig/eccodes_f90.pc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
export LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest -V -E eccodes_download
%files -f %{oreon_filedir}/main.list
%files -n eccodes-devel -f %{oreon_filedir}/eccodes-devel.list
%files -n eccodes-data -f %{oreon_filedir}/eccodes-data.list
%files -n eccodes-doc -f %{oreon_filedir}/eccodes-doc.list

%changelog

%autochangelog
