%global source0_hash 6809f5d0c8ed341bea33d4ecbff6d10564883f9f2017dbd9c128baee2d224cc3

%global pkg_name jsonformatter

Name:           python-%{pkg_name}
Version:        0.3.4
Release:        7%{?dist}
Summary:        Formatter to output json logs

License:        BSD-2-Clause
URL:            https://github.com/MyColorfulDays/jsonformatter
BuildArch:      noarch
# PyPI source is incomplete
Source0:        https://github.com/MyColorfulDays/jsonformatter/archive/v%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
jsonformatter is a formatter for python to output json logs.

%package -n python3-%{pkg_name}
Summary:        Formatter to output json logs

%description -n python3-%{pkg_name}
jsonformatter is a formatter for python to output json logs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkg_name}

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
