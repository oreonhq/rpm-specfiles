%global source0_hash f245786c831d25150f3dfb4317cda1acc5e3f79a5da4ad073ddca58886569527
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libunistring
Version: 1.3
Release: 1%{?dist}
Summary: Unicode string library
License: LGPL-3.0-or-later
URL: https://www.gnu.org/software/libunistring/
Source0: https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
%endif

%description
Unicode string library

%package devel
Summary: Unicode string library
Requires: libunistring%{?_isa} = %{version}-%{release}

%description devel
Unicode string library

%prep
%oreon_sha256
%autosetup -n libunistring-1.3 -p1

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
%license COPYING.LIB

%files devel -f %{_builddir}/%{name}-devel.files
