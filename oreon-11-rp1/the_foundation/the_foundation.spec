%global source0_hash 0a8ad34ac9d1559462f3a001a7b96aff25f073b475750ed9d3f9a5724fea5989
%bcond check 0
%bcond_without doc
%bcond_with sse41
%global srcname the_Foundation
Name:           the_foundation
Version:        1.13.1
Release:        1%{?dist}
Summary:        Opinionated C11 library for low-level functionality
License:        BSD-2-Clause
URL:            https://codeberg.org/skyjake/the_Foundation
Source0:        https://codeberg.org/skyjake/%{srcname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{url}/pulls/34.patch#/%{name}-glibc-2.43-once_init-compat.diff
%if %{with doc}
%endif
%global soname_version %%(echo %%{version}} | cut -d. -f1)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
%description    devel

The %{name}-devel package contains libraries and header files for
developing applications that use %{srcname}.

%if %{with doc}
%package        doc
Summary:        Documentation for %{srcname}
BuildArch:      noarch
%description    doc

The %{name}-doc package contains the documentation for %{srcname}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake \
%if %{without sse41}
  -DTFDN_ENABLE_SSE41:BOOL=OFF
%else
  %nil
%endif
%cmake_build
%if %{with doc}
doxygen %{srcname}.doxygen
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

for t in \
  archive \
  string \
  test \
  udptest \
; do
  %{__cmake_builddir}/${t}_Foundation
done
%endif
%files -f %{oreon_filedir}/main.list
%files -n the_foundation-devel -f %{oreon_filedir}/the_foundation-devel.list
%files -n the_foundation-doc -f %{oreon_filedir}/the_foundation-doc.list

%changelog

%autochangelog
