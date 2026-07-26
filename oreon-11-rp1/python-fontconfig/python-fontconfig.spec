%global source0_hash 4837290305613710cf6c515db8923284da06e4f48a549d2fe8e2d4276aed3e73

%global srcname python_fontconfig

Name:           python-fontconfig
Version:        0.6.2.post1
Release:        2%{?dist}
Summary:        Python bindings for Fontconfig library

License:        GPL-3.0-or-later
URL:            https://github.com/lilydjwg/%{name}
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  fontconfig-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  dejavu-serif-fonts

%description
%{summary}.

%package -n python3-fontconfig
Summary:        %{summary}
%{?python_provide:%python_provide python3-fontconfig}

%description -n python3-fontconfig
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%{python3} %{py_setup} build_ext -i
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fontconfig

%check
yes | %{py3_test_envvars} %{python3} test/test.py

%files -n python3-fontconfig -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
