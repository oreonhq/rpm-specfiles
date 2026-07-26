%global source0_hash 368af3e640150c5c7c6eaa358e9334f31f5a4e376a66e5e4d00638940af669bc

%global pkgname pagure-exporter
%global srcname pagure_exporter
%global desc Simple exporter tool that helps migrate repository files, data assets and issue tickets from projects on Pagure to GitLab

Name:           %{pkgname}
Version:        0.1.4
Release:        5%{?dist}
Summary:        %{desc}

License:        GPL-3.0-or-later
Url:            https://github.com/gridhead/%{pkgname}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{desc}

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

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
