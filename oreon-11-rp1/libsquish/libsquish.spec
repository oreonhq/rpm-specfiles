%global source0_hash 628796eeba608866183a61d080d46967c9dda6723bc0a3ec52324c85d2147269

%global __cmake_in_source_build 1
Name: libsquish
Version: 1.15
Release: 21%{?dist}
URL: https://sourceforge.net/projects/libsquish/
Summary: Open source DXT compression library
License: MIT
Source0: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Patch0:  libsquish-cmake_install.patch
BuildRequires: gcc-c++ cmake
BuildRequires: make

%package devel
Summary: Development files for Open source DXT compression library
Requires: %{name}%{_isa} = %{version}-%{release}

%description
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

%description devel
The libsquish-devel package contains files needed for developing or compiling
applications which use DXT compression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c libsquish-%{version}

%build
%cmake . -DBUILD_SQUISH_WITH_SSE2=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc ChangeLog.txt
%{_libdir}/*.so.0.0

%files devel
%doc README.txt
%{_libdir}/*.so
%{_includedir}/*

%changelog
%autochangelog
