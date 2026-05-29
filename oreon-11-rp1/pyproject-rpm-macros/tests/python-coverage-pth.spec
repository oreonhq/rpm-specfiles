%global source0_hash f8cfdc5f7f524267c5c8d5e92c39d72a3822875e6b0b53e7611af056e3ed9dbf

Name:           python-coverage-pth
Version:        0.0.2
Release:        0%{?dist}
Summary:        Coverage PTH file to enable coverage at the virtualenv level
License:        BSD-2-Clause
URL:            https://github.com/dougn/coverage_pth
Source:         %{pypi_source coverage_pth}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
This package exists to test %%pyproject_save_files -M.
It contains no Python modules, just a single .pth file.


%package -n     python3-coverage-pth
Summary:        %{summary}

%description -n python3-coverage-pth
...


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n coverage_pth-%{version}
# support multi-digit Python versions in setup.py regexes
sed -i 's/d)/d+)/' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# internal check for our macros:
# this should not work without -M
%pyproject_save_files -L && exit 1 || true

# but this should:
%pyproject_save_files -LM


%files -n python3-coverage-pth -f %{pyproject_files}
%{python3_sitelib}/coverage_pth.pth
