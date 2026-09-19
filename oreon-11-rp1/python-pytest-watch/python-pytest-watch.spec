%global source0_hash 06136f03d5b361718b8d0d234042f7b2f203910d8568f63df2f866b547b3d4b9

%global pypi_name pytest-watch
%global file_name pytest_watch
%global desc A zero-config CLI tool that runs [pytest][], and re-runs it \
when a file in your project changes. It beeps on failures and can run arbitrary \
commands on each passing and failing test run.

Name:           python-%{pypi_name}
Version:        4.2.0
Release:        28%{?dist}
Summary:        Local continuous test runner with pytest and watchdog

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-watch
Source0:        https://files.pythonhosted.org/packages/36/47/ab65fc1d682befc318c439940f81a0de1026048479f732e84fe714cd69c0/pytest-watch-4.2.0.tar.gz
Source1:        https://raw.githubusercontent.com/joeyespo/pytest-watch/master/LICENSE
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-colorama >= 0.3.3
Requires:       python3-docopt >= 0.6.2
Requires:       python3-pytest >= 2.6.4
Requires:       python3-watchdog >= 0.6.0
# Require missing watchdog deps for the package to work
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1360383
Requires:       python3-PyYAML
Requires:       python3-pathtools

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pypi_name}-%{version}
# Correct end of line encoding
sed -i 's/\r$//' *.md
sed -i 's/\r$//' %{file_name}/watcher.py
# %%patch0 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
cp %{SOURCE1} .

%install
%pyproject_install
%pyproject_save_files -l %{file_name}
pushd %{buildroot}%{_bindir}
mv ptw ptw-%{python3_version}
ln -s ptw-%{python3_version} ptw-3
mv pytest-watch pytest-watch-%{python3_version}
ln -s pytest-watch-%{python3_version} pytest-watch-3
popd

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGES.md AUTHORS.md
%license LICENSE
%{_bindir}/ptw-3*
%{_bindir}/pytest-watch-3*

%changelog
%autochangelog
