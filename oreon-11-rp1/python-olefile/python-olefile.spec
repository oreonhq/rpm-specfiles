%global source0_hash 599383381a0bf3dfbd932ca0ca6515acd174ed48870cbf7fee123d698c192c1c

Name:           python-olefile
Version:        0.47
Release:        14%{?dist}
Summary:        Python package to parse, read and write Microsoft OLE2 files

%global         srcname         olefile
%global         _description    %{expand:
olefile is a Python package to parse, read and write Microsoft OLE2 files
(also called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix files,
Outlook messages, StickyNotes, several Microscopy file formats, McAfee
antivirus quarantine files, etc.
}

License:        BSD-2-Clause
URL:            https://github.com/decalage2/olefile
Source0:        %{pypi_source olefile %version zip}

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  dos2unix
BuildRequires:  /usr/bin/find

%description %{_description}

%package doc
Summary:        %{summary}
BuildArch:      noarch
# Fedora >= 31 does not have python2-sphinx anymore.
# There is python-sphinx in RHEL 7, but it's possibly too old.
# Python26 sphinx works
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description doc %{_description}
This package contains documentation for %{name}.


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}
Python3 version.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

# Fix windows EOL
find ./ -type f -name '*.py' -exec dos2unix '{}' ';'
dos2unix doc/*.rst


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
make -C doc html BUILDDIR=_doc_build SPHINXBUILD=sphinx-build-%{python3_version}


%install
%pyproject_install
%pyproject_save_files -l olefile


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} tests/test_olefile.py


%files doc
%doc doc/_doc_build/html

%files -n python3-%{srcname}  -f %{pyproject_files}
%doc README.md
%license doc/License.rst

%changelog
%autochangelog
