%global source0_hash d2931cdad266e633510f9970e1a2f346055e351bb19f9b78912475b8074c36f6
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libassuan
Version: 3.0.2
Release: 1%{?dist}
Summary: IPC library for GnuPG components
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/libassuan/
Source0: https://www.gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libgpg-error-devel
%endif

%description
IPC library for GnuPG components

%package devel
Summary: IPC library for GnuPG components
Requires: libassuan%{?_isa} = %{version}-%{release}

%description devel
IPC library for GnuPG components

%prep
%oreon_sha256
%autosetup -n libassuan-3.0.2 -p1

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
