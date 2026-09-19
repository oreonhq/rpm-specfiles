%global source0_hash 289f084ede210a18c88e7e8d2b89c1205813dac58b1e7aad9d99126e56a1b458

%global pypi_name text-unidecode

Name:           python-%{pypi_name}
Version:        1.3
Release:        25%{?dist}
Summary:        A Python module for handling non-Roman text data

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/kmike/text-unidecode/
Source0:        https://github.com/kmike/text-unidecode/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
text-unidecode is the most basic port of the Text::Unidecode Perl library.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
text-unidecode is the most basic port of the Text::Unidecode Perl library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/text_unidecode/
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
