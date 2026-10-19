%global source0_hash 7141a8b5bad9d7d965483ac0d75317ac0c21dcee1d13d373693c655f9e3fabe6
%bcond_without shared
%bcond_with examples
%bcond_without tools
%global _vpath_builddir %{_vendor}-%{_target_os}-build
Name: dpdk
Version: 26.07
Release:        1%{?dist}
Epoch: 2
URL: http://dpdk.org
Source0:        https://fast.dpdk.org/rel/dpdk-%{version}.tar.xz
Summary:        Set of libraries and drivers for fast packet processing
License: BSD-3-Clause AND (BSD-3-Clause OR LGPL-2.1-only) AND (BSD-3-Clause OR GPL-2.0-only) AND MIT
ExclusiveArch: x86_64 i686 aarch64 ppc64le riscv64
%ifnarch %{ix86}
%endif
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libarchive-devel
BuildRequires:  libatomic
BuildRequires:  libbpf-devel
BuildRequires:  libfdt-devel
BuildRequires:  libpcap-devel
BuildRequires:  meson
BuildRequires:  numactl-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-pyelftools
BuildRequires:  rdma-core-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary: Data Plane Development Kit development files
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} python3
%if ! %{with shared}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: rdma-core-devel
%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package doc
Summary: Data Plane Development Kit API documentation
BuildArch: noarch
%description doc
API programming documentation for the Data Plane Development Kit.

%if %{with tools}
%package tools
Summary: Tools for setting up Data Plane Development Kit environment
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: kmod pciutils findutils iproute python3-pyelftools
%description tools
%{summary}
%endif

%if %{with examples}
%package examples
Summary: Data Plane Development Kit example applications
BuildRequires: libvirt-devel
BuildRequires: make
%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.
%endif

%define sdkdir  %{_datadir}/%{name}
%define docdir  %{_docdir}/%{name}
%define incdir %{_includedir}/%{name}
%define pmddir %{_libdir}/%{name}-pmds

%pretrans -p <lua>

-- This is to clean up directories before links created
-- See https://fedoraproject.org/wiki/Packaging:Directory_Replacement
directories = {
    "/usr/share/dpdk/mk/exec-env/bsdapp",
    "/usr/share/dpdk/mk/exec-env/linuxapp"
}
for i,path in ipairs(directories) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n dpdk%(awk -F. '{ if (NF > 2) print "-stable" }' <<<%{version})-%{version}

%build

CFLAGS="$(echo %{optflags} -fcommon)" \
%meson --includedir=include/dpdk \
       -Ddrivers_install_subdir=dpdk-pmds \
       -Denable_docs=true \
       -Dmachine=generic \
%if %{with examples}
       -Dexamples=all \
%endif
%if %{with shared}
  --default-library=shared
%else
  --default-library=static
%endif
%meson_build
%install
%meson_install
rm -f %{buildroot}%{docdir}/html/.buildinfo
rm -f %{buildroot}%{docdir}/html/objects.inv
rm -rf %{buildroot}%{docdir}/html/.doctrees
find %{buildroot}%{_mandir}/ -type f -a ! -iname "*rte_*" -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dpdk-devel -f %{oreon_filedir}/dpdk-devel.list
%files -n dpdk-doc -f %{oreon_filedir}/dpdk-doc.list
%files -n dpdk-tools -f %{oreon_filedir}/dpdk-tools.list

%changelog

%autochangelog
