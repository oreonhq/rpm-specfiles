%global source0_hash 522a3b80e885c62b9561c4150cefda7a67cad954d22d474c6f9362348828e079
Name:           ephemeral-port-reserve
Version:        1.1.4
Release:        1%{?dist}
Summary:        Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.
License:        MIT
URL:            https://github.com/Yelp/%{name}/
Source0:        https://github.com/Yelp/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch:          fix_test_fqdn.patch
BuildArch:      noarch
%py_provides python3-ephemeral-port-reserve
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ephemeral-port-reserve = %{version}-%{release}
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ephemeral-port-reserve-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%pytest
%files

%changelog

%autochangelog
