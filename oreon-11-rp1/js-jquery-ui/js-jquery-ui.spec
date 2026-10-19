%global source0_hash f1d6551af256a1c6546784ce9049da7c3d57007f1237e249a1d38e4f956da1ff
%global jsname jquery-ui
Name:		js-%{jsname}
Version:	1.14.2
Release:        1%{?dist}
Summary:        jQuery user interface
License:	MIT
URL:		https://jqueryui.com/
Source0:        https://github.com/jquery/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
Source1:	%{jsname}-%{version}-node-modules.tar.gz
Source2:	create-source.sh
BuildArch:	noarch
Requires:	js-jquery >= 1.12.0
Requires:	web-assets-filesystem
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  nodejs
BuildRequires:  python3
BuildRequires:  python3-rcssmin
BuildRequires:  uglify-js
BuildRequires:  web-assets-devel
# /oreon:deps
%description
A curated set of user interface interactions, effects, widgets, and
themes built on top of the jQuery JavaScript Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{jsname}-%{version} -a 1
rm -rf dist

%build

./node_modules/grunt-cli/bin/grunt -v requirejs:js concat:css
uglifyjs dist/jquery-ui.js -c -m --comments '/! jQuery UI/' > dist/jquery-ui.min.js
python3 -m rcssmin -b < dist/jquery-ui.css > dist/jquery-ui.min.css
%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}
install -m 644 -p dist/* %{buildroot}%{_jsdir}/%{jsname}
mkdir -p %{buildroot}%{_jsdir}/%{jsname}/images
install -m 644 -p themes/base/images/* %{buildroot}%{_jsdir}/%{jsname}/images
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
