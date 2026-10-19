%global source0_hash 454ca16dc7fa59aa9c8ba42500992531773fbdc04caef1b39611755cae9f34bf
Name:           python-pytesseract
Version:        0.3.13
Release:        1%{?dist}
Summary:        Python-tesseract is a python wrapper for Google's Tesseract-OCR
License:        Apache-2.0
URL:            https://github.com/madmaze/pytesseract
Source0:        https://github.com/madmaze/pytesseract/archive/v%{version}/pytesseract-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.0.4
BuildRequires:  python3dist(wheel) >= 0.29.0
Requires:       python3-pytesseract = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytesseract
Summary:        Python-tesseract is a python wrapper for Google's Tesseract-OCR
Requires:       tesseract
%description -n python3-pytesseract

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytesseract-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
    %{buildroot}%{python3_sitelib}/pytesseract/pytesseract.py
chmod +x %{buildroot}/%{python3_sitelib}/pytesseract/pytesseract.py
%oreon_autofiles python3-pytesseract usr/lib/python3*/site-packages/pytesseract* usr/lib64/python3*/site-packages/pytesseract* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytesseract* usr/lib64/python3*/site-packages/pytesseract* usr/bin/*

%check

%pyproject_check_import
%pytest -k 'not test_image_to_string_with_image_type[jpeg2000] and not test_get_languages[incorrect_tessdata_dir] and not test_get_languages[invalid_tessdata_dir]'
%files
%files -n python3-pytesseract -f %{oreon_filedir}/python3-pytesseract.list

%changelog

%autochangelog
