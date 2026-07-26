%global source0_hash c6b362c1ddc777748ff68fee0b9155fcdf32efb0b6731bf648340483c1ff202b

Name:           python-b2sdk
Version:        1.21.0
Release:        13%{?dist}
Summary:        Backblaze B2 SDK

License:        MIT
URL:            https://github.com/Backblaze/b2-sdk-python
Source0:        %{pypi_source b2sdk}
BuildArch:      noarch

# Fedora does not ship with version 5 or lower
Patch0:         relax-setuptools_scm-version.patch

%global _description %{expand:
Python library and a few handy utilities for easy access to all of the
capabilities of B2 Cloud Storage.

B2 command-line tool is an example of how it can be used to provide command-line
access to the B2 service, but there are many possible applications (including
FUSE filesystems, storage backend drivers for backup applications etc).}

%description %_description

%package -n python3-b2sdk
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%description -n python3-b2sdk %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n b2sdk-%{version}
rm -rf b2sdk.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/test

%files -n python3-b2sdk
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{python3_sitelib}/b2sdk-*.egg-info/
%{python3_sitelib}/b2sdk/

%changelog
%autochangelog
