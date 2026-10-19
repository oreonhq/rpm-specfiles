%global source0_hash 9053c272ee224aa95db2fdee47c852ff6d67b33834347aa902b7f1b30c35e9df
%global npm_name cssnano-preset-advanced
Name:           nodejs-%{npm_name}
Version:        9.0.5
Release:        1%{?dist}
Summary:        Advanced optimisations for cssnano; may or may not break your CSS!
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-4.0 AND ISC AND MIT
URL:            https://github.com/cssnano-preset-advanced/%{npm_name}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       nodejs
Requires:       nodejs-cssnano
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
# /oreon:deps
%description
Cssnano is a modern, modular compression tool written on top of the PostCSS
ecosystem, which allows us to use a lot of powerful features in order to
compact CSS appropriately. This package is a preset for cssnano that
provides advanced optimisations, which may or may not break your CSS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{npm_name}
%oreon_autofiles main

%check

%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
