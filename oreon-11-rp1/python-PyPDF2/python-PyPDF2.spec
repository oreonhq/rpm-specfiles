%global source0_hash e28f902f2f0a1603ea95ebe21dff311ef09be3d0f0ef29a3e44a932729564385

%global srcname PyPDF2
%global sum Python PDF toolkit and library

Name:           python-%{srcname}
Version:        1.26.0
Release:        36%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Summary:        %{sum}
Source:         https://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz
URL:            https://github.com/mstamy2/PyPDF2

# setuptools instead of distutils
# https://github.com/py-pdf/pypdf/pull/599
Patch01:        599.patch

BuildArch:      noarch

%description
A pure Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encryption and decryption of PDF files.

By being pure Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A pure Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encryption and decryption of PDF files.

By being pure Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%package -n python-%{srcname}-doc
Summary:    Documentation for python-%{srcname}

%description -n python-%{srcname}-doc
python-PyPDF2 contains documentation and examples for the python-PyPDF package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# non-executable script
sed -i -e '/^#!\//, 1d' PyPDF2/pagerange.py

# Lots of things in the repo shouldn't be executable
chmod a-x Scripts/* Sample_Code/* LICENSE README.md CHANGELOG

%build
%py3_build

%install
%py3_install

%check
# NOTE: Upstream has some testing bugs
#python -m unittest Tests.tests

%files -n python3-%{srcname}
%{python3_sitelib}/*
%license LICENSE

%files -n python-%{srcname}-doc
%doc README.md CHANGELOG Scripts/ Sample_Code/
%license LICENSE

%changelog
%autochangelog
