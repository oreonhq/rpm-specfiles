%global source0_hash 2540302a1844ad2b2b501977abecfa850f265f97b78f065a712ab4074a89f5b5

Summary:       A library of functions for manipulating PNG image format files
Name:          libpng
Epoch:         2
Version:       1.6.59
Release:       1%{?dist}
License:       zlib
URL:           http://www.libpng.org/pub/png/

Source0:        https://github.com/glennrp/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       pngusr.dfa

Patch0:        libpng-multilib.patch

BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: autoconf automake libtool
BuildRequires: cmake

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary:       Development tools for programs to manipulate PNG image format files
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      zlib-devel%{?_isa} pkgconfig

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install
the libpng package.

%package static
Summary:       Static PNG image format file library
Requires:      %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static
The libpng-static package contains the statically linkable version of libpng.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary:       Tools for PNG image format file library
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
The libpng-tools package contains tools used by the authors of libpng.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
# Provide pngusr.dfa for build.
cp -p %{SOURCE1} .

%patch -P0 -p1

%build
%cmake -DDFA_XTRA=pngusr.dfa
%cmake_build

%install
%cmake_install

# We don't ship .la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
%ctest

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libpng16.so.*
%{_mandir}/man5/*

%files devel
%doc libpng-manual.txt example.c TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%dir %{_libdir}/libpng/
%{_libdir}/libpng/*.cmake
%{_libdir}/pkgconfig/libpng*.pc
%{_libdir}/cmake/PNG/
%{_mandir}/man3/*

%files static
%{_libdir}/libpng*.a

%files tools
%{_bindir}/pngfix

%changelog
%autochangelog
