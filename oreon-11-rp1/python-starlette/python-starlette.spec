%global source0_hash 746c43c5a278ff133132fca858701ae2495fec104c930878f07b59ce92d02e75

Name:           python-starlette
Version:        0.52.1
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source:         https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz
Patch:          python-starlette-CVE-2026-48710.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist typing_extensions}

%global common_description %{expand:
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building
async web services in Python.}

%description %{common_description}

%package -n     python3-starlette
Summary:        %{summary}

%description -n python3-starlette %{common_description}

%pyproject_extras_subpkg -n python3-starlette full

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n starlette-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files starlette

%check
%pytest -v

%files -n python3-starlette -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
