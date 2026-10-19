%global source0_hash 88268464199d1611fcf73ce9c0a6c4d44c7d5363682720d8506f6508addf36a0
%global debug_package %{nil}
%global npm_name yarn
%{?nodejs_find_provides_and_requires}
%global enable_tests 1
%global __requires_exclude_from ^(%{nodejs_sitelib}/yarn/lib/.*|%{nodejs_sitelib}/yarn/bin/yarn(|\\.cmd|\\.ps1|pkg.*))$
%global bundledate 20260308
Name:           yarnpkg
Version:        1.22.22
Release:        1%{?dist}
Summary:        Fast, reliable, and secure dependency management.
License:        BSD-2-Clause
URL:            https://github.com/yarnpkg/yarn
Source0:        https://github.com/yarnpkg/yarn/releases/download/v%{version}/yarn-v%{version}.tar.gz
Source1:        yarnpkg-tarball.sh
ExclusiveArch:  %{nodejs_arches}
# oreon:deps
BuildRequires:  nodejs-packaging
BuildRequires:  npm
# /oreon:deps
%description
Fast, reliable, and secure dependency management.

%prep
%global oreon_srcdir yarn-v%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json lib bin \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
mkdir -p %{buildroot}%{_bindir}
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarnpkg
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarn
sed -e "s|^#!/usr/bin/env node$|#!/usr/bin/node|" \
    -i %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
