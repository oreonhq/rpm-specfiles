%global source0_hash 8dc780be038712fc12c9fecb3db4fe49e0d0723f9c171d7cda85c20369be693c

Name:           python-click-option-group
Version:        0.5.7
Release:        %autorelease
Summary:        Option groups missing in Click 

License:        BSD-3-Clause
URL:            https://github.com/click-contrib/click-option-group
Source:         %{pypi_source click_option_group}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
click-option-group is a Click-extension package that adds option groups
missing in Click.}

%description %_description

%package -n python3-click-option-group
Summary:        %{summary}
%description -n python3-click-option-group %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n click_option_group-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click_option_group

%check
%pytest

%files -n python3-click-option-group -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
