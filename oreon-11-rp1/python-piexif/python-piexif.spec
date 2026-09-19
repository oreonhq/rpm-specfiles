%global source0_hash abfd9a67795e23d7a76f9407d60841efa68c5d6e43376b295bb821a30602c569

%global modname piexif

Name:           python-%{modname}
Version:        1.1.3
Release:        28%{?dist}
Summary:        Pure Python library to simplify exif manipulations with python

License:        MIT
URL:            https://github.com/hMatoba/Piexif
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# Taken from https://github.com/hMatoba/Piexif/issues/108
Patch0:         python-piexif-fix-tests-pillow.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Very simple Python library to simplify exif manipulations that does
not depend on other libraries.

There are only just five functions:
    load(filename)                 - Get exif data as dict.
    dump(exif_dict)                - Get exif as bytes to save with JPEG.
    insert(exif_bytes, filename)   - Insert exif into JPEG.
    remove(filename)               - Remove exif from JPEG.
    transplant(filename, filename) - Transplant exif from JPEG to JPEG.}

%description %{_description}

%package -n     python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
Suggests:       python%{python3_version}dist(pillow)

%description -n python3-%{modname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Piexif-%{version}

sed -i 's|==.*$||' requirements.txt
sed -i 's|unittest.makeSuite|unittest.defaultTestLoader.loadTestsFromTestCase|' tests/s_test.py

%generate_buildrequires
%pyproject_buildrequires requirements.txt -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
