%global source0_hash 7d569961dbeeae2698a33b4f8f0e7b600ee7400710cb2a33a8148b764905ba5f

%global mmm_modules_dir %{nodejs_sitelib}/magicmirror/modules

%global srcname MMM-SingleStock

Name:           magicmirror-module-singlestock
Version:        2.1.1
Release:        %autorelease
Summary:        MagicMirror² module that displays the stock price of a single company

License:        MIT
URL:            https://github.com/balassy/MMM-SingleStock
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Backport of https://github.com/balassy/MMM-SingleStock/commit/66793e00483b65d7caecdf1236bca35118cb1df0
Patch0:         MMM-SingleStock-minimized-colorized.patch
Source1:        %{srcname}-%{version}-nm-prod.tgz
Source2:        %{srcname}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel
Requires:       magicmirror

%description
This is a module for MagicMirror² to display a single stock price without any
fancy animation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
cp %{SOURCE2} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
popd

%install
mkdir -p %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr package.json %{srcname}.js translations \
  %{buildroot}%{mmm_modules_dir}/%{srcname}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{mmm_modules_dir}/%{srcname}

%check
%nodejs_symlink_deps --check

%files
%doc CHANGELOG.md README.md doc
%license LICENSE %{srcname}-%{version}-bundled-licenses.txt
%{mmm_modules_dir}/%{srcname}

%changelog
%autochangelog
