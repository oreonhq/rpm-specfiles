%global source0_hash 2d8f2c47c40476d6e8cea9d878f6601d04f6d5642b47018eaafa9e9f833f3690

Name:           OpenColorIO
Version:        2.4.2
Release:        8%{?dist}
Summary:        Enables color transforms and image display across graphics apps

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opencolorio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/v%{version}/%{name}-%{version}.tar.gz
# Change MZ_VERSION_BUILD to hex
# https://github.com/AcademySoftwareFoundation/OpenColorIO/pull/1954
Patch0:         OpenColorIO-mzver.patch

# OpenVDB no longer builds on i686
ExcludeArch:    i686

# OIIO is only built for these arches due to Libraw
%if 0%{?rhel} >= 8 && 0%{?rhel} < 9
ExclusiveArch:  x86_64 ppc64le
%endif

# Utilities
BuildRequires:  cmake gcc-c++
BuildRequires:  help2man
BuildRequires:  python3
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-markupsafe
BuildRequires:  python3-setuptools

# Libraries
BuildRequires:  cmake(OpenEXR)
BuildRequires:  boost-devel
BuildRequires:  expat-devel
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  imath-devel
BuildRequires:  libX11-devel libXmu-devel libXi-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel
BuildRequires:  minizip-ng-compat-devel >= 3.0.6
BuildRequires:  opencv-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  pystring-devel
BuildRequires:  zlib-devel

#######################
# Unbundled libraries #
#######################
BuildRequires:  lcms2-devel
BuildRequires:  yaml-cpp-devel >= 0.7.0

%if 0%{?docs}
BuildRequires:  doxygen
BuildRequires:  python3-breathe
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx-press-theme
BuildRequires:  python3-sphinx-tabs
BuildRequires:  python3-testresources
%endif

%if ! 0%{?docs}
# upgrade path for when/if docs are not included
Obsoletes: %{name}-doc < %{version}-%{release}
%endif

%description
OCIO enables color transforms and image display to be handled in a consistent
manner across multiple graphics applications. Unlike other color management
solutions, OCIO is geared towards motion-picture post production, with an
emphasis on visual effects and animation color pipelines.

%package tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools for %{name}.

%package doc
BuildArch:      noarch
Summary:        API Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
API documentation for %{name}.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?relcan:-rc%{relcan}}

# Fedora maps minzip-ng back to minizip so work around it here:
sed -i "s/minizip-ng/minizip/g" src/OpenColorIO/OCIOZArchive.cpp src/apps/ocioarchive/main.cpp

%build
%cmake -DCMAKE_CXX_STANDARD=17 \
       -DOCIO_BUILD_DOCS=%{?docs:ON}%{?!docs:OFF} \
       -DOCIO_BUILD_TESTS=%{?tests:ON}%{?!tests:OFF} \
	   -DOCIO_USE_HEADLESS=ON \
	   -DOCIO_INSTALL_EXT_PACKAGES=NONE \
%ifnarch x86_64
       -DOCIO_USE_SSE=OFF \
%endif
       -Dminizip-ng_LIBRARY=%{_libdir}/libminizip.so \
	   -Dminizip-ng_INCLUDE_DIR=%{_includedir}/minizip \
	   -Dminizip-ng_DIR=TRUE \
       -DOpenGL_GL_PREFERENCE=GLVND

%cmake_build

%install
%cmake_install

# Remove static libs
find %{buildroot} -type f -name "*.a" -exec rm -f {} \;

# Generate man pages
#pushd %{__cmake_builddir}/src/apps
#mkdir -p %{buildroot}%{_mandir}/man1
#for app in ociobakelut ociocheck ociochecklut ocioconvert ociolutimage ociomakeclf ocioperf ociowrite; do \
#help2man -N -s 1 %{?fedora:--version-string=%{version}} \
#         -o %{buildroot}%{_mandir}/man1/$app.1 \
#         $app/$app
#done
#popd

%check
# Testing gpu fails due to lack of diaplay. Can it be faked?
#ctest

%ldconfig_scriptlets

%files
%license LICENSE
%doc CHANGELOG.md COMMITTERS.md CONTRIBUTING.md GOVERNANCE.md PROCESS.md
%doc README.md SECURITY.md THIRD-PARTY.md
%{_libdir}/*.so.*
%{python3_sitearch}/PyOpenColorIO/

%files tools
%{_bindir}/*
%{_datadir}/ocio/
#{_mandir}/man1/*

%if 0%{?docs}
%files doc
%{_datadir}/doc/%{name}/html/
%endif

%files devel
%{_includedir}/OpenColorIO/
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
