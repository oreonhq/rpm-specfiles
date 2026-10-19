%global source0_hash 5a9485db807704ea5526ca02d2b81cb3c3670a78dd6bb2e5d39d4c561a4a6ab4
%global plugin_name bad-behavior
%global plugin_human_name Bad Behavior
Name:		wordpress-plugin-%{plugin_name}
Version:	2.2.13
Release:        1%{?dist}
Summary:        Bad Behavior plugin for WordPress
License:	LGPL-3.0-or-later
URL:		http://www.bad-behavior.ioerror.us/
Source0:        http://downloads.wordpress.org/plugin/%{plugin_name}.%{version}.zip
Requires:	wordpress
BuildArch:	noarch
# oreon:deps

# /oreon:deps
%description
Bad Behavior is a PHP-based solution for blocking link spam and the robots
which deliver it.

Bad Behavior complements other link spam solutions by acting as a gatekeeper,
preventing spammers from ever delivering their junk, and in many cases, from
ever reading your site in the first place. This keeps your site's load down,
makes your site logs cleaner, and can help prevent denial of service conditions
caused by spammers.

Bad Behavior also transcends other link spam solutions by working in a
completely different, unique way. Instead of merely looking at the content of
potential spam, Bad Behavior analyzes the delivery method as well as the
software the spammer is using. In this way, Bad Behavior can stop spam attacks
even when nobody has ever seen the particular spam before.

Bad Behavior is designed to work alongside existing spam prevention services to
increase their effectiveness and efficiency. Whenever possible, you should run
it in combination with a more traditional spam prevention service.

This package is built for use with WordPress (wordpress), not WordPress MU.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
echo 'To enable "%{plugin_human_name}", go to the administrative section
of your blog, "Plugins", and enable the plugin there.' > README.fedora

%build

%install
rm -rf %{buildroot}
mv %{plugin_name}/{lgpl-3.0.txt,README.txt} .
rm -f %{plugin_name}/bad-behavior-{lifetype,mediawiki}.php
mkdir -p %{buildroot}%{_datadir}/wordpress/wp-content/plugins/
cp -a %{plugin_name} %{buildroot}%{_datadir}/wordpress/wp-content/plugins/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
