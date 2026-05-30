%global source0_hash 744d9f31fe424514dd44728daa3e562a703fca53b6627ddeb655f77c2aa88ab4

%{?nodejs_find_provides_and_requires}

#enable/disable tests in case the deps aren't there
%bcond_with tests

Name:           uglify-js
Version:        3.19.3
Release:        6%{?dist}
Summary:        JavaScript parser, mangler/compressor and beautifier toolkit
License:        BSD-2-Clause
URL:            https://github.com/mishoo/UglifyJS
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Provides:       nodejs-uglify-js = %{version}-%{release}

Provides:       uglify-js3 = %{version}-%{release}
Obsoletes:      uglify-js3 < 3.14.5-2

Provides:       nodejs-uglify-js3 = %{version}-%{release}

BuildRequires:  /usr/bin/node
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel

%if %{with tests}
BuildRequires:  npm(acorn)
BuildRequires:  npm(semver)
%endif

Requires:       js-uglify = %{version}-%{release}

%description
JavaScript parser, mangler/compressor and beautifier toolkit.

This package ships the uglifyjs command-line tool and a library suitable for
use within Node.js.

%package -n js-uglify
Summary:        JavaScript parser, mangler/compressor and beautifier toolkit - core library

Provides:       js-uglify3 = %{version}-%{release}
Obsoletes:      js-uglify3 < 3.14.5-2

Provides:       uglify-js-common = %{version}-%{release}
Obsoletes:      uglify-js-common < 2.2.5-4

Requires:       web-assets-filesystem

%description -n js-uglify
JavaScript parser, mangler/compressor and beautifier toolkit.

This package ships a JavaScript library suitable for use by any JavaScript
runtime.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n package

chmod 0755 bin/uglifyjs

%build
#nothing to do


%install
mkdir -p %{buildroot}%{_jsdir}/%{name}-3
cp -pr lib/* %{buildroot}%{_jsdir}/%{name}-3
ln -s %{name}-3 %{buildroot}%{_jsdir}/%{name}

#compat symlink
mkdir -p %{buildroot}%{_datadir}
ln -rs %{buildroot}%{_jsdir}/%{name} %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{nodejs_sitelib}/uglify-js@3
cp -pr bin tools package.json %{buildroot}%{nodejs_sitelib}/uglify-js@3
ln -rs %{buildroot}%{_jsdir}/%{name}-3 \
       %{buildroot}%{nodejs_sitelib}/uglify-js@3/lib
# Fix for rpmlint.
sed -i -e 's|^#! */usr/bin/env node|#!/usr/bin/node|' \
  %{buildroot}%{nodejs_sitelib}/uglify-js@3/bin/uglifyjs
chmod 755 %{buildroot}%{nodejs_sitelib}/uglify-js@3/bin/uglifyjs

mkdir -p %{buildroot}%{_bindir}
ln -rs %{buildroot}%{nodejs_sitelib}/uglify-js@3/bin/uglifyjs \
       %{buildroot}%{_bindir}/uglifyjs-3
ln -s uglifyjs-3 %{buildroot}%{_bindir}/uglifyjs

%nodejs_symlink_deps

ln -s uglify-js@3 %{buildroot}%{nodejs_sitelib}/uglify-js


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if %{with tests}
# Prevent timeout error on an ARM builder which is slower than the x86 builder.
sed -i '/timeout/ s/5000/10000/' test/mocha/cli.js
sed -i '/timeout/ s/10000/20000/' test/mocha/let.js
sed -i '/timeout/ s/20000/40000/' test/mocha/spidermonkey.js
NODE_DISABLE_COLORS=true %{__nodejs} test/run-tests.js
%endif


%pretrans -p <lua>
st = posix.stat("%{nodejs_sitelib}/uglify-js")
if st and st.type == "directory" then
  os.execute("rm -rf %{nodejs_sitelib}/uglify-js")
end


%pretrans -n js-uglify -p <lua>
st = posix.stat("%{_datadir}/%{name}")
if st and st.type == "directory" then
  os.execute("rm -rf %{_datadir}/%{name}")
end


%files
%{nodejs_sitelib}/uglify-js
%{nodejs_sitelib}/uglify-js@3
%{_bindir}/uglifyjs-3
%{_bindir}/uglifyjs


%files -n js-uglify
%{_jsdir}/%{name}-3
%{_jsdir}/%{name}
%{_datadir}/%{name}
%doc README.md
%license LICENSE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.19.3-6
- Prepare for Oreon 11 (RP1)
