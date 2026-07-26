%global source0_hash 41b1aa841160b3f4684cdff9152f29a32195a434fb7dbd5e336d2f8773375973

%{?python_enable_dependency_generator}

%global pypi_name urlgrabber
%global majorver 4
%global minorver 1
%global patchver 0
%global dashversion %{majorver}-%{minorver}-%{patchver}

# Tests require internet access
%bcond check 1

Name:           python-%{pypi_name}
Version:        %{majorver}.%{minorver}.%{patchver}
Release:        25%{?dist}
Summary:        A high-level cross-protocol url-grabber

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://urlgrabber.baseurl.org/
# Not uploaded there yet...
#Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
#Source0:        http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz
Source0:        https://github.com/rpm-software-management/urlgrabber/releases/download/urlgrabber-%{dashversion}/urlgrabber-%{version}.tar.gz

BuildArch:      noarch

%global _description\
A high-level cross-protocol url-grabber for python supporting HTTP, FTP\
and file locations.  Features include keepalive, byte ranges, throttling,\
authentication, proxies and more.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)
%if %{with check}
BuildRequires:  python3dist(pycurl)
BuildRequires:  python3dist(six)
%endif

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

This package provides the Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build
sed -e "s|/usr/bin/python|%{__python3}|" -i scripts/*

%install
%py3_install
rm -rf %{buildroot}%{_docdir}/urlgrabber-%{version}

%if %{with check}
%check
export PYTHONPATH=$PWD
export URLGRABBER_EXT_DOWN="%{buildroot}%{_libexecdir}/urlgrabber-ext-down"
%{__python3} test/runtests.py
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc ChangeLog README TODO
%{_bindir}/urlgrabber
%{_libexecdir}/urlgrabber-ext-down
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
