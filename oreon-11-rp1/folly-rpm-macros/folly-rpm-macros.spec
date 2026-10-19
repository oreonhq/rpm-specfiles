%global source0_hash none
Name:           folly-rpm-macros
Version:        37
Release:        1%{?dist}
Summary:        Common RPM macros for the Folly stack
License:        MIT
URL:            https://src.fedoraproject.org/rpms/folly-rpm-macros
Source0:        macros.folly-rpm
Source1:        macros.folly-srpm
BuildArch:      noarch
Requires:       rpm
# oreon:deps

# /oreon:deps
%description

%package -n folly-srpm-macros
Summary:        RPM macros for building Folly source packages
Requires:       rpm
%description -n folly-srpm-macros

This package contains the macros needed for building Folly source packages.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0} %{SOURCE1}
%oreon_autofiles folly-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n folly-srpm-macros -f %{oreon_filedir}/folly-srpm-macros.list

%changelog

%autochangelog
