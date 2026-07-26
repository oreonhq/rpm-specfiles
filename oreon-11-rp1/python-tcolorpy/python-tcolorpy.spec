%global source0_hash 43c1afe908f9968ff5ce59f129b62e392049b8e7cd6a8d3f416bd3d372bb5c7a

Name:          python-tcolorpy
Version:       0.1.3
Release:       13%{?dist}
Summary:       Python library to apply true color for terminal text

License:       MIT
URL:           https://github.com/thombashi/tcolorpy
Source0:       %{pypi_source tcolorpy}

BuildArch:     noarch
BuildRequires: python3-devel

# Missing pytest-md-report, hence manually specifying pytest instead
BuildRequires: python3dist(pytest)

%description
%{summary}.

%package -n python3-tcolorpy
Summary:        %{summary}

%description -n python3-tcolorpy
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n tcolorpy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files tcolorpy

%check
%pytest

%files -n python3-tcolorpy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
