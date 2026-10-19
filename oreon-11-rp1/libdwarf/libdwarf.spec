%global source0_hash bde13d1c49be6f2467326a6e0b3919247471455d16eefc3c6be26c7d4baca36a
Name:          libdwarf
Epoch:         1
Version:       2.3.3
Release:        1%{?dist}
Summary:        Library to access the DWARF Debugging file format
License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
URL:           https://www.prevanders.net/dwarf.html
Source0:        https://www.prevanders.net/%{name}-%{version}.tar.xz
Patch:         libdwarf-both.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  python3
# /oreon:deps
%description
Library to access the DWARF debugging file format which supports
source level debugging of a number of procedural languages, such as C, C++,
and Fortran.  Please see http://www.dwarfstd.org for DWARF specification.

%package devel
Summary:       Library and header files of libdwarf
License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:      %{name} = %{epoch}:%{version}-%{release}
%description devel
Development package containing library and header files of libdwarf.

%package static
Summary:       Static libdwarf library
License:       LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:      %{name}-devel = %{epoch}:%{version}-%{release}
%description static
Static libdwarf library.

%package tools
Summary:       Tools for accessing DWARF debugging information
License:       GPL-2.0-only AND BSD-2-Clause-FreeBSD
Requires:      %{name} = %{epoch}:%{version}-%{release}
%description tools
C++ version of dwarfdump (dwarfdump2) command-line utilities 
to access DWARF debug information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddwarfgen=true --default-library=both
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libdwarf-devel -f %{oreon_filedir}/libdwarf-devel.list
%files -n libdwarf-static -f %{oreon_filedir}/libdwarf-static.list
%files -n libdwarf-tools -f %{oreon_filedir}/libdwarf-tools.list

%changelog

%autochangelog
