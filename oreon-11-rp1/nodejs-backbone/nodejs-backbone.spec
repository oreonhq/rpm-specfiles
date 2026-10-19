%global source0_hash 8e0809508f06e7e0f9cfd3a30c4946ac6654afff86e9f4fd6bfb582369e8a2a1
%global modname backbone
%bcond_with tests
Name:           nodejs-%{modname}
Version:        1.6.1
Release:        1%{?dist}
Summary:        Models, Views, Collections, and Events for JavaScript applications (Nodejs module)
License:        MIT
URL:            http://backbonejs.org/
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
Source1:        tests-%{version}.tar.bz2
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       js-%{modname} = %{version}-%{release}
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-qunit
BuildRequires:  npm
BuildRequires:  uglify-js
BuildRequires:  web-assets-devel
# /oreon:deps
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
%endif
%install
mkdir -p %{buildroot}%{_jsdir}/%{modname}
cp -p backbone.js backbone-min.js backbone-min.js.map %{buildroot}%{_jsdir}/%{modname}/
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -p backbone.js package.json %{buildroot}%{nodejs_sitelib}/%{modname}/
%nodejs_symlink_deps
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n js-backbone -f %{oreon_filedir}/js-backbone.list

%changelog

%autochangelog
