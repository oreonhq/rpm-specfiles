%global source0_hash 693b753855ea9b781b177d27b7e13999700e558b4dabbda8ade6b147ccbdb9de

%global obsroot /usr/lib/obs
%global obssvcroot %{obsroot}/service

%global srcname obs-service-source_validator

Name:           osc-source_validator
Version:        0.42
Release:        3%{?dist}
License:        GPL-2.0-or-later
Summary:        OBS source service to validate sources
URL:            https://github.com/openSUSE/obs-service-source_validator
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Build)
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

# TODO: Rename this package...
Provides:       %{srcname} = %{version}-%{release}

%description
This is a source service for openSUSE Build Service.

This service runs all checks as required by openSUSE:Factory project. This can be used
to guarantee that all checks succeed also on the service side. This plugin can be
used via project wide defined services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
# Nothing to do

%install
%make_install

%check
%make_build test

%files
%license COPYING
%{obssvcroot}/*

%changelog
%autochangelog
