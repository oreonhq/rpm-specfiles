%global source0_hash debfb621a3151c225f6fb4e9a8c6b86b2516e237e6f0fe60dcffee5b62d1796a

%global srcname doxyqml
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.5.3
Release:        11%{?dist}
License:        BSD
Summary:        Doxygen to document your QML classes
Url:            https://invent.kde.org/sdk/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Doxyqml lets you use Doxygen to document your QML classes,
It integrates as a Doxygen input filter to turn .qml files into pseudo-C++
which Doxygen can then use to generate documentation.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

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
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{srcname}

%changelog
%autochangelog
