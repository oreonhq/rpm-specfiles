%global source0_hash cb9260eefec05db57653bc4947b38c1c4241c86f5b14e4a5dbbe8cc7a53be512

%global srcname pytest-tornado
%global srcname_ pytest_tornado

Name:           python-%{srcname}
Version:        0.8.1
Release:        23%{?dist}
Summary:        Py.test plugin for testing of asynchronous tornado applications

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/eugeniy/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel

%global _description %{expand:
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname_}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
