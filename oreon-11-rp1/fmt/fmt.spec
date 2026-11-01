%global source0_hash a2f4a8d51178f954e4c339007f77edd76ba0cb2e36f87a48e5a5403d9be5878f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: fmt
Version: 12.2.0
Release: 1%{?dist}
Summary: Formatting library for C++
License: MIT
URL: https://github.com/fmtlib/fmt
Source0: https://github.com/fmtlib/fmt/releases/download/%{version}/fmt-%{version}.zip

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: unzip

%description
{fmt} is an open-source formatting library providing a fast and safe
alternative to C stdio and C++ iostreams.

%package devel
Summary: Development files for fmt
Requires: fmt%{?_isa} = %{version}-%{release}
Provides: pkgconfig(fmt)
Provides: cmake(fmt)

%description devel
Headers and libraries for developing against fmt.

%prep
%oreon_sha256
%autosetup -n fmt-%{version} -p1

%build
%oreon_cmake -DFMT_DOC=OFF -DFMT_TEST=OFF -DFMT_INSTALL=ON
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
