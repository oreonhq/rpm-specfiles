%global source0_hash 8e79520ea64603af8c874062a292a6921f1d450056905df3e8a7708cbbe2ff6e

%global modname robosignatory
#%%global prerelease b1

Name:               python-robosignatory
Version:            0.8.2
Release:            13%{?prerelease}%{?dist}
Summary:            A Fedora Messaging consumer that automatically signs artifacts

License:            GPL-2.0-or-later
URL:                https://pagure.io/robosignatory/
Source0:            https://pagure.io/releases/robosignatory/robosignatory-%{version}%{?prerelease}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-koji
# Tests
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov

# https://bodhi.fedoraproject.org/updates/python-robosignatory-0.2.0-1.el7#comment-552652
#Requires:           sigul

%global _description\
A Fedora Messaging consumer that automatically signs artifacts.\
\
RoboSignatory is composed of multiple consumers:\
- TagSigner listens for tags into a specific koji tag, then signs the build and\
  moves it to a different koji tag.\
- AtomicSigner listens for messages about composed rpmostree trees and signs\
  those, optionally updating the tag.\
- CoreOSSigner listens for requests to sign CoreOS artefacts, downloads them\
  from AWS S3, signs them, and uploads the signature back to S3.\

%description %_description

%package -n python3-robosignatory
Summary: %summary
Requires:           python3-fedora-messaging
Requires:           koji
Requires:           rpmdevtools
# This is the default package
Provides:           robosignatory = %{version}-%{release}

%description -n python3-robosignatory %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}%{?prerelease}
# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files robosignatory

%check
%pyproject_check_import
%pytest

%files -n python3-robosignatory
%doc README.rst LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*
%{_bindir}/robosignatory

%changelog
%autochangelog
