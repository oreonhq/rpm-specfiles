%global source0_hash d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed

Name:           python-mdurl
Version:        0.1.2
Release:        1%{?dist}
Summary:        Markdown URL utilities
License:        MIT
URL:            https://github.com/executablebooks/mdurl
Source0:        https://github.com/executablebooks/mdurl/archive/%{version}/mdurl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
URL utilities for markdown-it parser.}

%description %_description

%package -n     python3-mdurl
Summary:        %{summary}

%description -n python3-mdurl %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mdurl-%{version}
sed -i "s/pytest-cov//" tests/requirements.txt

%generate_buildrequires
%pyproject_buildrequires tests/requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdurl

%check
%pyproject_check_import
%pytest

%files -n python3-mdurl -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
