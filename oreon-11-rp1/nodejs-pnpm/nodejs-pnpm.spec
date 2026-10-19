%global source0_hash 3bb1683c7bff8bf8a810284d8b38af46ac22e2a732fca88de299fdc6b88af814
%global pkgname pnpm
Name:           nodejs-%{pkgname}
Version:        12.4.2
Release:        1%{?dist}
Summary:        Fast, disk space efficient package manager
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND ISC
URL:            https://pnpm.io
Source0:        http://registry.npmjs.org/%{pkgname}/-/%{pkgname}-%{version}.tgz
Source3:        %{pkgname}-%{version}-bundled-licenses.txt
BuildArch:      noarch
Requires:       bash
Provides:       npm(%{pkgname}) = %{version}
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
# /oreon:deps
%description

%package -n %{pkgname}
Summary:        Fast, disk space efficient package manager
%description -n %{pkgname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n package
cp %{SOURCE3} .

%build

%install
CFLAGS="%{optflags}"
export CFLAGS
CXXFLAGS="%{optflags}"
export CXXFLAGS
npm_config_prefix=%{buildroot}%{_prefix}
export npm_config_prefix
install -d %{buildroot}%{nodejs_sitearch}
npm install -g %{SOURCE0}
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}/bin/pnpm.cjs %{buildroot}%{_bindir}/pnpm
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}/bin/pnpx.cjs %{buildroot}%{_bindir}/pnpx
sed -i -e 's|#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{nodejs_sitelib}/%{pkgname}/bin/*
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules -type f -name '.*' -delete
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/.pnpm
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/balanced-match/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/cacache/node_modules/brace-expansion/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/iconv-lite/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/iconv-lite/.idea
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/node-gyp
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/node-gyp-bin
%fdupes %{buildroot}%{nodejs_sitelib}/%{pkgname}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__nodejs} -e 'require("./")' | grep "^Version %{version}"
%files -f %{oreon_filedir}/main.list
%files -n pnpm -f %{oreon_filedir}/pnpm.list

%changelog

%autochangelog
