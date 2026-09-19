%global source0_hash da067628d6d5fd9dc5a55eab37951d46bd95661b7219fab364b711366abcc690

%global pypi_name patch-ng

%global _description %{expand:
Fork of the original python-patch library to parse
and apply unified diffs.}

Name: python-%{pypi_name}
Version: 1.18.0
Release: %autorelease

License: MIT
Summary: Library to parse and apply unified diffs
URL: https://github.com/conan-io/%{name}
Source0: %{pypi_source %{pypi_name}}
BuildArch: noarch

BuildRequires: python3-devel

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files patch_ng

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
