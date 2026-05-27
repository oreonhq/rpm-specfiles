%global source0_hash c7aa6b17a8a069224321ff94e46fb91a6426828ca78170a879a52cef2597abb7

Name: fsverity-utils
Version: 1.6
Release: 4%{?dist}
Summary: fsverity utilities

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/ebiggers/fsverity-utils
Source0:        https://github.com/ebiggers/fsverity-utils/archive/v1.6/fsverity-utils-1.6.tar.gz

BuildRequires: gcc make
BuildRequires: kernel-headers glibc-headers
BuildRequires: openssl-devel
BuildRequires: openssl-devel-engine
Requires:      libfsverity = %{version}-%{release}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1

%install
%set_build_flags
%make_install PREFIX=/usr LIBDIR=%{_libdir}  CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1
find %{buildroot} -type f -name "*.a" -delete

%files
%doc README.md
%{_bindir}/fsverity
%{_mandir}/man1/fsverity.1.gz

%files -n libfsverity
%license LICENSE
%{_libdir}/libfsverity.so.0

%files devel
%{_includedir}/libfsverity.h
%{_libdir}/libfsverity.so
%{_libdir}/pkgconfig/libfsverity.pc
