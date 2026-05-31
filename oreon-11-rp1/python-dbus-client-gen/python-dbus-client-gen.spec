%global source0_hash 2fd53bf85955cf9bc76f8bbbdb9968fc891401bea247b31d702a35f5a3bd8bba

%global srcname dbus-client-gen

Name:           python-%{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        Library for Generating D-Bus Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-client-gen
Source0:        https://github.com/stratis-storage/dbus-client-gen/archive/v0.5.1/dbus-client-gen-0.5.1.tar.gz

BuildArch:      noarch

%global _description \
This library contains a few methods that consume an XML specification\
of a D-Bus interface and return classes or functions that may be useful\
in constructing a python D-Bus client. The XML specification has the format\
of the data returned by the Introspect() method\
of the Introspectable interface.

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
%pyproject_save_files -l dbus_client_gen

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-1
- Prepare for Oreon 11 (RP1)
