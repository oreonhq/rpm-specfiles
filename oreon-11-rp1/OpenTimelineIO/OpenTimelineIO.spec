%global source1_hash 2d2601a82d2d3b7e143a3c8d43ef616671391034bc46891a9816b79cf2d3e7a8
%global source0_hash bcb516a43a962dac0cde3e1f9da634c1fd409915d499ff8f3ce6f738a4637d72
%bcond python 0
%global rjcommit 24b5e7a8b27f42fa16b96fc70aade9106cf7102f
Name:           OpenTimelineIO
Version:        0.18.1
Release:        1%{?dist}
Summary:        Editorial timeline information API
License:        Apache-2.0 AND MIT
URL:            https://github.com/AcademySoftwareFoundation/OpenTimelineIO
Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Tencent/rapidjson/archive/%{rjcommit}/rapidjson-%{rjcommit}.tar.gz
Patch0:         cmake-install.patch
%if %{with python}
%endif
Provides:       bundled(rapidjson) = %{rjcommit}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Imath)
BuildRequires:  gcc-c++
# /oreon:deps
%description
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Imath)
%description devel
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%if %{with python}
%package -n python3-%{name}
Summary:        Python interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package tools
Summary:       Additional tools for %{name}
Requires:      python3-%{name} = %{version}-%{release}
%description tools
Additional tools for %{name}.

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a1
# Imath: system version used via OTIO_FIND_MATH
# rapidjson: snapshot needed for APIs added since last release
find src/deps/{Imath,rapidjson} -delete
mv rapidjson-%{rjcommit} src/deps/rapidjson

%build

%cmake \
  -DOTIO_CXX_INSTALL=ON \
%if %{with python}
  -DOTIO_PYTHON_INSTALL=ON \
  -DOTIO_PYTHON_INSTALL_DIR=%{python3_sitearch} \
%endif
  -DOTIO_FIND_IMATH=ON \
  -DOTIO_SHARED_LIBS=ON \
  -DOTIO_DEPENDENCIES_INSTALL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles OpenTimelineIO-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n OpenTimelineIO-devel -f %{oreon_filedir}/OpenTimelineIO-devel.list

%changelog

%autochangelog
