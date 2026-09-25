%global source0_hash 19006c799fa0f5e198bc1371d551e672b03c799d67dea61d0670edc88e0df971

%global srcname dbus-client-gen

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        Library for Generating D-Bus Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-client-gen
Source0:        https://github.com/stratis-storage/dbus-client-gen/archive/refs/tags/v%{version}.tar.gz#/dbus-client-gen-0.5.2.tar.gz

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
%autochangelog
