%global source0_hash 39c501eaf10c6c9bde754a41089dbd3e6c06bacdbd8f99041b3fb5d991055e1f
%global pypi_name spec2scl
Name:           %{pypi_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Convert RPM specfiles to be SCL ready
License:        MIT
URL:            https://github.com/sclorg/spec2scl
Source0:        https://files.pythonhosted.org/packages/source/s/spec2scl/spec2scl-%{version}.tar.gz
Patch:          spec2scl-1.2.2-no-pytest-runner.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-spec2scl = %{version}-%{release}
# /oreon:deps
%description
spec2scl is a tool to convert RPM specfiles to SCL-style specfiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 644 spec2scl.1 %{buildroot}%{_mandir}/man1/spec2scl.1
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
