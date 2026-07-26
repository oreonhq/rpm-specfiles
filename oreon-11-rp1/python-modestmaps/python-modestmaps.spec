%global source0_hash e52092980f1a1bbd422acee6d42689d17381b716984eeb274b9c171884d7fa81

%global commit 524d5d36bdedc4995f06cdefaaa82546c41a75c2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global pkgname modestmaps
%global srcname ModestMaps

Name:           python-%{pkgname}
Version:        1.4.7
Release:        28%{?dist}
Summary:        Modest Maps python port

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://modestmaps.com
Source0:        https://github.com/stamen/%{pkgname}-py/archive/%{commit}/%{pkgname}-py-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Modest Maps is a small, extensible, and free library for designers and
developers who want to use interactive maps in their own projects. It provides
a core set of features in a tight, clean package with plenty of hooks for
additional functionality.

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-imaging

%{?python_provide:%python_provide python%{python3_pkgversion}-modestmaps}

%description -n python%{python3_pkgversion}-%{pkgname}
Modest Maps is a small, extensible, and free library for designers and
developers who want to use interactive maps in their own projects. It provides
a core set of features in a tight, clean package with plenty of hooks for
additional functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-py-%{commit}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pkgname}
%doc CHANGELOG
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
