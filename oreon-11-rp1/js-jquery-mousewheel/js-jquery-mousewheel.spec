%global source0_hash e54e2b5d8f2a492c2c7bb4552e10fa67601ae3faf96d759e869860f995fb642a

Name:       js-jquery-mousewheel
Version:    3.1.13
Release:    20%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    A jQuery plugin that adds cross-browser mouse wheel support
URL:        https://github.com/jquery/jquery-mousewheel
Source0:    %{url}/archive/%{version}.tar.gz

BuildRequires: uglify-js
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.2.2
Requires:      web-assets-filesystem

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

%files
%license LICENSE.txt
%doc ChangeLog.md
%doc README.md
%{_jsdir}/jquery.mousewheel*.js

%changelog
%autochangelog
