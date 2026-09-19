%global source0_hash 6332a31b8ddb8916d364ab734941c786dcce7dc65fcc84870c5a25ab3ac18cbf

Name:           python-cccolutils
Version:        1.5
Release:        35%{?dist}
Summary:        Python Kerberos Credential Cache Collection Utilities

License:        GPL-2.0-or-later
URL:            https://pagure.io/cccolutils
Source0:        https://pagure.io/releases/cccolutils/CCColUtils-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  python3-devel

%global _description %{expand:
Python utilities for Kerberos Credential Cache Collections}

%description %{_description}

%package     -n python3-cccolutils
Summary:        %{summary}

%description -n python3-cccolutils %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n CCColUtils-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L cccolutils

%check
%{py3_test_envvars} %{python3} -m unittest -v tests.cccolutils_test

%files -n python3-cccolutils -f %{pyproject_files}
%license COPYING

%changelog
%autochangelog
