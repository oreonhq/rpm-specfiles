%global source0_hash 8f111d5ed0330c9f478bcf1726f44a4fc6c4f127abfa00dabbb2de9420cd537a

# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global pypi_name pagure-messages

Name:           python-%{pypi_name}
Version:        0.0.6
Release:        20%{?dist}
Summary:        A schema package for messages sent by pagure

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/pagure-messages
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fedora-messaging)
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# Ensure we don't use this with incompatible Pagure versions
Conflicts:      pagure < 5.13

%description -n python3-%{pypi_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pagure_messages
%{python3_sitelib}/pagure_messages-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
