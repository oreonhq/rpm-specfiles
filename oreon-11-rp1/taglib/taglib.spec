%global source0_hash 7349f6fd942418bc7009ebe743eb7c9d055f02921ec56fa436ec25007c47fd38

%bcond_with mingw
%bcond_with tests
%bcond_with doc

%undefine __cmake_in_source_build
%global apidocdir __api-doc_fedora

%global common_description %{expand:
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.}

Name:       taglib
Summary:    Audio Meta-Data Library
Version:    2.3
Release:    2%{?dist}
License:    (LGPL-2.1-only OR MPL-1.1) AND BSD-2-Clause AND LGPL-2.1-only
URL:        https://taglib.github.io/
Source0:    https://taglib.github.io/releases/taglib-%{version}%{?beta}.tar.gz

Patch0:     taglib-2.2.1-multilib.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: utf8cpp-devel
BuildRequires: zlib-devel
%if %{with tests}
BuildRequires: cppunit-devel
%endif
%if %{with doc}
BuildRequires: doxygen
BuildRequires: graphviz
%endif

%description
%{common_description}

%package doc
Summary: API Documentation for %{name}
BuildArch: noarch

%description doc
This is API documentation generated from the TagLib source code.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%if ! %{with doc}
Obsoletes: %{name}-doc < %{version}-%{release}
%endif

%description devel
Files needed when building software with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n taglib-%{version}%{?beta} -p1

%build
%cmake \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON \
%endif
  -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%if %{with doc}
%cmake_build --target docs
%endif

%install
%cmake_install

%if %{with doc}
rm -fr %{apidocdir}
mkdir %{apidocdir}
cp -a %{_vpath_builddir}/doc/html/ %{apidocdir}/
ln -s html/index.html %{apidocdir}
find %{apidocdir} -name '*.md5' | xargs rm -fv
%endif

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion taglib)" = "%{version}"
test "$(pkg-config --modversion taglib_c)" = "%{version}"
%if %{with tests}
%ctest
%endif

%files
%doc AUTHORS CHANGELOG.md
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libtag.so.2*
%{_libdir}/libtag_c.so.2*

%files devel
%doc examples
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/cmake/taglib/
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_libdir}/pkgconfig/taglib.pc
%{_libdir}/pkgconfig/taglib_c.pc

%if %{with doc}
%files doc
%doc %{apidocdir}/*
%endif

%changelog
* Wed Jun 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-2
- bump to 2.3 for libtag.so.2
