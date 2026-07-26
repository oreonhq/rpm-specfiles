%global source0_hash 9e829dbe167c01eb5103d15ebc6086b70e9fa13ca9bf09c736345451f8cb8ba7

# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
# http://rpm.org/user_doc/conditional_builds.html
%if 0%{?fedora} >= 30
# disabled by default
%bcond_with py2
%else
%bcond_without py2 0
%endif

%global srcname pygiftiio

%global desc %{expand: \
GIFTI is an XML-based file format for cortical surface data. This reference IO
implementation is developed by the Neuroimaging Informatics Technology
Initiative (NIfTI).}

Name:           python-%{srcname}
Version:        1.0.4
Release:        29%{?dist}
Summary:        Python bindings for Gifti

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.nitrc.org/frs/?group_id=75
Source0:        https://www.nitrc.org/frs/download.php/1285/%{srcname}-%{version}.tar.gz
Source1:        https://www.nitrc.org/frs/download.php/261/gifti_write_example.py
Source2:        https://www.nitrc.org/frs/download.php/260/gifti_read_example.py

BuildArch:      noarch

%description
%{desc}

%if %{with py2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
Requires:       gifticlib-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       gifticlib-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}
cp -v %{SOURCE1} .
cp -v %{SOURCE2} .

%build
# Nothing to do

%install
# Put things where they belong
install -D -m 0644 %{srcname}.py -t %{buildroot}/%{python3_sitelib}/
%if %{with py2}
install -D -m 0644 %{srcname}.py -t %{buildroot}/%{python2_sitelib}/
%endif

%check
# No tests

%if %{with py2}
%files -n python2-%{srcname}
%license LICENSE.GPL
%doc gifti_write_example.py gifti_read_example.py
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.pyc
%{python2_sitelib}/%{srcname}.pyo
%endif

%files -n python3-%{srcname}
%license LICENSE.GPL
%doc gifti_write_example.py gifti_read_example.py
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-3*.opt-1.pyc
%{python3_sitelib}/__pycache__/%{srcname}.cpython-3*.pyc

%changelog
%autochangelog
