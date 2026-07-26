%global source0_hash df1d5c5624d02526a4513f5817b5f3ef235b9599da5fe520fc8877124b9c0292

%global pypi_name advisory-parser

Name:           python-%{pypi_name}
Version:        1.12
Release:        5%{?dist}
Summary:        Security flaw parser for upstream security advisories

# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://github.com/mprpic/advisory-parser
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library allows you to parse data from security advisories of certain
projects to extract information about security issues. The parsed information
includes metadata such as impact, CVSS score, summary, description, and
others; for a full list, see the advisory_parser/flaw.py file.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name}
This library allows you to parse data from security advisories of certain
projects to extract information about security issues. The parsed information
includes metadata such as impact, CVSS score, summary, description, and
others; for a full list, see the advisory_parser/flaw.py file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE COPYRIGHT
%doc README.rst
%{python3_sitelib}/advisory_parser
%{python3_sitelib}/advisory_parser-%{version}.dist-info

%changelog
%autochangelog
