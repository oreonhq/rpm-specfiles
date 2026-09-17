%global source0_hash 7d959253d5e34aeb16caa14d4889ac06486d19821216743142733a32ee7b4935

%if 0%{?el8}
%undefine __cmake_in_source_build
%endif

Name:           eccodes
Version:        2.46.0
Release:        1%{?dist}
Summary:        WMO data format decoding and encoding

# force the shared libraries to have these so versions
%global so_version       0.1
%global so_version_f90   0.1

# note that the test_data package provided on the ECMWF version
# is unversioned, so use the download date to discriminate
# between different versions.
%global datapack_date    20250202

# latest fedora-38/rawhide grib_api version is 1.27.0-18
# but this version number is to be updated as soon as we know
# what the final release of grib_api by upstream will be.
# latest upstream grib_api release is 1.28.0 (05-Dec-2018)
# as was written on https://confluence.ecmwf.int/display/GRIB/Home
# (Note that this page is no longer available, 17-Oct-2020)
%global final_grib_api_version 1.28.1-1%{?dist}

%ifarch i686 ppc64 armv7hl
  %global obsolete_grib_api 0
%else
  %global obsolete_grib_api 1
%endif

# license remarks:
# Most of eccodes is licensed ASL 2.0 (which is identical to the SPDX
# identifier Apache-2.0) but a special case must be noted.
# These 2 files:
#     src/grib_yacc.c
#     src/grib_yacc.h
# contain a special exception clause that allows them to be
# relicensed if they are included in a larger project

License:        Apache-2.0

URL:            https://confluence.ecmwf.int/display/ECC/ecCodes+Home
Source0:        https://confluence.ecmwf.int/download/attachments/45757960/eccodes-%{version}-Source.tar.gz

# note: this data package is unversioned upstream but still it is updated
# now and then so rename the datapack using the download date
# to make it versioned in fedora
Source1:        https://get.ecmwf.int/repository/test-data/eccodes/eccodes_test_data.tar.gz#/eccodes_test_data_%{datapack_date}.tar.gz

# a custom script to create man pages
Source2:        eccodes_create_man_pages.sh

# Add soversion to the shared libraries, since upstream refuses to do so
# https://jira.ecmwf.int/browse/SUP-1809
Patch1:         eccodes-soversion.patch

# note that the requests to make the other issues public are filed here:
# https://jira.ecmwf.int/browse/SUP-2073
# (and again, unfortunately this issue is not public)

BuildRequires:  cmake >= 3.18
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  /usr/bin/git
BuildRequires:  jasper-devel
BuildRequires:  openjpeg2-devel >= 2.5.2
BuildRequires:  libpng-devel
BuildRequires:  netcdf-devel
BuildRequires:  libaec-devel
BuildRequires:  libaec-static

# For tests
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(File::Compare)

# For creation of man pages
BuildRequires:  help2man

# The data is needed by the library and all tools provided in the main package.
# The other way around, the data package could be installed without
# installing the base package. It will probably be pretty useless,
# unless a user wishes to read and study all these grib and bufr
# file format definitions.
Requires: %{name}-data = %{version}-%{release}

# NOTE: upstream writes:
# """
# For GRIB encoding and decoding, the GRIB-API functionality is provided
# fully in ecCodes with only minor interface and behaviour changes.
# Interfaces for C, Fortran 90 and Python are all maintained as in GRIB-API.
# However, the GRIB-API Fortran 77 interface is no longer available.
# """
# Therefore, since the library name and pkg-config file content changes
# and fortran77 support was removed, this replacement package cannot be
# considered compatible enough and no Provides can be defined.
#
# Furthermore, upstream writes:
# "Please note that GRIB-API support is being discontinued at the end of 2018."
# So the old grib_api will need to be obsoleted.

%if 0%{obsolete_grib_api}
# as stated in the note above, setting provides seems not correct here
# Provides:       grib_api = %%{final_grib_api_version}
Obsoletes:      grib_api < %{final_grib_api_version}
%endif

# as explained in bugzilla #1562066
ExcludeArch: i686

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
# Provides:   grib_api-devel = %%{final_grib_api_version}
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

# a sub package grib_api-doc did not exist
# so no obsoletes needed here

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

# In response to change proposal CMake 4.0 (rhbz#2380563)
# upstream support has been requested in this feature request:
# https://github.com/ecmwf/eccodes/issues/409
export CMAKE_POLICY_VERSION_MINIMUM=3.5

#-- The following features are disabled by default and not switched on:
#
# * MEMFS , Memory based access to definitions/samples
# * MEMORY_MANAGEMENT , enable memory management
# * ALIGN_MEMORY , enable memory alignment
# * GRIB_TIMER , enable timer
# * ECCODES_THREADS , enable POSIX threads
#
#-- The following features are disabled by default and switched on:
# * PNG , support for PNG decoding/encoding
# * ECCODES_OMP_THREADS , enable OMP threads
# * EXTRA_TESTS , enable extended regression testing
# * EXTRA_TOOLS , enable the installation of tools for the METAR format

#-- The following features are set to AUTO by default and
#   explicitely switched on to ensure they don't vanish unnoticed
#   in case of dependency problems during the build:
# * ENABLE_JPG
# ^ ENABLE_FORTRAN
# * ENABLE_NETCDF
#   NetCDF is only needed to create the grib_to_netcdf convert tool
#
#-- Also add an explicit option to not use rpath
#
# Note: -DINSTALL_LIB_DIR=%%{_lib} is needed because otherwise
#        the library so files get installed in /usr/lib in stead
#        of /usr/lib64 on x86_64.

