%global source0_hash 0dc0494a0e6561b268542b28ede2280387c2728114f117d3bb5d8e4787b93ef4

%global srcname pdfrw

Name: python-%{srcname}
Version: 0.4
Release: 32%{?dist}
Summary: Python library to read and write PDF files
License: MIT

URL:     https://github.com/pmaupin/pdfrw
Source0: %{pypi_source %{srcname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildArch: noarch

%description
pdfrw is a Python library and utility that reads and writes PDF files. pdfrw
can also be used in conjunction with reportlab, in order to re-use portions
of existing PDFs in new PDFs created with reportlab.

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist reportlab}
Requires: %{py3_dist reportlab}

%description -n python3-%{srcname}
pdfrw is a Python library and utility that reads and writes PDF files. pdfrw
can also be used in conjunction with reportlab, in order to re-use portions
of existing PDFs in new PDFs created with reportlab.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pdfrw

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst examples

%changelog
%autochangelog
