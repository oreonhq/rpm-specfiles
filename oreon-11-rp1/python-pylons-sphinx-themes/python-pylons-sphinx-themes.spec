%global source0_hash 2c133f983ae293b671b997fdaa7d8784c1d5ffe2c3d2611201b8f49dd63962e6

%global srcname pylons-sphinx-themes
%global desc This is a Python package that contains Sphinx themes for Pylons related \
projects.

Name: python-%{srcname}
Version: 1.0.13
Release: 19%{?dist}
BuildArch: noarch

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Summary: Sphinx themes for projects under the Pylons Project
URL: https://github.com/Pylons/%{srcname}
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pygments

%description
%{desc}

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pylons_sphinx_themes

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
