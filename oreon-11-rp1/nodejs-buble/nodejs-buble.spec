%global source11_hash b4287fc98a83cb9bf25c2ce4e29c62d81ebc36bbce22b4fbae534dcd5d7db87a
%global source0_hash 51e93ec8a2958ae16d9e91b1d71ca0dc79c80aa319bf1240974dd4031166112c
%global npm_name buble
%global enable_tests 0
Name:		nodejs-buble
Version:	0.20.0
Release:        12%{?dist}
Summary:        The blazing fast, batteries-included ES2015 compiler
License:	MIT
URL:		https://gitlab.com/Rich-Harris/buble
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:	tests-%{version}.tar.bz2
Source2:        %{npm_name}-%{version}-nm-prod.tgz
Source4:        %{npm_name}-%{version}-bundled-licenses.txt
Source10:	dl-tests.sh
Source11:	https://gitlab.com/Rich-Harris/buble/raw/master/rollup.config.js
BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
# /oreon:deps
%description
The blazing fast, batteries-included ES2015 compiler

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package
cp -p %{SOURCE11} .

#fix script interpreter
sed -i '1s/env //' bin/buble

cp %{SOURCE4} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE2}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json *.js bin/ dist/ \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
mkdir %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/%{npm_name} \
    %{buildroot}%{_bindir}/%{npm_name}
%oreon_autofiles main

%check

%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
