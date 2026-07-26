%global source0_hash dab0af17e78d4d9db17f4ad1cd7da264d3e3904df20813553c3fd6533724d560

Name:           python-binary-manager
Version:        0.0.6
Release:        %autorelease
Summary:        Binman firmware-packaging tool

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/package/index.html
Source:         %{pypi_source binary-manager}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(pyyaml)

%global _description %{expand:
Binman provides a mechanism for building images, from simple SPL + U-Boot
combinations, to more complex arrangements with many parts. It also allows
users to inspect images, extract and replace binaries within them, repacking if
needed.}

%description %_description

%package -n     python3-binary-manager
Summary:        %{summary}
Requires:       python3dist(jsonschema)
Requires:       python3dist(pycryptodomex)
Requires:       python3dist(pyyaml)

%description -n python3-binary-manager %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n binary-manager-%{version}

# Fix dependency name
sed -i 's:pylibfdt:libfdt:' pyproject.toml

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/binman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files binman

%check
%pyproject_check_import -e binman.setup

%files -n python3-binary-manager -f %{pyproject_files}
%doc README.rst
%{_bindir}/binman

%changelog
%autochangelog
