%global source0_hash a937ef596ad94d16e7ed2c8553ad7be305798dcdcfd65ae60210b1e54ab51a2f
Name:          unshield
Version:       1.6.2
Release:        1%{?dist}
Summary:        Extract CAB files from InstallShield installers
SourceLicense: MIT and LicenseRef-RSA
License:       MIT
URL:           https://github.com/twogood/unshield
VCS:           git:%{url}.git
Source0:        https://github.com/twogood/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:   cmake
BuildOption(conf): -DUSE_OUR_OWN_MD5=OFF
# oreon:deps
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This tool allows the extraction of InstallShield format cabinet files (which
are different from Microsoft cabinet files). It was initially developed as a
part of the SynCE project to aid with installing applications for Pocket PC
devices, which were often contained in InstallShield installers, but these days
that is rather less likely to be the primary use case.

%package devel
Summary:       Files needed for software development with %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the files needed for development with
%{name}.

%files -f %{oreon_filedir}/main.list
%files -n unshield-devel -f %{oreon_filedir}/unshield-devel.list

%changelog

%autochangelog
