%global source0_hash 1d0ebdf6bbbdec4d576451edddc1a86d19ed7e81b63b499a3f2199f3009e49b8

%global modname mailman3_fedmsg_plugin_schemas

%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:               mailman3-fedmsg-plugin-schemas
Version:            1.0.0
Release:            9%{?dist}
Summary:            Fedora Messaging schema for messages emitted by Mailman 3

License:            LGPL-3.0-or-later
URL:                https://github.com/fedora-infra/mailman3-fedmsg-plugin
Source0:            %{pypi_source %modname}

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel

Requires:           fedora-messaging

%global _description %{expand:
  A schema describing fedora-messaging messages sent by mailman.
}

%description %_description

%package -n python3-%name
Summary: %{summary}

%description -n python3-%name %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import %{modname}

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
