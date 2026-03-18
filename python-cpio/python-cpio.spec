Name:           python-cpio
Version:        0.1
Release:        58%{?dist}
Summary:        A Python module for accessing cpio archives

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://developer.berlios.de/projects/python-cpio/
Source0:        http://download.berlios.de/python-cpio/python-cpio-0.1.tar.bz2
Patch0:        	cpioarchive_supports_2_3.patch
Patch1:         cpioarchive_bytes_str_compatibility.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
This is a Python module for accessing cpio archives.

%description %_description

%package -n python3-cpio
Summary: %summary

%description -n python3-cpio %_description

%prep
%setup -q
%patch -P0
%patch -P1

%build
%py3_build

%install
%py3_install

%files -n python3-cpio
%license COPYING.lib
%doc AUTHORS ChangeLog README TODO
%{python3_sitelib}/cpioarchive.py*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/*.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-58
- Prepare for Oreon 11 (RP1)
