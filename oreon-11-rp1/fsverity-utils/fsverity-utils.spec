%global source0_hash 94f1bde56bcec0f11d4b2945862b7760b85ef5eb9caff3a44fa8bdc7a639534e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: fsverity-utils
Version: 1.6
Release: 1%{?dist}
Summary: fs-verity userspace library
License: MIT
URL: https://git.kernel.org/pub/scm/fs/fsverity/fsverity-utils.git
Source0: https://mirrors.edge.kernel.org/pub/linux/kernel/people/ebiggers/fsverity-utils/v%{version}/fsverity-utils-%{version}.tar.gz
Patch0: fsverity-utils-openssl-no-engine.patch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: patchelf
%endif

%description
fsverity-utils provides libfsverity.

%package devel
Summary: fs-verity userspace library
Requires: fsverity-utils%{?_isa} = %{version}-%{release}

%description devel
fsverity-utils provides libfsverity.

%prep
%oreon_sha256
%autosetup -n fsverity-utils-%{version} -p1

%build
make %{?_smp_mflags} USE_SHARED_LIB=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{_oreon_cflags} -fPIC" LDFLAGS="%{_oreon_ldflags}"

%install
make install USE_SHARED_LIB=1 DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
