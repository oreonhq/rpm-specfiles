%global source0_hash d8a5222828c3adab70adf69a5583f1d32eb5ece04304f7f8392b6a353aa2228c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libXdmcp
Version: 1.1.5
Release: 1%{?dist}
Summary: X11 Display Manager Control Protocol library
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/libXdmcp-%{version}.tar.xz

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
X11 Display Manager Control Protocol library

%package devel
Summary: X11 Display Manager Control Protocol library
Requires: libXdmcp%{?_isa} = %{version}-%{release}

%description devel
X11 Display Manager Control Protocol library

%prep
%oreon_sha256
%autosetup -n libXdmcp-1.1.5 -p1

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
