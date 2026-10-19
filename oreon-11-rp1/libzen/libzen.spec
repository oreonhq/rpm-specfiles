%global source0_hash eb237d7d3dca6dc6ba068719420a27de0934a783ccaeb2867562b35af3901e2d
Name:           libzen
Version:        0.4.41
Release:        1%{?dist}
Summary:        Shared library for libmediainfo and medianfo*
License:        Zlib
URL:            https://github.com/MediaArea/ZenLib
Source0:        https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Files shared library for libmediainfo and medianfo-*.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation files.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Include files and mandatory libraries for development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ZenLib

#Correct documentation encoding and permissions
sed -i 's/.$//' *.txt
chmod 644 *.txt Source/Doc/Documentation.html

chmod 644 Source/ZenLib/*.h Source/ZenLib/*.cpp \
    Source/ZenLib/Format/Html/*.h Source/ZenLib/Format/Html/*.cpp \
    Source/ZenLib/Format/Http/*.h Source/ZenLib/Format/Http/*.cpp

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
pushd Source/Doc/
    doxygen -u Doxyfile
    doxygen Doxyfile
popd
cp Source/Doc/*.html ./
pushd Project/CMake
    %cmake3
    %cmake3_build
popd
%install
pushd Project/CMake
    %cmake3_install
popd
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libzen-doc -f %{oreon_filedir}/libzen-doc.list
%files -n libzen-devel -f %{oreon_filedir}/libzen-devel.list

%changelog

%autochangelog
