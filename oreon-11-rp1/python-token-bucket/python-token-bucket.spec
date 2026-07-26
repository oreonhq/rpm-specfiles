%global source0_hash 58a9744f11289fe780e2a93da773db2d0872ddc9dcd9a34036b1912557450156

Name:           python-token-bucket
Version:        0.3.0
Release:        18%{?dist}
Summary:        A Token Bucket implementation

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/falconry/token-bucket
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Temporary, until https://github.com/falconry/token-bucket/pull/24 gets
# merged upstream.
Patch0:         0000-py312-imp.patch
# Drop pytest-runner and "setup.py test" support
# https://github.com/falconry/token-bucket/pull/28
# Cherry-picked on 0.3.0
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch1:         0001-Drop-pytest-runner-and-setup.py-test-support.patch

%global _description %{expand:
The token-bucket package provides an implementation of the token bucket
algorithm suitable for use in web applications for shaping or policing
request rates. This implementation does not require the use of an independent
timer thread to manage the bucket state.
}

%description %_description

%package -n python3-token-bucket
Summary: %{summary}

%description -n python3-token-bucket %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n token-bucket-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files token_bucket

%check
%tox

%files -n python3-token-bucket -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
