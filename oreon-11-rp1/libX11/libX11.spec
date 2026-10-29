%global source0_hash fa026f9bb0124f4d6c808f9aef4057aad65e7b35d8ff43951cef0abe06bb9a9a
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libX11
Version: 1.8.12
Release: 1%{?dist}
Summary: X11 client library
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/libX11-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: xorgproto
BuildRequires: libXau-devel = 1.0.12-1%{?dist}
BuildRequires: libxcb-devel = 1.17.0-1%{?dist}
BuildRequires: pkgconf
%endif

%description
X11 client library

%package devel
Summary: X11 client library
Requires: libX11%{?_isa} = %{version}-%{release}

%description devel
X11 client library

%prep
%oreon_sha256
%autosetup -n libX11-1.8.12 -p1

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
