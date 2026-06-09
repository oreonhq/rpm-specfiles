%global source0_hash 6eb10e336e4e17838eaaabe1f4a02657bc846649d738a2902ac4edc1b2c70556
%global source1_hash adede9430271d0fc6026e690dd69bd17c7d357cf069c950c7ef275a0e457b738

%{?nodejs_find_provides_and_requires}
%global npm_name nodemon

# Disable until dependencies are bundled
%global enable_tests 0

Name:          nodejs-%{npm_name}
Version:       3.1.14
Release:       %autorelease
Summary:       Simple monitor script for use during development of a node.js app
License:       ISC AND MIT
URL:           https://github.com/remy/nodemon
Source0:        https://github.com/remy/nodemon/archive/v%{version}.tar.gz#/%{npm_name}-v%{version}.tar.gz
Source1:        nodemon-v%{version}-bundled.tar.gz


BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm

# Let the nodemon work with any nodejs version available
%global __requires_exclude ^\/usr\/bin\/node
Requires:      nodejs(engine)
Suggests:      nodejs

ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Simple monitor script for use during development of a node.js app.

For use during development of a node.js based application.

nodemon will watch the files in the directory in which nodemon
was started, and if any files change, nodemon will automatically
restart your node application.

nodemon does not require any changes to your code or method of
development. nodemon simply wraps your node application and keeps
an eye on any files that have changed. Remember that nodemon is a
replacement wrapper for node, think of it as replacing the word "node"
on the command line when you run your script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{npm_name}-%{version}
tar xzf %{SOURCE1}
%build

# nothing to do
# tarball is bundled in --production mode, so no need to prune

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr doc bin lib package.json website node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/nodemon.js %{buildroot}%{_bindir}/nodemon


#%%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
npm run test
%endif

%files
%doc CODE_OF_CONDUCT.md doc faq.md README.md
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/nodemon

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.14-1
- Import
