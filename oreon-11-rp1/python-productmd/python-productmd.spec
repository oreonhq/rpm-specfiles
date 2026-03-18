Name:           python-productmd
Version:        1.50
Release:        2%{?dist}
Summary:        Library providing parsers for metadata related to OS installation

License:        LGPL-2.1-only
URL:            https://github.com/release-engineering/productmd
Source:         %{pypi_source productmd}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description \
Python library providing parsers for metadata related to composes\
and installation media.

%description %_description

%package -n python3-productmd
Summary:        %{summary}

%description -n python3-productmd %_description

%prep
%autosetup -n productmd-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files productmd

%check
%pytest

%files -n python3-productmd -f %{pyproject_files}
%license LICENSE
%doc AUTHORS

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.50-2
- Prepare for Oreon 11 (RP1)
