%global source0_hash b327e6c8ed4c278136e0d15f436275f4f07f42f062d023e5ea999e7401bf9177

%global srcname humblewx
%global sum Library that simplifies creating user interfaces with wxPython

Name:           python-%{srcname}
Version:        0.2.2
Release:        15%{?dist}
Summary:        %{sum}

License:        GPL-3.0-or-later
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-wxpython4

BuildArch:      noarch

%description
Library that simplifies creating user interfaces with wxPython.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python3-wxpython4

%description -n python%{python3_pkgversion}-%{srcname}
Library that simplifies creating user interfaces with wxPython.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '%{srcname}*'

%check
%pyproject_check_import -t

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS

%changelog
%autochangelog
