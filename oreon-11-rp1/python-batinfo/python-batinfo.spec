%global source0_hash 497e29efc9353ec52e71d43bd040bdfb6d685137ddc2b9143cded4583af572f5

%global pypi_name batinfo

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        38%{?dist}
Summary:        Python module to retrieve battery information

License:        LGPL-3.0-or-later
URL:            https://github.com/nicolargo/batinfo
Source0:        %{pypi_source %{pypi_name} %{version}}
Buildarch:      noarch

BuildRequires:  python3-devel

%description
A simple Python module to retrieve battery information on Linux-based
operating system. No ACPI or external software is needed. Only the Linux
kernel and its /sys/class/power_supply folder.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A simple Python module to retrieve battery information on Linux-based
operating system. No ACPI or external software is needed. Only the Linux
kernel and its /sys/class/power_supply folder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{_defaultdocdir}/%{pypi_name}/

%pyproject_save_files -l %{pypi_name}

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS README.md
%license LICENSE

%changelog
%autochangelog
