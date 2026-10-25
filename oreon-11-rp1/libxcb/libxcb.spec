%global source0_hash 599ebf9996710fea71622e6e184f3a8ad5b43d0e5fa8c4e407123c88a59a6d55
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libxcb
Version: 1.17.0
Release: 1%{?dist}
Summary: X protocol C binding
License: MIT
URL: https://xcb.freedesktop.org/
Source0: https://www.x.org/releases/individual/lib/libxcb-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: xcb-proto
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: python3
BuildRequires: pkgconf
%endif

%description
X protocol C binding

%package devel
Summary: X protocol C binding
Requires: libxcb%{?_isa} = %{version}-%{release}

%description devel
X protocol C binding

%prep
%oreon_sha256
%autosetup -n libxcb-1.17.0 -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
