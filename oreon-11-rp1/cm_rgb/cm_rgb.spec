%global source0_hash c49833bb50b4e00bfa6bda60725b0e61557dd50ee175f1b65cef818e6e1dc2b8
%{?!python3_pkgversion:%global python3_pkgversion 3}
%global srcname cm_rgb
Name:           cm_rgb
Version:        0.3.6
Release:        15%{?dist}
Summary:        Utility to control RGB on AMD Wraith Prism
License:        MIT
URL:            https://github.com/gfduszynski/cm-rgb
Source0:        https://files.pythonhosted.org/packages/source/c/cm_rgb/cm_rgb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-hidapi
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Utility to control RGB on AMD Wraith Prism

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
chmod 644 LICENSE README.md

%build

%py3_build
%install
%py3_install
chmod -x %{buildroot}%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/dependency_links.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
