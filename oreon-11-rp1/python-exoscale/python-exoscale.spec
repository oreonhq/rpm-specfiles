%global source0_hash 8a1db8f51af79a63f999fad138af94def6742c5ff1519d0dc263f2af3903639b

Name:           python-exoscale
Version:        0.16.1
Release:        1%{?dist}
Summary:        Python bindings for Exoscale API

License:        ISC
URL:            https://exoscale.github.io/python-exoscale/
Source0:        https://github.com/exoscale/python-exoscale/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
The library to allow developers to use the Exoscale cloud platform API with
high-level Python bindings.}

%description %_description

%package -n python3-exoscale
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(setuptools)

%description -n python3-exoscale %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python-exoscale-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files exoscale

%check
%pyproject_check_import
%pytest

%files -n python3-exoscale -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
