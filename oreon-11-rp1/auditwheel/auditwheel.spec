%global source0_hash d007c4fd8c9c4b5113690ab0b159e05c5aa9b2d31b69efc40875826cc095594b
Name:           auditwheel
Version:        6.8.2
Release:        1%{?dist}
Summary:        Cross-distribution Linux wheels auditing and relabeling
License:        MIT
URL:            https://github.com/pypa/auditwheel
Source0:        https://files.pythonhosted.org/packages/source/a/auditwheel/auditwheel-%{version}.tar.gz
BuildArch:      noarch
Requires:       patchelf >= 0.14
%global wheel_version 0.36.2
Provides:       bundled(python3dist(wheel)) = %{wheel_version}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools_scm) >= 8
Requires:       python3-auditwheel = %{version}-%{release}
# /oreon:deps
%description
auditwheel is a command-line tool to facilitate the creation of Python wheel
packages for Linux (containing pre-compiled binary extensions)
that are compatible with a wide variety of Linux distributions,
consistent with the PEP 600 manylinux_x_y, PEP 513 manylinux1,
PEP 571 manylinux2010 and PEP 599 manylinux2014 platform tags.

auditwheel show: shows external shared libraries that the wheel depends on
(beyond the libraries included in the manylinux policies),
and checks the extension modules for the use of versioned symbols that exceed
the manylinux ABI.

auditwheel repair: copies these external shared libraries into the wheel
itself, and automatically modifies the appropriate RPATH entries such that
these libraries will be picked up at runtime.
This accomplishes a similar result as if the libraries had been statically
linked without requiring changes to the build system.
Packagers are advised that bundling,
like static linking, may implicate copyright concerns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# This project uses patchelf, packaged for pip -- we'll use the native one instead
sed -E -i 's/(, ?)?\"patchelf\"//' pyproject.toml

# docker is only used for integration testing we don't run
sed -E -i 's/(, ?)?\"docker\"//' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest -v tests/unit
export %{py3_test_envvars}
%{buildroot}%{_bindir}/auditwheel --help
%{buildroot}%{_bindir}/auditwheel lddtree %{python3}
test "$(%{python3} -c 'from auditwheel._vendor import wheel; print(wheel.__version__)')" == "%{wheel_version}"
for json in manylinux-policy.json musllinux-policy.json; do
  test -f %{buildroot}%{python3_sitelib}/auditwheel/policy/${json}
done
%files

%changelog

%autochangelog
