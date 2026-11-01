%global source0_hash 20dbe23e9dbc4ad769078a867ad002c04297a069ff93c95fb72242dd55d4dd6f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: patchelf
Version: 0.19.3
Release: 1%{?dist}
Summary: Modify the dynamic linker and RPATH of ELF executables
License: GPL-3.0-or-later
URL: https://github.com/NixOS/patchelf
Source0: https://github.com/NixOS/patchelf/releases/download/%{version}/patchelf-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
%endif

%description
PatchELF changes the dynamic linker, RPATH and DT_NEEDED entries of ELF
executables and shared libraries.

%prep
%oreon_sha256
%autosetup -n patchelf-%{version} -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
