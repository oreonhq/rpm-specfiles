%global source0_hash 6749259e89bbb273f3f5ad7acdffb7c47a2cf8fcaeab4c4695484cef5f4c6b46

# Fedora package review: http://bugzilla.redhat.com/718395

%global __cmake_in_source_build 1

Summary: Library for accessing MusicBrainz servers
Name: libmusicbrainz5
Version: 5.1.0
Release: 29%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: http://www.musicbrainz.org/
Source0:        https://github.com/metabrainz/libmusicbrainz/releases/download/release-5.1.0/libmusicbrainz-%{version}.tar.gz
# Filed upstream as http://tickets.musicbrainz.org/browse/LMB-41
Patch0:        doxygen.patch
Patch1:        0001-Don-t-emit-errors-unless-compiled-for-debug.patch
Patch2:        0002-libxml2-2-12.patch
Patch3:        libmusicbrainz5-cmake-wildcards.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: pkgconfig(neon)
BuildRequires: pkgconfig(libxml-2.0)
Obsoletes: libmusicbrainz4 < 4.0.3-5

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libmusicbrainz4-devel < 4.0.3-5

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libmusicbrainz-%{version}
%patch0 -p1 -b .doxygen
%patch1 -p1 -b .silence-warnings
%patch2 -p1 -b .libxml2
%patch3 -p1 -b .cmake-wildcards

# omit "Generated on ..." timestamps that induce multilib conflicts
# this is *supposed* to be the doxygen default in fedora these days, but
# it seems there's still a bug or 2 there -- Rex
echo "HTML_TIMESTAMP      = NO" >> Doxyfile.cmake


%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%cmake_build --target docs


%install
%cmake_install

rm -f docs/installdox


%ldconfig_scriptlets


%files
%doc AUTHORS.txt COPYING.txt NEWS.txt README.md
%{_libdir}/libmusicbrainz5.so.1*

%files devel
%doc docs/*
%{_includedir}/musicbrainz5/
%{_libdir}/libmusicbrainz5.so
%{_libdir}/pkgconfig/libmusicbrainz5.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-29
- Import
