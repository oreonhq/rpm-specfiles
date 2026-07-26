%global source0_hash 45da5af75c0aadb20983f73fb21c377492b4c7b467fbf2670becc5a69b5e10c3

%global commit 4bc009145202d9c7483ba85f3a236a8f3470354d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global jsname jquery-ui-touch-punch

Name:		js-%{jsname}
Version:	0.2.3
Release:	0.22.20141219git%{shortcommit}%{?dist}
Summary:	Touch Event Support for jQuery UI

# Automatically converted from old format: MIT or GPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-MIT OR GPL-2.0-only
URL:		http://touchpunch.furf.com/
Source0:	https://github.com/furf/%{jsname}/archive/%{commit}/%{jsname}-%{version}-%{shortcommit}.tar.gz

BuildArch:	noarch
BuildRequires:	uglify-js
BuildRequires:	web-assets-devel
Requires:	js-jquery >= 1.6
Requires:	js-jquery-ui >= 1.8
Requires:	web-assets-filesystem

%description
jQuery UI Touch Punch is a small hack that enables the use of touch
events on sites using the jQuery UI user interface library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{jsname}-%{commit}

# Remove pre-minified script
rm *.min.js

%build
# Minify script
uglifyjs jquery.ui.touch-punch.js -c -m --comments '/^!/' \
      -o jquery.ui.touch-punch.min.js

%install
mkdir -p %{buildroot}/%{_jsdir}/%{jsname}
install -m 644 -p *.js %{buildroot}/%{_jsdir}/%{jsname}

%files
%{_jsdir}/%{jsname}
%doc README.md

%changelog
%autochangelog
