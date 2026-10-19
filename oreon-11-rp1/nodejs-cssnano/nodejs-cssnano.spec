%global source0_hash 7ea51b40245bc5ec70ecd15c4101bbd6c57d1851b7b01695d8fb318ace2863aa
%global npm_name cssnano
Name:           nodejs-%{npm_name}
Version:        9.0.5
Release:        1%{?dist}
Summary:        A modular minifier, built on top of the PostCSS ecosystem
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-4.0 AND ISC AND MIT
URL:            https://github.com/cssnano/%{npm_name}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       nodejs
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
# /oreon:deps
%description
Cssnano is a modern, modular compression tool written on top of the PostCSS
ecosystem, which allows us to use a lot of powerful features in order to
compact CSS appropriately.

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
