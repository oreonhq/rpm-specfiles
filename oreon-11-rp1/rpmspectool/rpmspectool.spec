%global source0_hash 4a9eae6169a6ae8a56c6de0985935dad05d3cb087fc5b92f06d9739e215b0327
%bcond testcoverage 0
Name:           rpmspectool
Version:        1.100.0
Release:        1%{?dist}
Summary:        Utility for dealing with RPM spec files
License:        GPL-3.0-or-later
URL:            https://github.com/nphilipp/rpmspectool
Source0:        https://files.pythonhosted.org/packages/source/r/rpmspectool/rpmspectool-%{version}.tar.gz
BuildArch:      noarch
%if %{with testcoverage}
%endif
Requires:       python3-%{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpmspectool = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        Utility for dealing with RPM spec files
%description -n python3-%{name}

This package contains the Python package used by the rpmspectool CLI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%if %{without testcoverage}
cat << PYTESTINI > pytest.ini
[pytest]
addopts =
PYTESTINI
%endif

%build

%pyproject_wheel
%install
%pyproject_install
sed -i -e 's|^\(.*/COPYING\)|%%license \1|g' %{pyproject_files}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp shell-completions/bash/rpmspectool %{buildroot}%{_datadir}/bash-completion/completions/
%oreon_autofiles main usr/lib/python3*/site-packages/rpmspectool* usr/lib64/python3*/site-packages/rpmspectool* usr/bin/*

%check

%pytest -v
%files
%files -n python3-rpmspectool -f %{oreon_filedir}/python3-rpmspectool.list

%changelog

%autochangelog
