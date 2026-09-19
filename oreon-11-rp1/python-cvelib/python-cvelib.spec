%global source0_hash 371984737f29b8e5e433febd07a52eb7d73b4ea9628b79f7b6ce10468feccb3d

Name:           python-cvelib
Version:        1.8.0
Release:        %autorelease
Summary:        A library and command line interface for the CVE Project services
License:        MIT
URL:            https://github.com/RedHatProductSecurity/cvelib
Source:         %{pypi_source cvelib}

BuildArch:      noarch
BuildRequires:  python3-devel

Provides: bundled(cve-schema)

%global _description %{expand:
A library and a command line interface for the CVE Services API.
Note that version 1.3.0 of cvelib is compatible with CVE Services 2.2.0.}

%description %_description

%package -n     python3-cvelib
Summary:        %{summary}

%description -n python3-cvelib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cvelib-%{version}
sed -i 's:"collective.checkdocs",::' pyproject.toml

%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cvelib
mkdir -p %{buildroot}/%{_mandir}
cp -r --preserve=timestamps man %{buildroot}/%{_mandir}/man1
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%pyproject_check_import

%files -n python3-cvelib -f %{pyproject_files}
%{_bindir}/cve
%{_mandir}/man1/cve*

%changelog
%autochangelog
