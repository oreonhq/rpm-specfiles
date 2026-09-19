%global source0_hash 047f8f4b9dbd104c004cfe24211af38b7a21fd707a103b214b6a5c5af3c4790c

Name:      python-sphinxcontrib-doxylink
Version:   1.13.0
Release:   7%{?dist}
Summary:   A Sphinx extension to link to external Doxygen API documentation
License:   BSD-2-Clause
URL:       https://github.com/sphinx-contrib/doxylink
Source0:   https://github.com/sphinx-contrib/doxylink/archive/refs/tags/%{version}.tar.gz
BuildArch: noarch

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: python3-pyparsing
BuildRequires: python3-pytest
BuildRequires: python3-sphinx
BuildRequires: python3-testfixtures

%global _description %{expand:
This package contains a Sphinx extension to link to external Doxygen API
documentation. It allows you to specify C++ symbols and it will convert
them into links to the HTML page of their Doxygen documentation.}

%description %_description

%package -n python3-sphinxcontrib-doxylink
Summary: %{summary}

%description -n python3-sphinxcontrib-doxylink %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n doxylink-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L sphinxcontrib

%check
%pyproject_check_import
%{pytest}

%files -n python3-sphinxcontrib-doxylink -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
