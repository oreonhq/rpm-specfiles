%global source0_hash 522a3b80e885c62b9561c4150cefda7a67cad954d22d474c6f9362348828e079

Name:           ephemeral-port-reserve
Version:        1.1.4
Release:        17%{?dist}
Summary:        Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.

License:        MIT
URL:            https://github.com/Yelp/%{name}/
Source0:        https://github.com/Yelp/%{name}/archive/refs/tags/v%{version}.tar.gz

# Fix a failing test on containers without systemd
# Sent upstream: https://github.com/Yelp/ephemeral-port-reserve/pull/20
Patch:          fix_test_fqdn.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Provide the python3-* namespace as the package
# can also be used as a library.
%py_provides python3-ephemeral-port-reserve

%global _description %{expand:
Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.}

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ephemeral-port-reserve-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ephemeral_port_reserve

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%{_bindir}/ephemeral-port-reserve
%doc README.md

%changelog
%autochangelog
