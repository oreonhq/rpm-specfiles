%global source0_hash 133f3a023fdc2d1977ceebd7d3a7723830e31778a783e029d041ff3a5d682e54

Name:           python-xkbregistry
Version:        0.3
Release:        %autorelease
Summary:        Bindings for libxkbregistry using cffi

License:        MIT
URL:            https://github.com/sde1000/python-xkbregistry
Source:         %{pypi_source xkbregistry}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxkbcommon-devel

Requires:  libxkbcommon


%global _description %{expand:
Python bindings for libxkbregistry using cffi.}


%description %_description

%package -n     python3-xkbregistry
Summary:        %{summary}

%description -n python3-xkbregistry %_description


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n xkbregistry-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%python3 xkbregistry/ffi_build.py


%install
%pyproject_install
%pyproject_save_files xkbregistry


%check
%pyproject_check_import -t
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-xkbregistry -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-1
- Prepare for Oreon 11 (RP1)
