%global source0_hash aba10bf2dd25ef25b0a6e116e5ee10e43852fe285f66a4092984c87cbfcf5b18

Name:           python-pytest-relaxed
Version:        2.0.2
Release:        10%{?dist}
Summary:        Relaxed test discovery/organization for pytest

License:        BSD-2-Clause
URL:            https://github.com/bitprophet/pytest-relaxed
Source:         %{url}/archive/%{version}/pytest-relaxed-%{version}.tar.gz

# Backport patch for compatibility with pytest 8.4+
Patch:          https://github.com/bitprophet/pytest-relaxed/pull/34.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides relaxed test discovery for pytest.

It is the spiritual successor to python3-spec, but is built for pytest instead
of nosetests, and rethinks some aspects of the design (such as increased
ability to opt-in to various behaviors).}

%description %_description

%package -n python3-pytest-relaxed
Summary:        %{summary}

%description -n python3-pytest-relaxed %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-relaxed-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_relaxed

%check
%pyproject_check_import
%pytest

%files -n python3-pytest-relaxed -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
