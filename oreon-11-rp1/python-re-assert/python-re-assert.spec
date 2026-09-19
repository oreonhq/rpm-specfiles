%global source0_hash 01c4a849ed520923e4bab9afdf73b5f2698c4f92ad7f580ccb3f68ea79c69c0c

Name:           python-re-assert
Version:        1.1.0
Release:        %autorelease
Summary:        Show where your regex match assertion failed

# SPDX
License:        MIT
URL:            https://github.com/asottile/re-assert
Source:         %{url}/archive/v%{version}/re-assert-%{version}.tar.gz


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}!}

%description %{common_description}

%package -n python3-re-assert
Summary: %{summary}

%description -n python3-re-assert %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n re-assert-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l re_assert

%check
%pytest

%files -n python3-re-assert -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
