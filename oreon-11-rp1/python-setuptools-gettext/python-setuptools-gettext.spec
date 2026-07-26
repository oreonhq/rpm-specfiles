%global source0_hash 43f099eff31a4712cdfbcbb07e0264b0546ed3ebfd7ea998189326c519390d2c

Name:           python-setuptools-gettext
Version:        0.1.14
Release:        7%{?dist}
Summary:        Setuptools gettext extension plugin

License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Source:         %{pypi_source setuptools_gettext}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
# Enables tests/test_example.py::test_update_pot
BuildRequires:  gettext

%global _description %{expand:
Setuptools helpers for gettext. Compile .po files into .mo files.}

%description %{_description}

%package -n     python3-setuptools-gettext
Summary:        %{summary}

%description -n python3-setuptools-gettext %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n setuptools_gettext-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l setuptools_gettext

%check
%pyproject_check_import
# -rs: print reasons for skipped tests
%pytest -v -rs

%files -n python3-setuptools-gettext -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
