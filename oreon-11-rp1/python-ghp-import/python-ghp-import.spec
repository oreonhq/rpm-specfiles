%global source0_hash 9c535c4c61193c2df8871222567d7fd7e5014d835f97dc7b7439069e2413d343

Name:           python-ghp-import
Version:        2.1.0
Release:        16%{?dist}
Summary:        GitHub Pages Import
BuildArch:      noarch

License:        Apache-2.0
URL:            https://github.com/c-w/ghp-import
Source0:        %{pypi_source ghp-import}

BuildRequires:  python3-devel

%description
GitHub Pages Import.

%package -n python3-ghp-import
Summary:        %{summary}
Obsoletes:      python3-ghp-import2 < 1.0.1-12
Provides:       python3-ghp-import2 = %{version}-%{release}

%description -n python3-ghp-import
GitHub Pages Import.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ghp-import-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ghp_import

# Remove shebang on non-executable script
sed -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/ghp_import.py

%check
%py3_check_import ghp_import

%files -n python3-ghp-import -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ghp-import

%changelog
%autochangelog
