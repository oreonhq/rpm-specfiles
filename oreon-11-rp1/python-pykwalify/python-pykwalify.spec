%global source0_hash 796b2ad3ed4cb99b88308b533fb2f559c30fa6efb4fa9fda11347f483d245884

%global pypi_name pykwalify

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        17%{?dist}
Summary:        Python lib/cli for JSON/YAML schema validation

License:        MIT
URL:            https://github.com/Grokzen/pykwalify
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
It is a YAML/JSON validation library.
This framework is a port with a lot added functionality
of the java version of the framework kwalify that can be
found at: http://www.kuwata-lab.com/kwalify/

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
It is a YAML/JSON validation library.
This framework is a port with a lot added functionality
of the java version of the framework kwalify that can be
found at: http://www.kuwata-lab.com/kwalify/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE docs/license.rst
%doc README.md
%{_bindir}/pykwalify

%changelog
%autochangelog
