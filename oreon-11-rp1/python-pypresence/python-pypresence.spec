%global source0_hash 958a5bb2f28c3120c89c68cc242abd8e72e2dac9aaf9be36b7c7a6217dcf4669

Name:           python-pypresence
Version:        4.3.0
Release:        13%{?dist}
Summary:        A Discord Rich Presence Client in Python 
License:        MIT
URL:            https://qwertyquerty.github.io/pypresence/html/index.html
Source0:        https://github.com/qwertyquerty/pypresence/archive/v%{version}/pypresence-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Python-pypresence is a simple Discord Rich Presence Client in Python. \
Note that in order to use most of it's functions, an authorized app \
is required.

%description %{_description}

%package -n python3-pypresence
Summary:        %{summary}

%description -n python3-pypresence %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pypresence-%{version}
# docs include files that are under a different license model, omitting them
rm -rf %{buildroot}/docs

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pypresence

%check
%pyproject_check_import -t

%files -n python3-pypresence -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
