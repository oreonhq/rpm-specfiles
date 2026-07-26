%global source0_hash 7d111ce3b1324f46a10aad86a5b44d35dcf228e63f8ffe620d4357469b77cb50

Name:           postcss-cli
Version:        11.0.1
Release:        %autorelease
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
BuildRequires:  nodejs-devel

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
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json index.js lib/ %{buildroot}%{nodejs_sitelib}/%{name}/
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}/

mkdir -p %{buildroot}%{_bindir}
# wrapper script for postcss CLI to set NODE_PATH
cat << 'EOF' > %{buildroot}%{_bindir}/postcss
#!/bin/sh
# Set NODE_PATH to the system-wide node_modules directory
export NODE_PATH="%{nodejs_sitelib}"
# Execute the actual postcss script, passing all arguments
exec %{nodejs_sitelib}/%{name}/index.js "$@"
EOF

# Make the wrapper script executable
chmod +x %{buildroot}%{_bindir}/postcss

%check
%{buildroot}%{nodejs_sitelib}/%{name}/index.js --help

%files
%doc README.md
%license LICENSE %{name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{name}/
%{_bindir}/postcss

%changelog
%autochangelog
