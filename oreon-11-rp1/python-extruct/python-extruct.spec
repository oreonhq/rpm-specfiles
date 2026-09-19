%global source0_hash 0a9b8703159e89fa0d7b87d7c40c12ba609f61c31a42aa87e9027e774a78a3cb

%global         srcname         extruct
%global         forgeurl        https://github.com/scrapinghub/extruct
Version:        0.18.0
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        7%{?dist}
Summary:        Extract embedded metadata from HTML markup

License:        BSD-3-Clause
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

BuildArch: noarch

%global _description %{expand:
extruct is a library for extracting embedded metadata from HTML markup.

Currently, extruct supports:

- W3C's HTML Microdata
- embedded JSON-LD
- Microformat via mf2py
- Facebook's Open Graph
- (experimental) RDFa via rdflib
- Dublin Core Metadata (DC-HTML-2003)
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname} -L

%check 
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc AUTHORS
%doc HISTORY.rst
%license LICENSE
%{_bindir}/extruct

%changelog
%autochangelog