# added -DCMAKE_Fortran_FLAGS="-fPIC"
# because the koji build crashes with the error that it needs this setting
# when I try to build for armv7hl (other archs do not complain ......)
# I have no idea what causes this difference in behaviour.

# Note: the option:
#      -DENABLE_MEMFS=ON
# reformats the definition tables into big binary blobs to be included
# in the c code.
# This reduces the install size from 160MB to 72MB (in version 2.45.0),
# but it also makes it impossible for users to create and use their own
# local table definitions. Therefore, to allow flexibility on the users
# side, this option is not activated at the moment.

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

# note the final '..' is no longer needed to the cmake call.
# this is now hidden in the %%cmake macro

%cmake_build

# copy some include files to the build dir
# that are otherwise not found when creating the debugsource sub-package
cp fortran/eccodes_constants.h %{_vpath_builddir}/fortran/
cp fortran/grib_api_constants.h %{_vpath_builddir}/fortran/

%install
%cmake_install
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}/

# remove a script that does not belong in the doc section
# and triggers an rpmlint error
rm %{buildroot}%{_datadir}/%{name}/definitions/installDefinitions.sh
# by the way, is there a way in the files section to include a directory
# but exclude a given file in it? I could not find such a trick.

# copy the html documentation to the install directory
mkdir -p %{buildroot}%{_datadir}/doc/%{name}/
cp -r html %{buildroot}%{_datadir}/doc/%{name}/

# copy the example scripts/programs to the install directory
# but dont copy the shell scripts and Makefiles, since these
# are part of the cmake test setup and not usefull as example.
# Use %%{_datadir}/doc/%%{name}/ rather than %%{_datadir}/%%{name}/
# otherwise the rpmbuild will create a lot off unnecessary
# pyc and pyo files.

mkdir -p %{buildroot}%{_datadir}/doc/%{name}/examples/C
cp examples/C/*.c %{buildroot}%{_datadir}/doc/%{name}/examples/C
mkdir -p %{buildroot}%{_datadir}/doc/%{name}/examples/F90
cp examples/F90/*.f90 %{buildroot}%{_datadir}/doc/%{name}/examples/F90

# create man pages for the tools that support the --help option
# since upstream does not provide them.
# Source2 points to the script eccodes_create_man_pages.sh
# used to generate the man pages.
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} \
%{SOURCE2} %{_vpath_builddir}/bin \
           %{_vpath_builddir}/man

# copy the created man pages to the install directory
mkdir -p %{buildroot}%{_datadir}/man/man1
cp %{_vpath_builddir}/man/*.1 %{buildroot}%{_datadir}/man/man1

# Fix permissions
chmod 644 AUTHORS LICENSE

# also not needed for x86_64
# maybe they fixed it for all archs?
#%%ifarch i686 armv7hl
#  # pass (nothing to do)
#%%else
#  # it seems pkgconfig files end up in lib in stead of lib64 now
#  # so move them to the right place
#  mv %%{buildroot}/%%{_usr}/lib/pkgconfig/ \
#     %%{buildroot}/%%{_libdir}/pkgconfig/
#%%endif

# It seems the cmake options
# -DCMAKE_SKIP_RPATH=TRUE
# -DCMAKE_SKIP_INSTALL_RPATH=TRUE
# have no effect on the generated *.pc files.
# These still contain an rpath reference, so patch them and remove 
# the rpath using sed
sed -i 's|^libs=.*$|libs=-L${libdir} -leccodes|g' %{buildroot}/%{_libdir}/pkgconfig/eccodes.pc
sed -i 's|^libs=.*$|libs=-L${libdir} -leccodes_f90 -leccodes|g' %{buildroot}/%{_libdir}/pkgconfig/eccodes_f90.pc

%ldconfig_scriptlets

#####################################################
%check

# notes:
# * the LD_LIBRARY_PATH setting is required to let the tests
#   run inside the build dir, otherwise they are broken due to
#   the removal of rpath
# * the LIBRARY_PATH setting is needed te let the
#   'eccodes_t_bufr_dump_(de|en)code_C' tests run.
#   These tests compile on the fly generated C code, and
#   without this setting the loader does not find the libraries.
# * exporting the 2 environment variables below is required!
#   without export the values are not provided to the executed tests! 
#   (probably because the %%ctest macro starts with a blank line)
# * disabling 6 tests with eccodes_download in their name is required
#   since the fedora build environment does not have internet access
#   (these 6 tests where introduced in version 2.46.0)

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
export LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest -V -E eccodes_download

%files
%license LICENSE
%doc ChangeLog AUTHORS NEWS NOTICE
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/*
%{_fmoddir}/%{name}.mod
%{_fmoddir}/grib_api.mod
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_f90.pc
%{_libdir}/*.so
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/definitions/
%{_datadir}/%{name}/samples/
%{_datadir}/%{name}/ifs_samples/
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/1.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/110.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/174.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/2.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/20.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/21.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/221.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/222.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/223.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/225.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/226.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/227.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/228.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/229.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/230.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/231.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/232.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/233.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/234.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/235.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/236.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/237.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/31.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/41.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/42.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/local/8/78/64.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/10.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/11.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/12.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/7.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/8.rpmmoved
%ghost %{_datadir}/%{name}/definitions/bufr/tables/0/wmo/9.rpmmoved

%files doc
%doc %{_datadir}/doc/%{name}/

%changelog
%autochangelog
