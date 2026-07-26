%global source0_hash 5cad17bedfc3af57b399db0fed32771f18fc54bbd917e85546088607ac5e1277

%global _description %{expand:
Goals:
- Convert UNIX timestamps to and from RFC3339.
- Either produce RFC3339 strings with a UTC offset (Z) or with the offset that
  the C time module reports is the local timezone offset.
- Simple with minimal dependencies/libraries.
- Avoid timezones as much as possible.
- Be very strict and follow RFC3339.}

Name:           python-strict-rfc3339
Version:        0.7
Release:        21%{?dist}
Summary:        Strict, simple, lightweight RFC3339 functions

License:        GPL-3.0-only
URL:            https://github.com/danielrichman/strict-rfc3339
Source:         %{pypi_source strict-rfc3339}
BuildArch:      noarch

BuildRequires:  python3-devel

%description %{_description}

%package -n     python3-strict-rfc3339
Summary:        %{summary}

%description -n python3-strict-rfc3339 %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n strict-rfc3339-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files strict_rfc3339

%check
%pyproject_check_import

%files -n python3-strict-rfc3339 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
