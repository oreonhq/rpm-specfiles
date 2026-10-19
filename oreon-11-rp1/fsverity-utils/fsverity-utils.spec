%global source0_hash 686de715e27c30b579d468ab02d7a841ab2a1f553975754fd134ebf627b26149
Name: fsverity-utils
Version: 1.7
Release:        1%{?dist}
Summary:        fsverity utilities
License: LicenseRef-Callaway-BSD
URL:     https://github.com/ebiggers/fsverity-utils
Source0:        https://github.com/ebiggers/fsverity-utils/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:      libfsverity = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-headers
BuildRequires:  kernel-headers
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
# /oreon:deps
%description
This is fsverity, a userspace utility for fs-verity.
fs-verity is a Linux kernel feature that does transparent on-demand
integrity/authenticity verification of the contents of read-only files,
using a hidden Merkle tree (hash tree) associated with the file.
The mechanism is similar to dm-verity, but implemented at the file level
rather than at the block device level. The fsverity utility allows you
to set up fs-verity protected files.

%package -n libfsverity
Summary:          Development package for fsverity-utils
%description -n libfsverity
Library for fsverity-utils.

%package devel
Summary:          Development package for fsverity-utils
Requires:         libfsverity = %{version}-%{release}
Requires:         %{name} = %{version}-%{release}
%description devel
Development package for fsverity-utils. This package includes the
libfsverity header and library files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1
%install
%set_build_flags
%make_install PREFIX=/usr LIBDIR=%{_libdir}  CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1
find %{buildroot} -type f -name "*.a" -delete
%oreon_autofiles libfsverity usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfsverity -f %{oreon_filedir}/libfsverity.list
%files -n fsverity-utils-devel -f %{oreon_filedir}/fsverity-utils-devel.list
