%global source0_hash f681d6b0a7209c0b35f8eb89cf3b47595a4789099023d55bd7fdc909682979de

%global srcname arpy

Name:          python-%{srcname}
Summary:       Library for accessing "ar" files
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/viraptor/arpy

Version:       2.3.0
Release:       15%{?dist}
Source0:       %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch

%description
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest

%description -n python3-%{srcname}
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

This package allows using arpy in Python 3 applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
