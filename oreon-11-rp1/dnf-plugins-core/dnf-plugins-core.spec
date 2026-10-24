%global source0_hash 0f6966a6cb62912cd3520ef2a09ddfcdb48aa3091009f9834526b04f6de9a70a
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: dnf-plugins-core
Version: 4.10.1
Release: 1%{?dist}
Summary: Core plugins for dnf
License: GPL-2.0-or-later
URL: https://github.com/rpm-software-management/dnf-plugins-core
Source0: https://github.com/rpm-software-management/dnf-plugins-core/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
%endif

Requires: python3-dnf-plugins-core = %{version}-%{release}

%description
Core plugins for dnf.

%package -n python3-dnf-plugins-core
Summary: Core plugins for dnf
Requires: python3-dnf
Requires: python3-dateutil
Requires: python3-dbus
Requires: python3-distro
Requires: python3-systemd

%description -n python3-dnf-plugins-core
Core plugins for dnf.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake -DPYTHON_DESIRED=3
%oreon_cmake_build
cmake --build %{_oreon_builddir} --target doc-man

%install
%oreon_cmake_install
%oreon_filelist
mv %{_builddir}/%{name}.files %{_builddir}/python3-dnf-plugins-core.files

%files
%license COPYING

%files -n python3-dnf-plugins-core -f %{_builddir}/python3-dnf-plugins-core.files
