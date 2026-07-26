%global source0_hash 866143ccc863283b3163b9022a15cd04aed8e736ac22204f3488d41944b7265e

%global srcname pywebdav
%global pypiname PyWebDAV3

Name:           pywebdav
Version:        0.9.12
Release:        28%{?dist}
Summary:        WebDAV library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/andrewleech/%{pypiname}
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypiname}/%{pypiname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of objects,
store properties for objects, etc.

%package -n python3-%{srcname}

Summary:        WebDAV library for Python 3

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of objects,
store properties for objects, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypiname}-%{version}

rm -f doc/INSTALL

%build
%py3_build

# Move the LICENSE to separate it from other documentation
mv doc/LICENSE .

%install
%py3_install

%files -n python3-%{srcname}

%license LICENSE

# README references e.g. "doc/ARCHITECTURE", so package doc/ as a subdirectory
%doc README
%doc doc/

%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{pypiname}*.egg-info
%exclude %{python3_sitelib}/%{srcname}/server
%exclude %{_bindir}/*

%changelog
%autochangelog
