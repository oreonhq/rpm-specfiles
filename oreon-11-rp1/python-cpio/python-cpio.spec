%global source0_hash none

Name:           python-cpio
Version:        0.1
Release:        58%{?dist}
Summary:        A Python module for accessing cpio archives

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://developer.berlios.de/projects/python-cpio/
Source0:        https://web.archive.org/web/20150301000000/http://download.berlios.de/python-cpio/python-cpio-%{version}.tar.bz2
Patch0:        https://src.fedoraproject.org/rpms/python-cpio/raw/rawhide/f/cpioarchive_supports_2_3.patch
Patch1:        https://src.fedoraproject.org/rpms/python-cpio/raw/rawhide/f/cpioarchive_bytes_str_compatibility.patch

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
_tar="python-cpio-%{version}.tar.bz2"
if test ! -f "$_tar"; then
  curl -sfL -o "$_tar" "https://src.fedoraproject.org/rpms/python-cpio/raw/rawhide/f/python-cpio-%{version}.tar.bz2" || \\
  curl -sfL -o _src.rpm "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-cpio-%{version}-59.fc44.src.rpm" && \\
  rpm2cpio _src.rpm | cpio -id "$_tar" && rm -f _src.rpm
fi
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-58
- Import
