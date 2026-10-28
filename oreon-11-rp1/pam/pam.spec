%global source0_hash 21dbcec6e01dd578f14789eac9024a18941e6f2702a05cf91b28c232eeb26ab0
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pam
Version: 1.7.1
Release: 1%{?dist}
Summary: Pluggable authentication modules
License: BSD-3-Clause
URL: https://github.com/linux-pam/linux-pam
Source0: https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: flex
BuildRequires: libxcrypt-devel
BuildRequires: audit-devel
BuildRequires: libeconf-devel
BuildRequires: libselinux-devel
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: systemd-devel
BuildRequires: gettext-devel
BuildRequires: libdb-devel
BuildRequires: gdbm-devel
BuildRequires: pkgconf
BuildRequires: patchelf
%endif

%description
PAM is the pluggable authentication library.

%package devel
Summary: Pluggable authentication modules
Requires: pam%{?_isa} = %{version}-%{release}

%description devel
PAM is the pluggable authentication library.

%prep
%oreon_sha256
%autosetup -n Linux-PAM-%{version} -p1

%build
%oreon_meson -Ddocs=disabled -Delogind=disabled
%oreon_meson_build

%install
%oreon_meson_install
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
