%global source0_hash 25c6141d87550549b4e27d0661fd543f1deae0dea6e9eeb9e14cbb134610e811

%global srcname  click-default-group
%global libname click_default_group

%global common_description %{expand:
Provides DefaultGroup, a subclass of click.Group that invokes a default
subcommand instead of showing a help message when a subcommand is not passed.}

Name:           python-%{srcname}
Version:        1.2.2
Release:        %autorelease
Summary:        Extends click.Group to invoke a command without explicit subcommand name

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sublee/click-default-group/
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix detection of error message in test, related to click 8
Patch0:         https://patch-diff.githubusercontent.com/raw/click-contrib/click-default-group/pull/18.patch#/0001-Fix-detection-of-error-message.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
