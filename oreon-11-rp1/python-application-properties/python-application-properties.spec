%global source0_hash d8e7858bbf72c9d834117d74f561efb65d31e5193f1a5e803d6adc2d556c8465

%global pypi_name application-properties

Name:           python-%{pypi_name}
Version:        0.9.2
Release:        1%{?dist}
Summary:        A simple, easy to use, unified manner of accessing program properties

License:        MIT
URL:            https://github.com/jackdewinter/application_properties
Source0:        %{pypi_source application_properties}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml) >= 5.4.1
BuildRequires:  python3dist(tomli) >= 2.0.1
BuildRequires:  python3dist(typing-extensions) >= 4.5
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-cov)

%description
The application_properties package was born out of necessity.
During the creation of the PyMarkdown project, there was a distinct need for
a configuration subsystem that was able to handle more complex
configuration scenarios.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(pyyaml) >= 5.4.1
Requires:       python3dist(tomli) >= 2.0.1
Requires:       python3dist(typing-extensions) >= 4.5
%description -n python3-%{pypi_name}
The application_properties package was born out of necessity.
During the creation of the PyMarkdown project, there was a distinct need for
a configuration subsystem that was able to handle more complex
configuration scenarios.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n application_properties-%{version}
sed -i -e 's@pytest@nopytest@' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sed -i 's/\r$//' README.md

%install
%pyproject_install
%pyproject_save_files -l application_properties

rm -f %{buildrot}%{python3_sitelib}application_properties/.external-package

%check
%pyproject_check_import application_properties
#%%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
