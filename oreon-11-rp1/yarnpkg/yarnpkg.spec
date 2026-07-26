%global source0_hash none

%global debug_package %{nil}
%global npm_name yarn

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

# don't require bundled modules
%global __requires_exclude_from ^(%{nodejs_sitelib}/yarn/lib/.*|%{nodejs_sitelib}/yarn/bin/yarn(|\\.cmd|\\.ps1|pkg.*))$

%global bundledate 20260308

Name:           yarnpkg
Version:        1.22.22
Release:        17%{?dist}
Summary:        Fast, reliable, and secure dependency management.
License:        BSD-2-Clause
URL:            https://github.com/yarnpkg/yarn
# we need tarball with node_modules
Source0:        %{name}-v%{version}-bundled-%{bundledate}.tar.gz
Source1:        yarnpkg-tarball.sh

# These are applied by yarnpkg-tarball.sh
# yarn-update-jest.prebundle.patch
# yarn-no-commitizen.prebundle.patch
# yarn-no-eslint.prebundle.patch

Patch0:         CVE-2023-26136.patch
Patch1:         CVE-2022-37599.patch
Patch2:         CVE-2024-4067.patch
# https://github.com/yarnpkg/yarn/commit/97731871e674bf93bcbf29e9d3258da8685f3076.patch
Patch3:         CVE-2025-8262.patch
# https://github.com/form-data/form-data/commit/3d1723080e6577a66f17f163ecd345a21d8d0fd0
Patch4:         CVE-2025-8263.patch

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
%autosetup -p1 -n %{npm_name}-%{version}

%build
# use build script
npm run build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib bin node_modules \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarnpkg
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarn

# Fix the shebang in yarn.js because brp-mangle-shebangs fails to detect this properly (rhbz#1998924)
sed -e "s|^#!/usr/bin/env node$|#!/usr/bin/node|" \
    -i %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js

# Remove executable bits from bundled dependency tests
find %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules \
    -ipath '*/test/*' -type f -executable \
    -exec chmod -x '{}' +

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
if [[ $(%{buildroot}%{_bindir}/yarnpkg --version) == %{version} ]] ; then echo PASS; else echo FAIL && exit 1; fi
if [[ $(%{buildroot}%{_bindir}/yarn --version) == %{version} ]] ; then echo PASS; else echo FAIL && exit 1; fi
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/yarnpkg
%{_bindir}/yarn
%{nodejs_sitelib}/%{npm_name}/

%changelog
%autochangelog
