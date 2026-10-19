%global source0_hash 14999ff954e820a23af44389b9f7c65f9e58b2f1c0a559f0badd38f9b459aee6
%global         project lxqt-build-tools
Name:           lxqt-build-tools
Version:        2.4.0
Release:        1%{?dist}
Summary:        Packaging tools for LXQt
License:        BSD-3-Clause
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       cmake
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(Qt6Core)
# /oreon:deps
%description
Various packaging tools and scripts for LXQt applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{project}-%{version} -S git_am

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
