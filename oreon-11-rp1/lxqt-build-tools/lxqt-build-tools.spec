%global source0_hash f979142ceee22993da6f5d43a7eea9b0d8ef1ff9812ea9210f514e9a52407f42

%global         project lxqt-build-tools
Name:           lxqt-build-tools
Version:        2.3.0
Release:        2%{?dist}
Summary:        Packaging tools for LXQt

License:        BSD-3-Clause
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{project}/releases/download/%{version}/%{project}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  glib2-devel

Requires:       cmake

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

%files
%license BSD-3-Clause
%doc CHANGELOG README.md
%{_datadir}/cmake/lxqt2-build-tools
%{_bindir}/lxqt2-transupdate

%changelog
%autochangelog
