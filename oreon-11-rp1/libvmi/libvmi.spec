%global source0_hash c5ae380b19ca0d4d89c0e6fb5ed3b39964091f72afdf44512e0f7fadd90b4dbc
%global commit 77a677aa6621927495f1954eded11e601937798b
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251217
%global commit_release .%{commit_date}git%{short_commit}
%global baserelease 15
Name:           libvmi
Version:        0.14.0
Release:        1%{?dist}
Summary:        A library for performing virtual-machine introspection
License:        LGPL-3.0-or-later
URL:            http://libvmi.com/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Patch0001:      libvmi-no_werror.patch
Patch0002:      libvmi-fix-incompatible-pointer.patch
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  xen-devel
# /oreon:deps
%description
LibVMI is a C library with Python bindings that makes it easy to monitor
the low-level details of a running virtual machine by viewing its memory,
trapping on hardware events, and accessing the vCPU registers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities which make use of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    utils
The %{name}-utils package contains a number of programs which make
use of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libvmi-%{commit} -p1

%build

%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build
%install
%cmake_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
find %{buildroot}%{_libdir} -name '*.a' -delete -print
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libvmi-devel -f %{oreon_filedir}/libvmi-devel.list
%files -n libvmi-utils -f %{oreon_filedir}/libvmi-utils.list

%changelog

%autochangelog
