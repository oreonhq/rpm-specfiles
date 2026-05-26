%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:        2.4
Release:        9%{?dist}
Summary:        Resolve JSON Pointers in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-pointer
Source0:        https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-2.4.tar.gz
# oreon url source checksums begin
%global source0_sha256 585cee82b70211fa9e6043b7bb89db6e1aa49524340dde8ad6b63206ea689d88
%global source0_file jsonpointer-2.4.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%global _description %{expand:
Library to resolve JSON Pointers according to RFC 6901.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %{_description}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jsonpointer-2.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "585cee82b70211fa9e6043b7bb89db6e1aa49524340dde8ad6b63206ea689d88" || { echo "oreon: Source0 SHA256 mismatch for jsonpointer-2.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%python3 -m unittest discover

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md AUTHORS
%{_bindir}/jsonpointer

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-9
- Prepare for Oreon 11 (RP1)
