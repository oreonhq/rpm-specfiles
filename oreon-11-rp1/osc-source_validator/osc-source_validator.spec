%global source0_hash c15d397c0010ea72fcf3658978ee1a52c4ad275a1c56fc48be7986f53c264037
%global obsroot /usr/lib/obs
%global obssvcroot %{obsroot}/service
%global srcname obs-service-source_validator
Name:           osc-source_validator
Version:        0.47
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        OBS source service to validate sources
URL:            https://github.com/openSUSE/obs-service-source_validator
Source0:        https://github.com/openSUSE/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnupg2
Requires:       obs-build
Requires:       osc
Requires:       rpm-build
Requires:       %{_bindir}/xmllint
Requires:       %{_bindir}/cpio
Requires:       unzip
Requires:       perl(Date::Parse)
Requires:       perl(Time::Zone)
Requires:       perl(Time::Local)
Requires:       perl(Time::localtime)
Provides:       %{srcname} = %{version}-%{release}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Build)
BuildRequires:  perl-generators
# /oreon:deps
%description
This is a source service for openSUSE Build Service.

This service runs all checks as required by openSUSE:Factory project. This can be used
to guarantee that all checks succeed also on the service side. This plugin can be
used via project wide defined services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%install
%make_install
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
