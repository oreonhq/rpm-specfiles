%global source0_hash 01a870108f96a447d066f843d5ea1765c1441d3f8ea376f71624df58bb77726b

Name:           rpminspect-data-centos
Version:        1.4
Release:        8%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files for CentOS
Group:          Development/Tools
License:        CC-BY-SA-4.0
URL:            https://gitlab.com/redhat/centos-stream/ci-cd/rpminspect-data-centos
Source0:        https://dcantrell.fedorapeople.org/rpminspect-data-centos/%{name}-%{version}.tar.xz
Source1:        https://dcantrell.fedorapeople.org/rpminspect-data-centos/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-62977BB9C841B965.gpg

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gnupg2

Requires:       rpminspect >= 1.11

# Used by inspections enabled in the configuration file
Requires:       fedora-license-data
Requires:       xhtml1-dtds
Requires:       html401-dtds
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
Requires:       libabigail
Requires:       /usr/bin/annocheck

%description
CentOS and CentOS Stream specific configuration file for rpminspect
and data files used by the inspections provided by librpminspect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license CC-BY-SA-4.0.txt
%doc AUTHORS README
%{_datadir}/rpminspect
%{_bindir}/rpminspect-centos

%changelog
%autochangelog
