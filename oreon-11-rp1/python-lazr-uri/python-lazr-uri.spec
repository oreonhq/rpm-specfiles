%global source0_hash 5026853fcbf6f91d5a6b11ea7860a641fe27b36d4172c731f4aa16b900cf8464

%global pypi_name lazr.uri
Name:           python-lazr-uri
Version:        1.0.6
Release:        %autorelease
Summary:        Parsing and dealing with URIs

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.uri
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
The lazr.uri package includes code for parsing and dealing with URIs.}

%description %_description

%package -n     python3-lazr-uri
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-lazr-uri  %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lazr

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest src/lazr/uri/tests/*py

%files -n python3-lazr-uri -f %{pyproject_files}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth

%changelog
%autochangelog
