%global source0_hash 74d0e4dfa3d39ad8939e99bda37f5967aba528211076828464d2777d477fc0fb
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libXau
Version: 1.0.12
Release: 1%{?dist}
Summary: X11 authorisation library
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/libXau-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: xorgproto
BuildRequires: pkgconf
%endif

%description
X11 authorisation library

%package devel
Summary: X11 authorisation library
Requires: libXau%{?_isa} = %{version}-%{release}

%description devel
X11 authorisation library

%prep
%oreon_sha256
%autosetup -n libXau-1.0.12 -p1

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
