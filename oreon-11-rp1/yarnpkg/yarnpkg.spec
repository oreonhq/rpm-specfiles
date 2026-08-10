%global source0_hash 88268464199d1611fcf73ce9c0a6c4d44c7d5363682720d8506f6508addf36a0

%global debug_package %{nil}
%global npm_name yarn

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

# don't require bundled modules
%global __requires_exclude_from ^(%{nodejs_sitelib}/yarn/lib/.*|%{nodejs_sitelib}/yarn/bin/yarn(|\\.cmd|\\.ps1|pkg.*))$

%global bundledate 20260308

Name:           yarnpkg
Version:        1.22.22
Release:        18%{?dist}
Summary:        Fast, reliable, and secure dependency management.
License:        BSD-2-Clause
URL:            https://github.com/yarnpkg/yarn
# upstream release tarball (prebuilt)
Source0: https://github.com/yarnpkg/yarn/releases/download/v%{version}/yarn-v%{version}.tar.gz
Source1:        yarnpkg-tarball.sh

ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-packaging
%if 0%{?fedora}
BuildRequires:  %{_bindir}/npm
%else
BuildRequires:  npm
%endif

%description
Fast, reliable, and secure dependency management.

%prep
%autosetup -n yarn-v%{version}

%build
# release tarball is already built

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib bin \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarnpkg
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarn

# Fix the shebang in yarn.js because brp-mangle-shebangs fails to detect this properly (rhbz#1998924)
sed -e "s|^#!/usr/bin/env node$|#!/usr/bin/node|" \
    -i %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js

%files
%doc README.md
%license LICENSE
%{_bindir}/yarnpkg
%{_bindir}/yarn
%{nodejs_sitelib}/%{npm_name}/

%changelog
%autochangelog
