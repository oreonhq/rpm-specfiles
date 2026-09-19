%global source0_hash 057ab68d31270dece4d1a47662096aa76341968aaee145ffc711cb44cbd5c4a7

%global pypi_name ofxparse

Name:           python-%{pypi_name}
Version:        0.21
Release:        15%{?dist}
Summary:        Python library for working with the OFX (Open Financial Exchange) file format
License:        MIT
URL:            https://pypi.org/project/ofxparse/
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
ofxparse is a parser for Open Financial Exchange (.ofx) format files. OFX files 
are available from almost any online banking site, so they work well if you 
want to pull together your finances from multiple sources. Online trading 
accounts also provide account statements in OFX files.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-six
BuildRequires:  python3-lxml

%description -n python3-%{pypi_name}
ofxparse is a parser for Open Financial Exchange (.ofx) format files. OFX files 
are available from almost any online banking site, so they work well if you 
want to pull together your finances from multiple sources. Online trading 
accounts also provide account statements in OFX files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS

%changelog
%autochangelog
