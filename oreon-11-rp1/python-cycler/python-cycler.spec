%global source0_hash 2530b40270be9e5e8c5f570d15a934c5dc9737ce3f3ba54307b371655e48e7e4

%global srcname cycler
%global sum Cycle through lists in various ways (used by matplotlib)
%global desc General purpose library used by matplotlib to cycle through lists for colors,\
marker styles, etc

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Source0:        %pypi_source
URL:            https://github.com/matplotlib/cycler.git

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
