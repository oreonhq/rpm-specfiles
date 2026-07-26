%global source0_hash 84221a3abd5b91228f15f8e6065c335a336237b5738197b75bf419eea561a194

Name:           wimlib
Version:        1.14.5
Release:        1%{?dist}
Summary:        Open source Windows Imaging (WIM) library

# wimlib is dual-licensed (GPL-3.0-or-later/LGPL-3.0-or-later) but is linked to
# libntfs-3g (GPL-3.0-or-later), utilities are GPL-3.0-or-later, some internal
# headers are MIT
License:        GPL-3.0-or-later AND MIT
URL:            https://wimlib.net/
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
# Disable tests requiring mount privileges
Patch0:         %{name}-1.14.3-tests.patch

%if 0%{?fedora} <= 42
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libntfs-3g)

%description
wimlib is a C library for creating, modifying, extracting, and mounting files in
the Windows Imaging Format (WIM files). wimlib and its command-line frontend
'wimlib-imagex' provide a free and cross-platform alternative to Microsoft's
WIMGAPI, ImageX, and DISM.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package utils
Summary:        Tools for creating, modifying, extracting, and mounting WIM files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
This package provides tools for creating, modifying, extracting, and mounting
files in the Windows Imaging Format (WIM files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build
# Ensure build files match the installed Automake version
%if 0%{?fedora} <= 42
autoreconf -fiv
%endif
%configure \
    --disable-silent-rules \
    --disable-static
# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name "*.la" -delete

%check
%make_build check

%files
%doc NEWS.md README.md
%license COPYING COPYING.GPLv3
%{_libdir}/*.so.15*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/*
%{_mandir}/man1/*.1.*

%changelog
%autochangelog
