%global source0_hash 8b5ac3ae87155c5d37828d3685bd285871fd1b8df1c67387ab38cb81be09f5e4

%global modname backbone

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

# tests are disabled for now (need QUnit, runs in PhantomJS?)
%bcond_with tests

Name:           nodejs-%{modname}
Version:        1.3.3
Release:        23%{?dist}
Summary:        Models, Views, Collections, and Events for JavaScript applications (Nodejs module)
License:        MIT
URL:            http://backbonejs.org/
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
# git archive --format=tar --prefix=test/ 1.3.3:test/ | bzip2 >tests-1.3.3.tar.bz2
Source1:        tests-%{version}.tar.bz2
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel
BuildRequires:  uglify-js
Requires:       js-%{modname} = %{version}-%{release}
%if %{with tests}
BuildRequires:  nodejs
BuildRequires:  nodejs-qunit
%endif

%description
Backbone supplies structure to JavaScript-heavy applications by providing 
models key-value binding and custom events, collections with a rich API of 
enumerable functions, views with declarative event handling, and connects it 
all to your existing application over a RESTful JSON interface.

This package provides Backbone as a Nodejs module, for use in server-side 
applications or with browserify.

%package -n js-%{modname}
Summary:        Models, Views, Collections and Events for JavaScript applications
Requires:       web-assets-filesystem

%description -n js-%{modname}
Backbone supplies structure to JavaScript-heavy applications by providing 
models key-value binding and custom events, collections with a rich API of 
enumerable functions, views with declarative event handling, and connects it 
all to your existing application over a RESTful JSON interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n package
%setup -q -T -D -a 1 -n package
rm backbone-min.{js,map}

%build
uglifyjs backbone.js -m --source-map -o backbone-min.js

%if %{with tests}
%check
%nodejs_symlink_deps --check
# ?
%endif

%install
mkdir -p %{buildroot}%{_jsdir}/%{modname}
cp -p backbone.js backbone-min.js backbone-min.js.map %{buildroot}%{_jsdir}/%{modname}/
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -p backbone.js package.json %{buildroot}%{nodejs_sitelib}/%{modname}/
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/%{modname}

%files -n js-%{modname}
%doc README.md
%license LICENSE
%{_jsdir}/%{modname}

%changelog
%autochangelog
