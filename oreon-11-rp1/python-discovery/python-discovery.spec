%global source0_hash 8f3746c4b4968d22afbb97d36e1a0e5b66e6c0f297290f2e95f05b9b8bf18690

Name:           python-discovery
Version:        1.4.2
Release:        %autorelease
Summary:        Python discovery helper library

License:        MIT
URL:            https://pypi.org/project/python-discovery/
Source:         https://files.pythonhosted.org/packages/0b/1a/cbbaf13b730abb0a16b964d984e19f2fe520c21a4dc664051359a3f5a9e7/python_discovery-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Python discovery helper library.


%package -n python3-python-discovery
Summary:        %{summary}

%description -n python3-python-discovery
Python discovery helper library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n python_discovery-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files python_discovery


%check
%pyproject_check_import


%files -n python3-python-discovery -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
