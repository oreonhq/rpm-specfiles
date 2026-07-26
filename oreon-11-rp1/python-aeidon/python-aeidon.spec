%global source0_hash a86a46ada459155696d49cacdb8aaf7cfa3958383b43f7e1be6e38247f2e955c

%global pypi_name aeidon

Name:           python-%{pypi_name}
Version:        1.15
Release:        29%{?dist}
Summary:        Subtitle file manipulation library

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gettext

%description
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      gaupol < 1.16
Conflicts:      gaupol < 1.16

%description -n python3-%{pypi_name}
Aeidon is a library for reading, writing and manipulating
text-based subtitle files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# FIXME in upstream
sed -i '14i shutil.copytree("data/ui", "aeidon/data/ui")' setup-aeidon.py

# we want to package aeidon, not gaupol
# the setup.py file is for gaupol
mv setup.py setup_gaupol.py
sed 's/from setup import/from setup_gaupol import/' setup-aeidon.py > setup.py

%generate_buildrequires
rm -rf aeidon/data/{headers,patterns,ui}  # setup.py fails if this was already created
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
