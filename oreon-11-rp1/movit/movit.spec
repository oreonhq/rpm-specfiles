%global source0_hash b33073b705f0ccb6ac4942cf51151515407b40bb4e9a2dd0228c1c2cb1fbc11a

%if 0%{?el9}
# Disable LTO for ppc64le to work around build failures
# Cf. https://bugzilla.redhat.com/show_bug.cgi?id=1996330
%ifarch ppc64le
%global _lto_cflags %{nil}
%endif
%endif

Name:           movit
Version:        1.7.1
Release:        8%{?dist}
Summary:        GPU video filter library
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            https://movit.sesse.net
Source0:        https://movit.sesse.net/%{name}-%{version}.tar.gz
Source1:        COPYING
Patch0:         gcc_erase_signature.patch
Patch1:         data.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(microbenchmark)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  gtest-devel
Requires:       %{name}-data = %{version}-%{release}

%description
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the Movit shared library.

%package devel
Summary:        Development files for the Movit GPU video filter library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the development files (library and header files).

%package        data
Summary:        Data files for the Movit GPU video filter library
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    data
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the architecture-independent data files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE1} .
%if 0%{?rhel} && 0%{?rhel} < 8
%patch -P0 -p1
%endif
%patch -P1 -p1

%build
#./autogen.sh
aclocal
libtoolize --install --copy
autoconf
%configure --disable-static
%make_build TESTS=

%install
sed -i 's/-m 0644 libmovit.la/libmovit.la/' Makefile
%make_install

rm %{buildroot}%{_libdir}/libmovit.la

#check
# skipped test suite due src/gtest-all.cc is missing
# make check

%ldconfig_scriptlets

%files
%doc README NEWS
%license COPYING
%{_libdir}/libmovit.so.*

%files data
%{_datadir}/movit/

%files devel
%{_libdir}/libmovit.so
%{_includedir}/movit/
%{_libdir}/pkgconfig/movit.pc

%changelog
%autochangelog
