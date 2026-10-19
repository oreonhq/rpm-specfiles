%global source0_hash 6c9e3addef7a755d0f0431a09e9719c3d57c17a52d1d743b184681bbf9ab3bc8
%global mmm_modules_dir %{nodejs_sitelib}/magicmirror/modules
%global srcname MMM-AirNow
%global srcversion 1.0.0
%global forgeurl https://github.com/nigel-daniels/%{srcname}
%global commit efddeb369d4bb454194e7ed5bb48d38f06c890a9
%global date 20200824
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           magicmirror-module-airnow
Version:        %{srcversion}^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        MagicMirror² module to show air quality based on the US AirNow API
License:        Apache-2.0 and BSD and ISC and MIT and Unlicense
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Source1:        %{srcname}-%{srcversion}-nm-prod.tgz
Source2:        %{srcname}-%{srcversion}-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       magicmirror
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
# /oreon:deps
%description
This is a module for the MagicMirror. This module shows air quality based on
the US AirNow API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{commit}
cp %{SOURCE2} .

%build

tar xfz %{SOURCE1}
rm -r node_modules_prod/performance-now/test/
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd
%install
mkdir -p %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr package.json airnow.css airquality.png *.js \
  %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr node_modules node_modules_prod %{buildroot}%{mmm_modules_dir}/%{srcname}
%oreon_autofiles main

%check

%nodejs_symlink_deps --check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
