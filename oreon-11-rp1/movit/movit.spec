%global source0_hash 00ac1f8e46c2d3e38c75cbb7a1af0a615751c158c611cb70053094b65ecfe8d5
%if 0%{?el9}
%ifarch ppc64le
%global _lto_cflags %{nil}
%endif
%endif
Name:           movit
Version:        1.7.2
Release:        1%{?dist}
Summary:        GPU video filter library
License:        GPL-2.0-or-later
Url:            https://movit.sesse.net
Source0:        https://movit.sesse.net/%{name}-%{version}.tar.gz
Source1:        COPYING
Patch0:         gcc_erase_signature.patch
Patch1:         data.patch
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
# /oreon:deps
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
%patch -P1 -p1

%build

aclocal
libtoolize --install --copy
autoconf
%configure --disable-static
%make_build TESTS=
%install
sed -i 's/-m 0644 libmovit.la/libmovit.la/' Makefile
%make_install
rm %{buildroot}%{_libdir}/libmovit.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n movit-devel -f %{oreon_filedir}/movit-devel.list
%files -n movit-data -f %{oreon_filedir}/movit-data.list

%changelog

%autochangelog
