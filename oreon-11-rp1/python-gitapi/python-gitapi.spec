%global source0_hash a39ef3541d40d6edc972efb1860af195b540e5870fbc17bb707ac40efa389ab8

Name:           python-gitapi
Version:        1.1.0
Release:        0.a3%{?dist}.38
Summary:        Pure-Python API to git, which uses the command-line interface

License:        MIT
URL:            https://bitbucket.org/haard/gitapi
Source0:        https://pypi.python.org/packages/source/g/gitapi/gitapi-%{version}a2.tar.gz
# Ask upstream to include license in a separate file here:
# https://bitbucket.org/haard/gitapi/issue/3/include-the-license-in-a-separate-file
Source1:        LICENSE

BuildArch:      noarch
BuildRequires:  git

%global _description\
Pure-Python API to git, which uses the command-line interface.

%description %_description

%package -n     python3-gitapi
Summary:        Pure-Python API to git, which uses the command-line interface
BuildRequires:  python3-devel
Requires:       git

%description -n python3-gitapi
Pure-Python API to git, which uses the command-line interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gitapi-%{version}a2
cp %{SOURCE1} .
# Remove egg
# Apply patches
sed -i 's/\r$//' gitapi/testgitapi.py
# Correct end of line encoding for README.rst
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gitapi

%check
%pyproject_check_import

%files -n python3-gitapi -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
