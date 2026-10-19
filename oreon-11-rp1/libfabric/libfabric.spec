%global source0_hash 366000427e194d4ce22e272519b608afbebb1fc9915bcf5da924157a8a47fe10
%global __remake_config 0
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%ifarch %{ix86}
%global build_type_safety_c 2
%endif
%endif
Name:           libfabric
Version:        2.7.0
Release:        1%{?dist}
Summary:        Open Fabric Interfaces
License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/ofiwg/libfabric
Source0:        https://github.com/ofiwg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
%ifnarch %{arm}
%endif
%ifarch x86_64
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libibverbs-devel
BuildRequires:  libnl3-devel
BuildRequires:  librdmacm-devel
BuildRequires:  make
# /oreon:deps
%description
OpenFabrics Interfaces (OFI) is a framework focused on exporting fabric
communication services to applications.  OFI is best described as a collection
of libraries and applications used to export fabric services.  The key
components of OFI are: application interfaces, provider libraries, kernel
services, daemons, and test applications.

Libfabric is a core component of OFI.  It is the library that defines and
exports the user-space API of OFI, and is typically the only software that
applications deal with directly.  It works in conjunction with provider
libraries, which are often integrated directly into libfabric.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure --disable-static --disable-silent-rules
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfabric-devel -f %{oreon_filedir}/libfabric-devel.list

%changelog

%autochangelog
