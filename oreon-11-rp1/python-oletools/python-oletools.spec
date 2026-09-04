%global source0_hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Name:           python-oletools
Version:        0.60.2
Release:        1%{?dist}
Summary:        Tools to analyze Microsoft OLE2 files

# oletools/*.py: BSD
# oletools/olevba*.py: BSD and MIT
# oletools/thirdparty/xxxswf/*.py: No license specified
# oletools/thirdparty/xglob/*.py: BSD
# oletools/thirdparty/tablestream/*.py: BSD
# oletools/thirdparty/zipfile27/*.py: Python
# oletools/thirdparty/msoffcrypto/*.py: MIT
# Automatically converted from old format: BSD and MIT and Python - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Python
URL:            https://www.decalage.info/python/oletools
VCS:            https://github.com/decalage2/oletools/
#               https://github.com/decalage2/oletools/releases
#               https://github.com/nolze/msoffcrypto-tool/releases

%global         srcname oletools

# Bootstrap may be needed to break circular dependencies between
# python-oletools and python-pcodedmp
%bcond_with     bootstrap

# Build with python3 package by default
%bcond_without  python3

# Bundles taken from oletools-0.54.2b/oletools/thirdparty
%global         _provides \
Provides:       bundled(oledump) = 0.0.49 \
Provides:       bundled(tablestream) = 0.09 \
Provides:       bundled(xglob) = 0.07 \
Provides:       bundled(xxxswf) = 0.1

%global         _description %{expand:
The python-oletools is a package of python tools from Philippe Lagadec
to analyze Microsoft OLE2 files (also called Structured Storage,
Compound File Binary Format or Compound Document File Format),
such as Microsoft Office documents or Outlook messages, mainly for
malware analysis, forensics and debugging.
It is based on the olefile parser.
See http://www.decalage.info/python/oletools for more info.
}

Source0:        https://github.com/decalage2/oletools/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Remove the bundled libraries from the build. Use the system libraries instead
Patch0:         %{name}-01-thirdparty.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-colorclass
BuildRequires:  python%{python3_pkgversion}-easygui
BuildRequires:  python%{python3_pkgversion}-olefile
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pymilter
BuildRequires:  python%{python3_pkgversion}-prettytable
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-msoffcrypto
%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-pcodedmp
%endif

%description    %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{_provides}

Requires:       python%{python3_pkgversion}-pymilter
Requires:       python%{python3_pkgversion}-pyparsing
Requires:       python%{python3_pkgversion}-colorclass
Requires:       python%{python3_pkgversion}-easygui
Requires:       python%{python3_pkgversion}-olefile
Requires:       python%{python3_pkgversion}-prettytable
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-msoffcrypto
%if %{without bootstrap}
Requires:       python%{python3_pkgversion}-pcodedmp
%endif

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python3 version.

%package -n python-%{srcname}-doc
Summary:        Documentation files for %{name}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-doc}

%description -n python-%{srcname}-doc %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

# Use globally installed python modules instead of bundled ones
for i in colorclass easygui olefile prettytable pyparsing; do
  rm -rf "oletools/thirdparty/${i}"
done

sed -i -e '
  s|from oletools.thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.olefile import olefile|from olefile import olefile|;
  s|from oletools.thirdparty.prettytable import prettytable|import prettytable|;
  s|from oletools.thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from .thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.easygui import easygui|import easygui|;
' */*.py

sed -i -e 's|pyparsing>=2\.1\.0,<3|pyparsing|' requirements.txt setup.py

%if %{with bootstrap}
sed -i -e '/pcodedmp/d' requirements.txt setup.py
%endif

%build
%py3_build

%install
# Install python3 files
%py3_install

# Move executables to python3 versioned names
pushd %{buildroot}%{_bindir}
  main=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}'.format(sys.version_info))")  # e.g. 3
  full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4

  # mraptor3 and olevba3 are deprecated, mraptor or olevba should be used instead
  rm -f mraptor3 olevba3

  for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    mv -f "${i}" "${i}-${full}"
    ln -s "${i}-${full}" "${i}-${main}"
  done
popd

# Remove '\r' line ending and shebang from non-executable python libraries
for file in %{buildroot}%{python3_sitelib}/%{srcname}/{.,*,*/*}/*.py; do
  sed -e '1{\@^#![[:space:]]*/usr/bin/env python@d}' -e 's|\r$||' "${file}" > "${file}.new"
  touch -c -r "${file}" "${file}.new"
  mv -f "${file}.new" "${file}"
done

# Remove files that should either go to %%doc or to %%license
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/{doc,LICENSE.txt,README.*}
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/msoffcrypto/LICENSE.txt
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xglob/LICENSE.txt
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xxxswf/LICENSE.txt

# Create trivial name symlinks to the default executables of preferred python version
# For example in FC31 exists python3 package, but puthon2 is the preferred one
pushd %{buildroot}%{_bindir}
for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4
    ln -s "${i}-${full}" "${i}"
done
popd

# Prepare licenses from bundled code for later %%license usage
mv -f %{srcname}/thirdparty/xglob/LICENSE.txt xglob-LICENSE.txt
mv -f %{srcname}/thirdparty/xxxswf/LICENSE.txt xxxswf-LICENSE.txt

%check
%{__python3} -m unittest

# Simple self-test: If it fails, package won't work after installation
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/olevba-3 --code cheatsheet/oletools_cheatsheet.docx
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/mraptor-3 cheatsheet/oletools_cheatsheet.docx

%files -n python%{python3_pkgversion}-%{srcname}
%license %{srcname}/LICENSE.txt xglob-LICENSE.txt xxxswf-LICENSE.txt
%doc README.md
%{python3_sitelib}/*
%{_bindir}/ezhexviewer-3*
%{_bindir}/msodde-3*
%{_bindir}/olebrowse-3*
%{_bindir}/oledir-3*
%{_bindir}/oleid-3*
%{_bindir}/olefile-3*
%{_bindir}/olemap-3*
%{_bindir}/olemeta-3*
%{_bindir}/oleobj-3*
%{_bindir}/oletimes-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/olevba-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/mraptor-3*
%{_bindir}/pyxswf-3*
%{_bindir}/rtfobj-3*
%{_bindir}/ezhexviewer
%{_bindir}/mraptor
%{_bindir}/msodde
%{_bindir}/olebrowse
%{_bindir}/oledir
%{_bindir}/oleid
%{_bindir}/olefile
%{_bindir}/olemap
%{_bindir}/olemeta
%{_bindir}/oleobj
%{_bindir}/oletimes
%{_bindir}/olevba
%{_bindir}/pyxswf
%{_bindir}/rtfobj

%files -n python-%{srcname}-doc
%doc %{srcname}/doc/*
%doc cheatsheet

%changelog
%autochangelog
