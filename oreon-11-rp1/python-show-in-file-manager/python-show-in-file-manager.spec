%global source0_hash 15d16e4a875b9e217b038d02f029c3800c4a6ad645e3f73c9e107ea26bab3adb

%global srcname show-in-file-manager
%{?python_enable_dependency_generator}

Name:          python-%{srcname}
Version:       1.1.4
Release:       17%{?dist}
Summary:       Show in File Manager is a Python package to open the system file manager and optionally select files in it.

License:       MIT
URL:           https://github.com/damonlynch/showinfilemanager
Source0:       %{pypi_source}
BuildArch:     noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:      %{srcname} = %{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{srcname}
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/showinfilemanager
%{python3_sitelib}/showinfm/
%{python3_sitelib}/show_in_file_manager-*.egg-info/

%changelog
%autochangelog
