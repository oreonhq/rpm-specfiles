%global source0_hash 5db2956a00fbf87d92274cccc92436387ec0c3faadece7413ece1ba1c10c98ff
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: device-mapper
Version: 2.03.31
Release: 1%{?dist}
Summary: Device mapper library
License: LGPL-2.1-or-later
URL: https://sourceware.org/lvm2/
Source0: https://sourceware.org/ftp/lvm2/LVM2.%{version}.tgz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: pkgconf
BuildRequires: patchelf
%endif

%description
device-mapper is the library behind libcryptsetup.

%package devel
Summary: Device mapper library
Requires: device-mapper%{?_isa} = %{version}-%{release}

%description devel
device-mapper is the library behind libcryptsetup.

%prep
%oreon_sha256
%autosetup -n LVM2.%{version} -p1

%build
%oreon_configure --enable-selinux --disable-udev-sync --disable-static
make %{?_smp_mflags} device-mapper

%install
make install_device-mapper DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
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
%license COPYING.LIB

%files devel -f %{_builddir}/%{name}-devel.files
