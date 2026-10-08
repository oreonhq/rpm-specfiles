%global source0_hash e06b88efe223885d2725df51cf7c9b7b463d1c6f04ea49d4690874318d0eb7a3

Name:           python-dbus-deviation
Version:        0.6.1
Release:        1%{?dist}
Summary:        D-Bus introspection XML linter
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/dbus-deviation/
Source0:        https://files.pythonhosted.org/packages/01/dc/047feaa6a81545e10c37d4eeff86443c90dd114c5ce13d6937c5ed38854d/dbus-deviation-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Tools for checking D-Bus interface XML.

%package -n python3-dbus-deviation
Summary:        %{summary}

%description -n python3-dbus-deviation
Tools for checking D-Bus interface XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n dbus-deviation-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dbusdeviation

%files -n python3-dbus-deviation -f %{pyproject_files}
