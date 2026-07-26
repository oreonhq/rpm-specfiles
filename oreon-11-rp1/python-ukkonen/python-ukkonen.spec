%global source0_hash d238ac2751c967594a5ffd4d3e76a01ddcc63d01088a5c54e5fdd9e3cc7e1211

Name:           python-ukkonen
Version:        1.1.0
Release:        1%{?dist}
Summary:        Implementation of bounded Levenshtein distance (Ukkonen)

License:        MIT
URL:            https://www.github.com/asottile/ukkonen
Source0:        %{url}/archive/v%{version}/ukkonen-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-devel

# We don’t use %%tox for testing because it brings in unnecessary and
# unpackaged coverage dependencies.
BuildRequires:  python3dist(pytest)

%description
Implementation of bounded Levenshtein distance (Ukkonen) port

%package -n     python3-ukkonen
Summary:        %{summary}

%description -n python3-ukkonen
Implementation of bounded Levenshtein distance (Ukkonen) port

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ukkonen-%{version}
cp -p licenses/LICENSE LICENSE-upstream

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ukkonen

%check
%pytest

%files -n python3-ukkonen -f %{pyproject_files}
%license LICENSE-upstream LICENSE
%doc README.md
%{python3_sitearch}/_ukkonen.abi3.so

%changelog
%autochangelog
