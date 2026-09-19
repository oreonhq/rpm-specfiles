%global source0_hash a2305b8d64f6d636e36d669bbdb0ca5445d1345c754b3d61d3f037dad2e5f701

Name:           SOIL
Version:        1.07
Release:        42.20080706%{?dist}
Summary:        Simple OpenGL Image Library

# src/image_helper.{c,h} are MIT-licensed
# Automatically converted from old format: Public Domain and MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT
URL:            http://www.lonesock.net/soil.html
Source0:        http://www.lonesock.net/files/soil.zip
Patch0:         %{name}-link-correctly.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libGL-devel

%description
SOIL is a tiny C library used primarily for uploading textures into OpenGL. It
is based on stb_image version 1.16, the public domain code from Sean Barrett.
The author has extended it to load TGA and DDS files, and to perform common
functions needed in loading OpenGL textures. SOIL can also be used to save and
load images in a variety of formats (useful for loading height maps, non-OpenGL
applications, etc.)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
# workaround for RH bug #912831
mv Simple\ OpenGL\ Image\ Library/* .
rmdir Simple\ OpenGL\ Image\ Library
%patch -P0 -p1 -b .link-correctly

%build
pushd src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -c -fPIC" \
    -f ../projects/makefile/alternate\ Makefile.txt
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd src
make -f ../projects/makefile/alternate\ Makefile.txt install \
    DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}/%{name} \
    INSTALL_FILE="install -pm 644" INSTALL_DIR="install -dp"
popd
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# kill the static library
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib%{name}.a

# fix the library permissions
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.1.07-20071110

%ldconfig_scriptlets

%files
%doc soil.html
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
