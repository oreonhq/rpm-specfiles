%global source0_hash 99d4fabddab7ee4a05fa458deb1a6f0d009966e4631c50d1b875767a1cd3896d

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
