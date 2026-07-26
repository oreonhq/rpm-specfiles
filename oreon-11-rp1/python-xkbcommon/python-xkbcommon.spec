%global source0_hash 5be5973bf5b7525687a4df6c84789b421590d7f7cf92ae56f2aab177b795d516

Name:           python-xkbcommon
Version:        0.8
Release:        13%{?dist}
Summary:        Bindings for libxkbcommon using cffi

License:        MIT
URL:            https://github.com/sde1000/python-xkbcommon
Source:         %{pypi_source xkbcommon}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxkbcommon-devel

Requires:  libxkbcommon

%global _description %{expand:
Python bindings for libxkbcommon using cffi.}

%description %_description

%package -n     python3-xkbcommon
Summary:        %{summary}

%description -n python3-xkbcommon %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n xkbcommon-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%python3 xkbcommon/ffi_build.py

%install
%pyproject_install
%pyproject_save_files xkbcommon

%check
%pyproject_check_import -t
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-xkbcommon -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
