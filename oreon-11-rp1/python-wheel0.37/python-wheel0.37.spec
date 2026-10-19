%global source0_hash a82516a039e521100ecdef137f9e44249bf6903f9aff7d368e84ac31d60597f5
Name:           python-wheel0.37
Version:        0.37.1
Release:        20%{?dist}
Summary:        A compatibility package with wheel 0.37
License:        MIT
URL:            https://github.com/pypa/wheel
Source0:        https://github.com/pypa/wheel/archive/%{version}/wheel-%{version}.tar.gz
Patch:          tests-normalized-dist-name.patch
Patch:          tests-pep639-license-directory.patch
BuildArch:      noarch
%global python_wheel_name wheel-%{version}-py2.py3-none-any.whl
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wheel0.37 = %{version}-%{release}
# /oreon:deps
%description

%package -n     %{python_wheel_pkg_prefix}-wheel0.37-wheel
Summary:        The Python wheel 0.37.x package packaged as a wheel
Conflicts:      %{python_wheel_pkg_prefix}-wheel-wheel < 1:0.38
Provides:       bundled(python3dist(packaging)) = 20.9
%description -n %{python_wheel_pkg_prefix}-wheel0.37-wheel
A Python wheel of wheel 0.37.x to use with virtualenv
to create virtual environments for Python < 3.7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n wheel-%{version}
sed -Ei '/(pytest|-)-cov/d' setup.cfg

%build

%pyproject_wheel
%install
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{python_wheel_dir}/%{python_wheel_name}}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PYTHONPATH=%{buildroot}%{python_wheel_dir}/%{python_wheel_name}
%pytest
%files
%files -n python-wheel0.37-wheel -f %{oreon_filedir}/python-wheel0.37-wheel.list

%changelog

%autochangelog
