%global source0_hash 078b6fe7f770dd164f9549bdd7a355663225a3ff9b0f7575ad546d27239ec609

%global srcname jupyter-kernel-test
%global srcname_ jupyter_kernel_test

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        Machinery for testing Jupyter kernels via the messaging protocol

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).

%generate_buildrequires
%pyproject_buildrequires -x test

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname_}-%{version} -p1
sed -i -e '/"pre-commit"/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    %{python3} -m unittest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
