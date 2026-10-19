%global source0_hash fe7eb948871521d690abfb3f6354abd41846d026cb72611aed467b69e88c942e
Name:		python-isal
Version:	1.8.0
Release:        1%{?dist}
Summary:        Faster zlib and gzip compatible (de)compression using the ISA-L library
License:	PSF-2.0 AND Zlib
URL:		https://github.com/pycompression/python-isal
Source0:        https://github.com/pycompression/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-old-setuptools-epel9.patch
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-isal = %{version}-%{release}
# /oreon:deps
%description
This package provides Python bindings for the ISA-L library.

The Intel(R) Intelligent Storage Acceleration Library (ISA-L)
implements several key algorithms in assembly language.

This includes a variety of functions to provide zlib/gzip compatible
compression and decompression.

%package -n python3-isal
Summary:        Faster zlib and gzip compatible (de)compression using the ISA-L library
%py_provides	python3-isal
%description -n python3-isal
This package provides Python bindings for the ISA-L library.

The Intel(R) Intelligent Storage Acceleration Library (ISA-L)
implements several key algorithms in assembly language.

This includes a variety of functions to provide zlib/gzip compatible
compression and decompression.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# setuptools versions < 77 don't support PEP 639
# convert license key in pyproject.toml to old format for older versions
setuptoolsver=$(python3 -c "import setuptools; print(setuptools.__version__.split('.')[0])")
if [ $setuptoolsver -lt 77 ] ; then
    sed 's!^\(license\)\s*=\s*\(.*\)$!\1 = { text = \2 }!' -i pyproject.toml
fi

%build

export PYTHON_ISAL_LINK_DYNAMIC=1
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_ISAL=%{version}
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-isal usr/lib/python3*/site-packages/isal* usr/lib64/python3*/site-packages/isal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/isal* usr/lib64/python3*/site-packages/isal* usr/bin/*

%check

%pytest tests
%files
%files -n python3-isal -f %{oreon_filedir}/python3-isal.list

%changelog

%autochangelog
