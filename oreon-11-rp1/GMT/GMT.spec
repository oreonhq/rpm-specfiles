%global source0_hash 17c03353839c71a1b11efe4f4e9d5e3f0586a7a7b5f84a298d95ccc35241b001
%undefine __cmake_in_source_build
%global gmthome %{_datadir}/gmt
%global gmtconf %{_sysconfdir}/gmt
%global gmtdoc %{_docdir}/gmt
%bcond_with flexiblas
%bcond_with octave
%if %with octave
%{!?octave_api: %global octave_api %(octave-config -p API_VERSION 2>/dev/null || echo 0)}
%global octave_mdir %(octave-config -p LOCALAPIFCNFILEDIR || echo)
%global octave_octdir %(octave-config -p LOCALAPIOCTFILEDIR || echo)
%endif
%global completion_dir %(pkg-config --variable=completionsdir bash-completion)
%if "%{completion_dir}" == ""
%global completion_dir "/etc/bash_completion.d"
%endif
Name:           GMT
Version:        6.7.0
Release:        1%{?dist}
Summary:        Generic Mapping Tools
License:        LGPL-3.0-or-later
URL:            https://www.generic-mapping-tools.org/
Source0:        https://github.com/GenericMappingTools/gmt/releases/download/%{version}/gmt-%{version}-src.tar.xz
%if %{with flexiblas}
%else
%endif
%if %with octave
%endif
Requires:       gdal
Requires:       GraphicsMagick
Requires:       less
Requires:       %{name}-common = %{version}-%{release}
Requires:       dcw-gmt
Requires:       gshhg-gmt-nc4
Provides:       gmt = %{version}-%{release}
Requires:       xdg-utils
%if %without octave
Obsoletes:      GMT-octave <= 4.5.11
%endif
%global __provides_exclude_from ^%{_libdir}/gmt/.*\\.so$
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  GraphicsMagick
BuildRequires:  bash-completion-devel
BuildRequires:  cmake
BuildRequires:  dcw-gmt
BuildRequires:  fftw-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gdal
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  ghostscript
BuildRequires:  glib2-devel
BuildRequires:  gshhg-gmt-nc4
BuildRequires:  less
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  netcdf-devel
BuildRequires:  pcre2-devel
BuildRequires:  xdg-utils
# /oreon:deps
%description
GMT is an open source collection of ~60 tools for manipulating geographic and
Cartesian data sets (including filtering, trend fitting, gridding, projecting,
etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging
from simple x-y plots via contour maps to artificially illuminated surfaces
and 3-D perspective views.  GMT supports ~30 map projections and transforma-
tions and comes with support data such as coastlines, rivers, and political
boundaries.

GMT is developed and maintained by Paul Wessel and Walter H. F.  Smith with
help from a global set of volunteers, and is supported by the National
Science Foundation.

NOTE: Specific executables that conflict with other Fedora packages have been
removed.  These functions can still be accessed via the GMT wrapper script
with: GMT <function> [args]

%package        common
Summary:        Common files for %{name}
Provides:       gmt-common = %{version}-%{release}
BuildArch:      noarch
%description    common
The %{name}-common package contains common files for GMT (Generic
Mapping Tools) package.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-devel = %{version}-%{release}
Obsoletes:      GMT-static <= 4.5.11
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-doc = %{version}-%{release}
Provides:       %{name}-examples = %{version}-%{release}
Obsoletes:      %{name}-examples < %{version}-%{release}
BuildArch:      noarch
%description    doc
The %{name}-doc package provides the documentation for the GMT (Generic
Mapping Tools) package.

%if %with octave
%package        octave
Summary:        Octave libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}
Provides:       gmt-octave = %{version}-%{release}
%description    octave
The %{name}-octave package contains and Octave interface for developing
applications that use %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gmt-%{version}
%oreon_prep
%build

%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DGSHHG_ROOT=%{_datadir}/gshhg-gmt-nc4 \
  -DGMT_INSTALL_MODULE_LINKS=off \
  -DGMT_INSTALL_TRADITIONAL_FOLDERNAMES=off \
  -DLICENSE_RESTRICTED=LGPL \
%if %with octave
  -DGMT_OCTAVE=BOOL:ON \
%endif
  -DGMT_ENABLE_OPENMP=BOOL:ON \
  -DGMT_USE_THREADS=BOOL:ON \
%if %{with flexiblas}
  -DGMT_EXCLUDE_BLAS=BOOL:ON \
  -DGMT_EXCLUDE_LAPACK=BOOL:ON \
  -DBLAS_LIBRARY=-lflexiblas \
  -DLAPACK_LIBRARY=-lflexiblas \
%endif
  -DBASH_COMPLETION_DIR=%{completion_dir}
%cmake_build
%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{gmtconf}/{mgg,dbase,mgd77}
pushd $RPM_BUILD_ROOT%{gmthome}/
for file in mgg/gmtfile_paths mgd77/mgd77_paths.txt; do
  mv $file $RPM_BUILD_ROOT%{gmtconf}/$file
  ln -s ../../../../../%{gmtconf}/$file $RPM_BUILD_ROOT%{gmthome}/$file
done
popd
mkdir -p $RPM_BUILD_ROOT%{gmthome}/coast
echo %{_datadir}/gshhg-gmt-nc4 > $RPM_BUILD_ROOT%{gmthome}/coast/coastline.conf
find $RPM_BUILD_ROOT -name \*.bat -delete
%ldconfig_scriptlets
%oreon_autofiles GMT-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles GMT-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles GMT-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n GMT-common -f %{oreon_filedir}/GMT-common.list
%files -n GMT-devel -f %{oreon_filedir}/GMT-devel.list
%files -n GMT-doc -f %{oreon_filedir}/GMT-doc.list

%changelog

%autochangelog
