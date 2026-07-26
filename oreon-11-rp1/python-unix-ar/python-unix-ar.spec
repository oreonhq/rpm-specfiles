%global source0_hash 4e1c6e8fe5255b7babe93b9af51532ba09c6946eee413c5db00cab3878d7ed2f

Name:           python-unix-ar
Version:        0.2.1
Release:        %autorelease
Summary:        .ar file handling for Python (including .deb)

License:        BSD-3-Clause
URL:            https://github.com/getninjas/unix_ar
Source:         %{url}/archive/%{version}/unix-ar-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This packages allows the reading and writing of AR archive files.}

%description %{_description}

%package -n     python3-unix-ar
Summary:        %{summary}

%description -n python3-unix-ar %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n unix_ar-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l unix_ar

%check
%{py3_test_envvars} %{python3} tests.py

%files -n python3-unix-ar -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
