%global source0_hash 0cdda09c846add76ad4891e26d69c7c0d41769b6d590b7ef66ede05230a3a24e

%global service download_files

Name:           obs-service-%{service}
Version:        0.9.2
Release:        7%{?dist}
Summary:        An OBS source service: download files

License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
# tests
BuildRequires:  /usr/bin/prove
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(File::Type)
BuildRequires:  obs-build
Requires:       diffutils
Requires:       wget
# for appimage parser:
Requires:       perl(YAML::XS)

%description
This is a source service for openSUSE Build Service.

This service is parsing all spec files and downloads all
Source files which are specified via http, https, or ftp URLs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
perl -p -i -e "s{#!/usr/bin/env bash}{#!/bin/bash}" download_files

%install
%make_install

%check
%make_build test

%files
%license COPYING
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*

%changelog
%autochangelog
