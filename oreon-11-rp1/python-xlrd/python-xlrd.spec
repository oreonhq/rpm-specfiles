%global source0_hash f72f148f54442c6b056bf931dbc34f986fd0c3b0b6b5a58d013c9aef274d0c88

%global srcname xlrd
%global sum Library to extract data from Microsoft Excel (TM) spreadsheet files

Name:           python-%{srcname}
Version:        2.0.1
Release:        27%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.python-excel.org/
Source0:        %pypi_source

BuildArch:      noarch
#BuildRequires:  dos2unix

%generate_buildrequires
%pyproject_buildrequires

%description
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{srcname}
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0 onwards)
on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong support for Excel
dates.  Unicode-aware.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

# fix CRLF to LF
#for i in */*.py *.html docs/* examples/*; do
#  # ignore missing files, they was may be only removed by mistake
#  dos2unix $i || :
#done
#for i in docs/* examples/xlrdnameAPIdemo.py; do
#  iconv -f iso8859-1 -t UTF-8 $i > $i.tmp
#  mv -f $i.tmp $i
#done

%build
%pyproject_wheel
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if 0%{?with_python3_other}
%py3_other_install
%endif
%pyproject_install
%pyproject_save_files -l xlrd

# remove .py extension from binary
mv $RPM_BUILD_ROOT%{_bindir}/runxlrd.py $RPM_BUILD_ROOT%{_bindir}/runxlrd
rm -rf $RPM_BUILD_ROOT%{_bindir}/runxlrd.py* \
  $RPM_BUILD_ROOT/%{python3_sitelib}/xlrd/doc \
  $RPM_BUILD_ROOT/%{python3_sitelib}/xlrd/examples

%check
%pyproject_check_import

%{python3} -c 'import xlrd'

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%attr(755,root,root) %{_bindir}/*

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst CHANGELOG.rst
%attr(755,root,root) %dir %{python3_other_sitelib}/xlrd
%{python3_other_sitelib}/xlrd/*
%{python3_other_sitelib}/xlrd-*egg-info
%endif

%changelog
%autochangelog
