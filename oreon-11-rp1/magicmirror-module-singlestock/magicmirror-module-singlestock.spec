%global source0_hash 1222f0f8e26a2ca3c20414a507de385e3caf78b907b7dba49fcc9d9da4649280
%global mmm_modules_dir %{nodejs_sitelib}/magicmirror/modules
%global srcname MMM-SingleStock
Name:           magicmirror-module-singlestock
Version:        2.1.1
Release:        1%{?dist}
Summary:        MagicMirror² module that displays the stock price of a single company
License:        MIT
URL:            https://github.com/balassy/MMM-SingleStock
Source0:        https://github.com/balassy/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         MMM-SingleStock-minimized-colorized.patch
Source1:        %{srcname}-%{version}-nm-prod.tgz
Source2:        %{srcname}-%{version}-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       magicmirror
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
# /oreon:deps
%description
This is a module for MagicMirror² to display a single stock price without any
fancy animation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
cp %{SOURCE2} .

%build

tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
popd
%install
mkdir -p %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr package.json %{srcname}.js translations \
  %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr node_modules node_modules_prod %{buildroot}%{mmm_modules_dir}/%{srcname}
%oreon_autofiles main

%check

%nodejs_symlink_deps --check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
