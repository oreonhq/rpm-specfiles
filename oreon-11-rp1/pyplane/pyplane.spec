%global source0_hash a5250694c6e4227f1209f00c6a3e6e425793d7e179b7b5218452f5ea7753cbdf

%bcond_without tests

%global _description %{expand:
PyPlane is a free software for phase plane analysis of second order dynamical
systems written in PYTHON and PyQT5. Comparable to MATLAB's pplane.}

%global forgeurl https://github.com/TUD-RST/pyplane
Name:           pyplane
Version:        2.0.1
Summary:        Phase plane analysis of nonlinear systems

%global  tag PyPlane_v%{version}
%forgemeta

Release:        %autorelease
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  libappstream-glib
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
# bits not mentioned in install_requires
BuildRequires:  texlive-latex
BuildRequires:  texlive-dvipng
BuildRequires:  desktop-file-utils
%endif

# Optional but readme says they improve the graphs etc., so add them as weak
# dependencies
Recommends:     texlive-latex
Recommends:     texlive-dvipng

# Add virtual provides to help users find it
Provides:       python3-pyplane

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%generate_buildrequires
# the install requirements seem to be required for tests, so include them
%pyproject_buildrequires %{?with_tests:-r}

# correct import in test script
sed -i -e '/sys.path.append/ d' -e 's/import core./import pyplane.core./' tests/test_core.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyplane

desktop-file-install --dir=%{buildroot}%{_datadir}/applications packaging/linux/pyplane.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/pyplane.desktop

%check
%if %{with tests}
%{pytest}
%endif

%files -f %{pyproject_files}
%{_datadir}/applications/pyplane.desktop
%doc README.md AUTHORS
%{_bindir}/pyplane

%changelog
%autochangelog
