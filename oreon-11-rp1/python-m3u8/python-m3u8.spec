%global source0_hash 6521e02d0c3295999c14e348d7c6d4f13b1ba33ba14e1b9a3a6d5b8170ad3efb

%global srcname m3u8

%bcond_without  tests

Name:           python-%{srcname}
Version:        6.0.0
Release:        8%{?dist}
Summary:        Python module %srcname parser
License:        MIT
Url:            https://github.com/globocom/m3u8
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Python module %srcname parser

%package -n     python3-%{srcname}
Summary:        %{summary}
%py_provides python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-iso8601
BuildRequires:  python3-pytest
BuildRequires:  python3dist(wheel)
Requires:       python3dist(iso8601)

%description -n python3-%{srcname}
Python module %srcname parser

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
# needs BR: python3-devel
%pyproject_buildrequires -r

%build
# Bytecompile Python modules
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
%pyproject_check_import

# 3 deselected tests require internet connection
#%%pytest -vv -k "not (test_load_should_ and (uri or redirect))"
%pytest -vv -k "not (test_load_should_ and (uri or redirect)) and not test_raise_timeout_exception_if_timeout_happens_when_loading_from_uri"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
