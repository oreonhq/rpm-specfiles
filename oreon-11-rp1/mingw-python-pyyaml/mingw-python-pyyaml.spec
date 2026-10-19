%global source0_hash d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f
%{?mingw_package_header}
%global mod_name pyyaml
Name:          mingw-python-%{mod_name}
Version:       6.0.3
Release:        2%{?dist}
Summary:        MinGW Windows Python pyyaml library
BuildArch:     noarch
License:       MIT
URL:           https://github.com/yaml/pyyaml
Source0:        https://files.pythonhosted.org/packages/source/p/pyyaml/pyyaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-Cython
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-Cython
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Windows Python %{mod_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python2 %{mod_name} library
%description -n mingw32-python3-%{mod_name}
MinGW Windows Python2 %{mod_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python2 %{mod_name}
%description -n mingw64-python3-%{mod_name}
MinGW Windows Python2 %{mod_name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py
# remove pre-generated file
rm -rf ext/_yaml.c
# we have a patch for Cython 3
sed -i 's/Cython<3.0/Cython/' pyproject.toml

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-pyyaml -f %{oreon_filedir}/mingw32-python3-pyyaml.list
%files -n mingw64-python3-pyyaml -f %{oreon_filedir}/mingw64-python3-pyyaml.list

%changelog

%autochangelog
