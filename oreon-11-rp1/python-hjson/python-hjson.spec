%global source0_hash 0317721da1df80f5902cd56bbc6659a8f473313d25ec6f2e88d904f116829299

%global forgeurl https://github.com/hjson/hjson-py
# This is the commit corresponding to the PyPI release
# https://github.com/hjson/hjson-py/issues/35
%global commit 1687b811fcbbc54b5ac71cfbaa99f805e406fbcb

Name:           python-hjson
Version:        3.1.0
Release:        %autorelease
Summary:        User interface for JSON

License:        MIT
URL:            https://hjson.github.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/%{commit}/hjson-py-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package is a Python implementation of Hjson based on simplejson.}

%description %_description

%package -n     python3-hjson
Summary:        %{summary}

%description -n python3-hjson %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hjson-py-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l hjson

%check
%pytest -v

%files -n python3-hjson -f %{pyproject_files}
%doc README.md history.md
%{_bindir}/hjson

%changelog
%autochangelog
