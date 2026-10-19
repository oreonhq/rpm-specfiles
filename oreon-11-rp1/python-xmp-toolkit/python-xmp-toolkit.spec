%global source0_hash ca0aa2c60d418dd2558767db59953ab5954fb5b87dc0b50cecd60566b0b4e2da
Name:           python-xmp-toolkit
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python XMP Toolkit for working with metadata
License:        BSD-3-Clause
URL:            https://github.com/python-xmp-toolkit/python-xmp-toolkit
Source0:        https://files.pythonhosted.org/packages/source/p/python_xmp_toolkit/python_xmp_toolkit-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-xmp-toolkit = %{version}-%{release}
# /oreon:deps
%package -n       python3-xmp-toolkit+test
Summary:        Metapackage for python3-xmp-toolkit test extras
Requires:       python3-xmp-toolkit = %{version}-%{release}
Requires:       python3dist(pytest) >= 2.7.3
Provides:       python3dist(xmp-toolkit[test]) = %{version}-%{release}

%description -n python3-xmp-toolkit+test
Metapackage for python3-xmp-toolkit test extras.

%description
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.

%package -n     python3-xmp-toolkit
Summary:        Python XMP Toolkit for working with metadata
Requires:       exempi
%description -n python3-xmp-toolkit
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.

%package -n python-xmp-toolkit-doc
Summary:        python-xmp-toolkit documentation
%description -n python-xmp-toolkit-doc
Documentation for python-xmp-toolkit

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python_xmp_toolkit-%{version}
%oreon_prep
%build

%pyproject_wheel
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%install
%pyproject_install
%oreon_autofiles python3-xmp-toolkit usr/lib/python3*/site-packages/xmp_toolkit* usr/lib64/python3*/site-packages/xmp_toolkit* usr/bin/*
%oreon_autofiles python-xmp-toolkit-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/xmp_toolkit* usr/lib64/python3*/site-packages/xmp_toolkit* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{pytest}
%files
%files -n python3-xmp-toolkit -f %{oreon_filedir}/python3-xmp-toolkit.list
%files -n python-xmp-toolkit-doc -f %{oreon_filedir}/python-xmp-toolkit-doc.list

%changelog

%autochangelog
