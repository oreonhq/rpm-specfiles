%global source0_hash 8b37ce4265a82bebf0e796e21a769e56fdbf8420411ccbe3fafee4ed75b6a6e5
%global pypi_name coincurve
%undefine _debugsource_packages
Name:          python-%{pypi_name}
Version:       21.0.0
Release:        1%{?dist}
Summary:        Cross-platform Python bindings for libsecp256k1
License:       MIT and (MIT or Apache-2.0)
URL:           https://github.com/ofek/coincurve
VCS:           git:%{url}.git
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name/%{pypi_name-%{version}.tar.gz
Patch:         python-coincurve-0001-Relax-dependency.patch
Patch:         python-coincurve-0002-Customize-CMake-defaults.patch
Patch:         python-coincurve-0003-Don-t-strip-binary.patch
Patch:         python-coincurve-0004-Don-t-override-C-XX-FLAGS.patch
Requires: python3-cffi
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libsecp256k1-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-pytest
# /oreon:deps
%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:        Cross-platform Python bindings for libsecp256k1
%description -n python3-%{pypi_name}
%{summary}.

%prep

%autosetup -p1
rm -rf docs/.scripts docs/.snippets docs/assets
rm hatch_build.py
sed -i '/^\[tool\.hatch\.build\.targets\.wheel\.hooks\.custom\]$/d' pyproject.toml

%build -p

export COINCURVE_VENDOR_CFFI=0
%install
%pyproject_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-coincurve -f %{oreon_filedir}/python3-coincurve.list

%changelog

%autochangelog
