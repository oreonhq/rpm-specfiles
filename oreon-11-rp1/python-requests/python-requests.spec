%global source0_hash f288924cae4e29463698d6d60bc6a4da69c89185ad1e0bcc4104f584e960b9ed
Name:           python-requests
Version:        2.34.2
Release:        1%{?dist}
Summary:        Python HTTP for Humans.
License:        Apache-2.0
URL:            https://github.com/psf/requests
Source0:        https://files.pythonhosted.org/packages/source/r/requests/requests-%{version}.tar.gz
BuildArch:      noarch
Patch:          system-certs.patch
Patch:          support_IPv6_CIDR_in_no_proxy.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-requests = %{version}-%{release}
# /oreon:deps
%package -n       python3-requests+security
Summary:        Metapackage for python3-requests security extras
Requires:       python3-requests = %{version}-%{release}
Provides:       python3dist(requests[security]) = %{version}-%{release}

%description -n python3-requests+security
Metapackage for python3-requests security extras.

%package -n       python3-requests+socks
Summary:        Metapackage for python3-requests socks extras
Requires:       python3-requests = %{version}-%{release}
Requires:       python3dist(PySocks) >= 1.5.6
Provides:       python3dist(requests[socks]) = %{version}-%{release}

%description -n python3-requests+socks
Metapackage for python3-requests socks extras.

%package -n       python3-requests+use_chardet_on_py3
Summary:        Metapackage for python3-requests use_chardet_on_py3 extras
Requires:       python3-requests = %{version}-%{release}
Requires:       python3dist(chardet) >= 3.0.2
Requires:       python3dist(chardet) < 8
Provides:       python3dist(requests[use_chardet_on_py3]) = %{version}-%{release}

%description -n python3-requests+use_chardet_on_py3
Metapackage for python3-requests use_chardet_on_py3 extras.

%description
This is package 'requests' generated automatically by pyp2spec.

%package -n     python3-requests
Summary:        Python HTTP for Humans.
# oreon:reqs
Requires:       python3dist(certifi) >= 2023.5.7
Requires:       python3dist(charset_normalizer) < 4
Requires:       python3dist(charset_normalizer) >= 2
Requires:       python3dist(idna) < 4
Requires:       python3dist(idna) >= 2.5
Requires:       python3dist(urllib3) < 3
Requires:       python3dist(urllib3) >= 1.26
# /oreon:reqs
%description -n python3-requests
This is package 'requests' generated automatically by pyp2spec.

%prep
%global oreon_srcdir requests-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests usr/lib/python3*/site-packages/requests* usr/lib64/python3*/site-packages/requests* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests* usr/lib64/python3*/site-packages/requests* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requests -f %{oreon_filedir}/python3-requests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.33.1-1
- Import
