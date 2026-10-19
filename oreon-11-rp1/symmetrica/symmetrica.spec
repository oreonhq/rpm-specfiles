%global source0_hash 2efc4b1d047c6fe036453882a20e906ca2bedecae888356c7626447db2b10fd3
%global gittag b24da56820651687cafb611809a4b1b0
Name:           symmetrica
Version:        3.1.0
Release:        4%{?dist}
Summary:        A Collection of Routines for Solving Symmetric Groups
License:        ISC
URL:            https://gitlab.com/-/project/16178617
Source0:        https://gitlab.com/-/project/16178617/uploads/%{gittag}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Symmetrica is a collection of routines, written in the programming
language C, through which the user can readily write his/her own
programs. Routines which manipulate many types of mathematical objects
are available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build

%configure --disable-static --disable-silent-rules
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm doc/Makefile*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd src
make test
export LD_LIBRARY_PATH=$PWD/.libs
./test
cd -
%files -f %{oreon_filedir}/main.list
%files -n symmetrica-devel -f %{oreon_filedir}/symmetrica-devel.list

%changelog

%autochangelog
