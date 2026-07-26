%global source0_hash 86c9933b004aec8ce1c476d1d1129e00325c7724df3c09aa353d5f8e883ed08d

%global srcname colorzero

Name:           python-%{srcname}
Version:        2.0
Release:        20%{?dist}
Summary:        Yet another Python color library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/waveform80/colorzero
Source0:        %{url}/archive/release-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Colorzero is a color manipulation library for Python (yes, another one)
which aims to be reasonably simple to use and "pythonic" in nature.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-release-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files colorzero

%check
%{python3} -m pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
