%global source0_hash c9cc77c7c560c543135edc555af609d5619dbef011997e988ce40a3d75d86088
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: file
Version: 5.46
Release: 1%{?dist}
Summary: File type identification library
License: BSD-2-Clause-Darwin
URL: https://www.darwinsys.com/file/
Source0: https://astron.com/pub/file/file-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
%endif

%description
File type identification library

%package devel
Summary: File type identification library
Requires: file%{?_isa} = %{version}-%{release}

%description devel
File type identification library

%prep
%oreon_sha256
%autosetup -n file-5.46 -p1

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
