%global source0_hash d3b752049b453a5c95edb27ce78d69e9319af5a34f257fa0f4c738c701b4184e

%global modname weasyprint
%global srcname weasyprint

Name:           weasyprint
Version:        68.1
Release:        1%{?dist}
Summary:        Utility to render HTML and CSS to PDF

License:        BSD-3-Clause
URL:            https://weasyprint.org
Source0:        %{pypi_source weasyprint}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# used as "build-backend" in pyproject.toml but not detected by Fedora's
# macros to generate build requirements
BuildRequires:  python3dist(flit-core)
# requirements for testing
BuildRequires:  dejavu-fonts-all
BuildRequires:  ghostscript
# https://doc.courtbouillon.org/weasyprint/latest/first_steps.html
BuildRequires:  pango >= 1.44.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

Requires:       python3-weasyprint = %{version}-%{release}

%description
WeasyPrint can render HTML and CSS to PDF. It aims to support web standards
for printing.

%package -n python3-weasyprint
Summary:        Python library to render HTML and CSS to PDF
Requires:       pango >= 1.44.0
# other Python dependencies will be picked up automatically
# Weasyprint will fail if no fonts are installed. There's no way to know
# what fonts the user would actually want, but require a few common ones
# that might be useful:
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts

%description -n python3-weasyprint
The WeasyPrint Python library is a rendering engine for HTML and CSS that
can export to PDF. It aims to support web standards for printing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -n auto
# do not ship tests
rm -rf %{buildroot}%{python3_sitelib}/%{modname}/tests

%files
%license LICENSE
%doc README.rst
%{_bindir}/weasyprint

%files -n python3-weasyprint
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-%{version}.dist-info/
%{python3_sitelib}/%{modname}/

%changelog
%autochangelog
