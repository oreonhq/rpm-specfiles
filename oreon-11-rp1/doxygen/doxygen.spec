%global source0_hash a1deed70a6785bbec95a2b2a9e419dc7f7b223a9d74a8644ae611c8e2dcdd354
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: doxygen
Version: 1.18.0
Release: 1%{?dist}
Summary: Documentation system for C, C++ and other languages
License: GPL-2.0-only
URL: https://www.doxygen.nl/
Source0: https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: flex
BuildRequires: bison
BuildRequires: python3
%endif

%description
Doxygen generates documentation from annotated C, C++ and other sources.

%prep
%oreon_sha256
%autosetup -n doxygen-%{version} -p1

%build
%oreon_cmake -Dbuild_doc=OFF -Dbuild_wizard=OFF -Dbuild_search=OFF -Duse_libclang=OFF -DBUILD_SHARED_LIBS=OFF
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
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE
