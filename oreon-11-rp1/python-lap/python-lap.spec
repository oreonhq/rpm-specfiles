%global source0_hash 9eff7169e3ca452995af0493cc20d35452c4bfd06122c36c06457119ffbd411b

%global common_description %{expand:
This package provides the 'lap' Python library, a Linear Assignment Problem
solver using the Jonker-Volgenant algorithm. It is required by applications
like Beets for efficient tag matching.
}

Name:           python-lap
Version:        0.5.13
Release:        %autorelease
Summary:        Linear Assignment Problem solver for Python
License:        BSD-2-Clause

URL:            https://pypi.org/project/lap/
Source0:        %{pypi_source lap}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}

BuildSystem:  pyproject
BuildOption(install): -l lap

%description %common_description

%package -n python3-lap
Summary:        %{summary}

%description -n python3-lap %common_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lap-%{version}

%install -a

# Remove test suite from installed files (not needed at runtime)
rm -rvf '%{buildroot}%{python3_sitearch}/lap/tests'
sed -r -i '/.*\/lap\/tests(\/|$)/d' %{pyproject_files}
sed -r -i '/lap\.tests(\.|$)/d' %{_pyproject_modules}

%check
mkdir _empty
cd _empty
ln -s ../lap/tests
%pyproject_check_import
%pytest

%files -n python3-lap -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
