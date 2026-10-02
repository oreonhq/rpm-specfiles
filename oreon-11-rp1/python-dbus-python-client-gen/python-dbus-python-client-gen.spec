%global source0_hash e297a0f20694885bb8db35cb203b930ca512e2071f658d725967238a70a7ed31

%global srcname dbus-python-client-gen

Name:           python-%{srcname}
Version:        0.8.5
Release:        %autorelease
Summary:        Python Library for Generating dbus-python Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-python-client-gen
Source0:        https://github.com/stratis-storage/dbus-python-client-gen/archive/refs/tags/v0.8.5.tar.gz#/dbus-python-client-gen-0.8.4.tar.gz

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dbus_python_client_gen

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
