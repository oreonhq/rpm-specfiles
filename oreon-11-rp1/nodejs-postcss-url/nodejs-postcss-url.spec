%global source0_hash 04ce525ed711a32eefec79ca7957172868a259cc14f2d83ea2181f799d3279d3
%global npm_name postcss-url
%define _description PostCSS plugin to rebase, inline or copy on url()
Name:           nodejs-%{npm_name}
Version:        10.1.4
Release:        1%{?dist}
Summary:        PostCSS plugin to rebase, inline or copy on url()
License:        ISC AND MIT
URL:            https://github.com/postcss/%{npm_name}
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
%{_description}.

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
