%global source0_hash 68044a9d7dc4b257c123e9077c09666477e3b938a2575d4554277d3085a176f6
Name:       js-jquery-mousewheel
Version:    3.2.2
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        A jQuery plugin that adds cross-browser mouse wheel support
URL:        https://github.com/jquery/jquery-mousewheel
Source0:        https://github.com/jquery/jquery-mousewheel/archive/%{version}.tar.gz
Requires:      js-jquery >= 1.2.2
Requires:      web-assets-filesystem
# oreon:deps
BuildRequires:  uglify-js
BuildRequires:  web-assets-devel
# /oreon:deps
%description
A jQuery plugin that adds cross-browser mouse wheel support with delta
normalization.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jquery-mousewheel-%{version}

# We must minify the JS ourselves.
find . -name "*.min.js" -delete

# https://github.com/jquery/jquery-mousewheel/pull/176
chmod a-x jquery.mousewheel.js

%build

uglifyjs -c -m --comments some jquery.mousewheel.js > jquery.mousewheel.min.js
%install
install -d -m 0755 %{buildroot}/%{_jsdir}
cp -a jquery.mousewheel*.js %{buildroot}/%{_jsdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
