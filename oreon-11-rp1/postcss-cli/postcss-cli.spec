%global source0_hash 3d06063483b1984cd8d1c2496f610e505a0cd9e4dbe46019c029cb2ba92a9696
Name:           postcss-cli
Version:        12.0.0
Release:        1%{?dist}
Summary:        CLI for postcss, which transforms CSS styles with JS plugins
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            https://postcss.org
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz
Source1:        %{name}-%{version}-nm-prod.tgz
Source2:        %{name}-%{version}-nm-dev.tgz
Source3:        %{name}-%{version}-bundled-licenses.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       nodejs
# oreon:deps
BuildRequires:  nodejs-devel
# /oreon:deps
%description
PostCSS CLI is a command line interface for PostCSS, a tool for transforming
styles with JS plugins. These plugins can lint your CSS, support variables and
mixins, transpile future CSS syntax, inline images, and more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n package
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
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json index.js lib/ %{buildroot}%{nodejs_sitelib}/%{name}/
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}/
mkdir -p %{buildroot}%{_bindir}
cat << 'EOF' > %{buildroot}%{_bindir}/postcss
export NODE_PATH="%{nodejs_sitelib}"
exec %{nodejs_sitelib}/%{name}/index.js "$@"
EOF
chmod +x %{buildroot}%{_bindir}/postcss
%oreon_autofiles main

%check

%{buildroot}%{nodejs_sitelib}/%{name}/index.js --help
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
