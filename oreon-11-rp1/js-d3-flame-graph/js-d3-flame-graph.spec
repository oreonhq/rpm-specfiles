%global source0_hash 03a847ff162cba0a457893054d89f066e630db19a43d6cf74b2c7b66766c3583
%global source1_hash 77e32d2c3f77e2e9547c99ee780303bf6080fd3da1ecd2fd6e3882ecdb3b909e

%global         pkgname d3-flame-graph
%global         github https://github.com/spiermar/d3-flame-graph

Name:           js-d3-flame-graph
Version:        5.0.0
Release:        %autorelease
Summary:        A D3.js plugin that produces flame graphs

BuildArch:      noarch

License:        Apache-2.0
URL:            %{github}

Source0:        https://github.com/spiermar/d3-flame-graph/archive/%{version}/d3-flame-graph-%{version}.tar.gz#/js-d3-flame-graph-%{version}.tar.gz
# Note: In case there were no changes to this tarball, the NVR of this tarball
# lags behind the NVR of this package.
# -3: adds @esbuild/linux-arm64 (vite on aarch64)
Source1:        js-d3-flame-graph-vendor-%{version}-3.tar.xz
Source2:        Makefile
Source3:        list_bundled_nodejs_packages.py


BuildRequires:  web-assets-devel
BuildRequires:  nodejs, /usr/bin/node

%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       web-assets-filesystem
%endif

# Bundled npm packages
Provides: bundled(npm(ajv)) = 8.18.0
Provides: bundled(npm(d3-array)) = 3.1.1
Provides: bundled(npm(d3-dispatch)) = 3.0.1
Provides: bundled(npm(d3-ease)) = 3.0.1
Provides: bundled(npm(d3-format)) = 3.0.1
Provides: bundled(npm(d3-hierarchy)) = 3.0.1
Provides: bundled(npm(d3-scale)) = 4.0.2
Provides: bundled(npm(d3-selection)) = 3.0.0
Provides: bundled(npm(d3-transition)) = 3.0.1
Provides: bundled(npm(eslint)) = 9.39.3
Provides: bundled(npm(eslint-plugin-n)) = 17.24.0
Provides: bundled(npm(eslint-plugin-promise)) = 7.2.1
Provides: bundled(npm(jsdom)) = 28.1.0
Provides: bundled(npm(prettier)) = 3.8.1
Provides: bundled(npm(vite)) = 7.3.1
Provides: bundled(npm(vite-plugin-lib-inject-css)) = 2.2.2
Provides: bundled(npm(vitest)) = 4.0.18

%description
A D3.js plugin that produces flame graphs from hierarchical data.


%package doc
Summary: Documentation and example files for js-d3-flame-graph

%description doc
Documentation and example files for js-d3-flame-graph.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -T -D -b 0 -n %{pkgname}-%{version}
%setup -q -T -D -b 1 -n %{pkgname}-%{version}



%build
./node_modules/.bin/vite build --config vite.config.mjs
./node_modules/.bin/vite build --config vite.config.min.mjs


%install
install -d -m 755 %{buildroot}/%{_jsdir}/%{pkgname}
cp -a dist/* %{buildroot}/%{_jsdir}/%{pkgname}


%check
./node_modules/.bin/vitest run


%files
%{_jsdir}/%{pkgname}

%license LICENSE
%doc README.md


%files doc
%doc README.md docs


%changelog
%autochangelog
