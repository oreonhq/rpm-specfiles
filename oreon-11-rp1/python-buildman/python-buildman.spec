%global source0_hash d52716d3c13d530fb564cb55d3e3d5a814d49a9cd95e5759f67989d9547b14ba

Name:           python-buildman
Version:        0.0.6
Release:        %autorelease
Summary:        Buildman build tool for U-Boot

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/build/buildman.html
Source:         %{pypi_source buildman}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
This tool handles building U-Boot to check that you have not broken it with
your patch series. It can build each individual commit and report which boards
fail on which commits, and which errors come up. It aims to make full use of
multi-processor machines.}

%description %_description

%package -n     python3-buildman
Summary:        %{summary}

%description -n python3-buildman %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n buildman-%{version}

# Remove unnecessary shebangs
sed -i "\|#!/usr/bin/env python3|d" src/buildman/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files buildman

%check
%pyproject_check_import

%files -n python3-buildman -f %{pyproject_files}
%doc README.rst
%{_bindir}/buildman

%changelog
%autochangelog
