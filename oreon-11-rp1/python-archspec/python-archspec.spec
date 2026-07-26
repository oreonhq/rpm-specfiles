%global source0_hash 5bec8dfc5366ff299071200466dc9572d56db4e43abca3c66bdd62bc2b731a2a

%global srcname archspec

Name:           python-%{srcname}
Version:        0.2.5
Release:        %autorelease
Summary:        A library to query system architecture

License:        Apache-2.0 OR MIT
URL:            https://github.com/archspec/archspec
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-jsonschema

%global _description %{expand:
Archspec aims at providing a standard set of human-understandable labels for
various aspects of a system architecture like CPU, network fabrics, etc. and
APIs to detect, query and compare them.

This project grew out of Spack and is currently under active development. At
present it supports APIs to detect and model compatibility relationships among
different CPU microarchitectures.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf archspec/json/.git*

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*
%{_bindir}/archspec

%changelog
%autochangelog
