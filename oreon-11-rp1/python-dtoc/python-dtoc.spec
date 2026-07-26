%global source0_hash 279fdb23c506c8f2c4ff1c789901a085c99d5071b01c822924e87b1183ee9544

Name:           python-dtoc
Version:        0.0.6
Release:        %autorelease
Summary:        Devicetree-to-C generator

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/develop/driver-model/of-plat.html
Source:         %{pypi_source dtoc}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This is a Python program and associated utilities, which supports converting
devicetree files into C code. It generates header files containing struct
definitions, as well as C files containing the data. It does not require any
modification of the devicetree files.}

%description %_description

%package -n     python3-dtoc
Summary:        %{summary}

%description -n python3-dtoc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dtoc-%{version}

# Fix dependency name
sed -i 's:pylibfdt:libfdt:' pyproject.toml

# Remove unnecessary shebangs
sed -i src/dtoc/*.py \
  -e "\|#!/usr/bin/env python3|d" \
  -e "\|#!/usr/bin/python|d"

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dtoc

%check
%pyproject_check_import -e dtoc.setup

%files -n python3-dtoc -f %{pyproject_files}
%doc README.rst
%{_bindir}/dtoc

%changelog
%autochangelog
