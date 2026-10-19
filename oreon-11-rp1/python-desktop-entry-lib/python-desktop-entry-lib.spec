%global source0_hash 2189a34f209782bd7c0d392c13093f764e00aacc3b9c49c74a69194cfb9e439b
Name:           python-desktop-entry-lib
Version:        5.0
Release:        1%{?dist}
Summary:        Library for working with .desktop files
License:        BSD-2-Clause
URL:            https://codeberg.org/JakobDev/desktop-entry-lib
Source0:        https://codeberg.org/JakobDev/desktop-entry-lib/archive/%{version}.tar.gz#/desktop-entry-lib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-desktop-entry-lib = %{version}-%{release}
# /oreon:deps
%package -n       python3-desktop-entry-lib+xdg-desktop-portal
Summary:        Metapackage for python3-desktop-entry-lib xdg-desktop-portal extras
Requires:       python3-desktop-entry-lib = %{version}-%{release}
Provides:       python3dist(desktop-entry-lib[xdg-desktop-portal]) = %{version}-%{release}

%description -n python3-desktop-entry-lib+xdg-desktop-portal
Metapackage for python3-desktop-entry-lib xdg-desktop-portal extras.

%description

%package -n python3-desktop-entry-lib
Summary:        Library for working with .desktop files
%description -n python3-desktop-entry-lib

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n desktop-entry-lib-%{version}
# remove coverage options
tomcli set pyproject.toml del tool.pytest.ini_options.addopts

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-desktop-entry-lib usr/lib/python3*/site-packages/desktop_entry_lib* usr/lib64/python3*/site-packages/desktop_entry_lib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/desktop_entry_lib* usr/lib64/python3*/site-packages/desktop_entry_lib* usr/bin/*

%check

%pytest
%files
%files -n python3-desktop-entry-lib -f %{oreon_filedir}/python3-desktop-entry-lib.list

%changelog

%autochangelog
