%global source0_hash none
%global source0101_hash 2555db64b4ca51629f2ea3475be6b40460ac3bc900687a8e8b51f0befb0eb1a2

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           nodejs-packaging
Version:        2023.10
Release:        %autorelease
Summary:        RPM Macros and Utilities for Node.js Packaging
BuildArch:      noarch
License:        MIT
URL:            https://fedoraproject.org/wiki/Node.js/Packagers
ExclusiveArch:  %{nodejs_arches} noarch

Source0001:        LICENSE
Source0002:        README.md
Source0003:        macros.nodejs
Source0004:        multiver_modules
Source0005:        nodejs-fixdep
Source0006:        nodejs-setversion
Source0007:        nodejs-symlink-deps
Source0008:        nodejs.attr
Source0009:        nodejs.prov
Source0010:        nodejs.req

Source0111:        nodejs-packaging-bundler

# Created with `tar cfz test.tar.gz test`
Source0101:        test.tar.gz

BuildRequires:  python3

Requires:       redhat-rpm-config

%description
This package contains RPM macros and other utilities useful for packaging
Node.js modules and applications in RPM-based distributions.

%package bundler
Summary:      Bundle a node.js application dependencies
Requires:       npm
Requires:       coreutils, findutils, jq

%description bundler
nodejs-packaging-bundler bundles a node.js application node_module dependencies
It gathers the application tarball.
It generates a runtime (prod) tarball with runtime node_module dependencies
It generates a testing (dev) tarball with node_module dependencies for testing
It generates a bundled license file that gets the licenses in the runtime
dependency tarball

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source0101_hash}" = "none" || { f="%{SOURCE0101}"; test -f "$f" || { echo "oreon: missing Source0101 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0101_hash}" || { echo "oreon: Source0101 hash mismatch" >&2; exit 1; }; }cp -da %{_sourcedir}/* .
tar xvf test.tar.gz


%build
#nothing to do


%install
install -Dpm0644 macros.nodejs %{buildroot}%{macrosdir}/macros.nodejs
install -Dpm0644 nodejs.srpm.macros %{buildroot}%{macrosdir}/nodejs.srpm.macros
install -Dpm0644 nodejs.attr %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs.attr
install -pm0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -pm0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req
install -pm0755 nodejs-symlink-deps %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps
install -pm0755 nodejs-fixdep %{buildroot}%{_rpmconfigdir}/nodejs-fixdep
install -pm0755 nodejs-setversion %{buildroot}%{_rpmconfigdir}/nodejs-setversion
install -Dpm0644 multiver_modules %{buildroot}%{_datadir}/node/multiver_modules
install -Dpm0755 nodejs-packaging-bundler %{buildroot}%{_bindir}/nodejs-packaging-bundler


%check
./test/run


%files
%license LICENSE
%{macrosdir}/macros.nodejs
%{macrosdir}/nodejs.srpm.macros
%{_rpmconfigdir}/fileattrs/nodejs*.attr
%{_rpmconfigdir}/nodejs*
%{_datadir}/node/multiver_modules

%files bundler
%{_bindir}/nodejs-packaging-bundler


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2023.10-1
- Import
