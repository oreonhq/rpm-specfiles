%global source0_hash 2d01a51ed2200747a64f8eb7e07e9bf8907566d08f28b302b457471b6625cca4

%global jsname jquery-ui

Name:		js-%{jsname}
Version:	1.14.2
Release:	1%{?dist}
Summary:	jQuery user interface

License:	MIT
URL:		https://jqueryui.com/
Source0:	https://github.com/jquery/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
#		We need to bundle build dependencies since they are no
#		longer available in Fedora. This uses the same
#		technique as the js-jquery package.
Source1:	%{jsname}-%{version}-node-modules.tar.gz
#		Script to create the above sources
Source2:	create-source.sh

BuildArch:	noarch
BuildRequires:	/usr/bin/node
BuildRequires:	nodejs >= 1:16
BuildRequires:	web-assets-devel
BuildRequires:	python3
BuildRequires:	python3-rcssmin
BuildRequires:	uglify-js
Requires:	js-jquery >= 1.12.0
Requires:	web-assets-filesystem

%description
A curated set of user interface interactions, effects, widgets, and
themes built on top of the jQuery JavaScript Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{jsname}-%{version} -a 1
rm -rf dist

%build
./node_modules/grunt-cli/bin/grunt -v requirejs:js concat:css

# Provide a compressed version of the javascript file
uglifyjs dist/jquery-ui.js -c -m --comments '/! jQuery UI/' > dist/jquery-ui.min.js

# Provide a compressed version of the cascading style sheet
python3 -m rcssmin -b < dist/jquery-ui.css > dist/jquery-ui.min.css

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}
install -m 644 -p dist/* %{buildroot}%{_jsdir}/%{jsname}
mkdir -p %{buildroot}%{_jsdir}/%{jsname}/images
install -m 644 -p themes/base/images/* %{buildroot}%{_jsdir}/%{jsname}/images

%files
%{_jsdir}/%{jsname}
%license LICENSE.txt
%doc AUTHORS.txt CONTRIBUTING.md README.md

%changelog
%autochangelog
