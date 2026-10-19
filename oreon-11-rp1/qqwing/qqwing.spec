%global source0_hash 1753736c31feea0085f5cfac33143743204f8a7e66b81ccd17e249ecafba802f
Name:           qqwing
Version:        1.3.4
Release:        1%{?dist}
Summary:        Command-line Sudoku solver and generator
License:        GPL-2.0-or-later
URL:            http://qqwing.com/
Source0:        http://qqwing.com/qqwing-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
QQwing is a command-line Sudoku solver and generator.

%package        libs
Summary:        Library for Sudoku solving and generation
%description    libs
libqqwing is a C++ library for solving and generating Sudoku puzzles.

%package        devel
Summary:        Development files for libqqwing
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use libqqwing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qqwing-libs -f %{oreon_filedir}/qqwing-libs.list
%files -n qqwing-devel -f %{oreon_filedir}/qqwing-devel.list

%changelog

%autochangelog
