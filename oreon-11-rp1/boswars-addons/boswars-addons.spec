%global source0_hash 508935a335fe8bddfab5b88fc93fcba78952277e878b7392d6f9b64df824a66e

Name:		boswars-addons
Version:	2.6
Release:	34%{?dist}
Summary:	Addon maps for Bos Wars real-time strategy game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.boswars.org/addons/addons.shtml
Source0:	http://www.boswars.org/addons/maps/greenlands.map.tgz
Source1:	http://www.boswars.org/addons/maps/obese.map.tgz
Source2:	http://www.boswars.org/addons/maps/obese2.map.tgz
Source3:	http://www.boswars.org/addons/maps/wargrounds.map.tgz
Source4:	http://www.boswars.org/addons/maps/wetlands03.map.tgz
BuildArch:	noarch

Requires:	boswars >= 2.6

%description
A collection of addon maps for Bos Wars real-time strategy game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n boswars-addons
%setup -q -c -n boswars-addons -T -D -a 1
%setup -q -c -n boswars-addons -T -D -a 2
%setup -q -c -n boswars-addons -T -D -a 3
%setup -q -c -n boswars-addons -T -D -a 4

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/boswars/maps
cp -a * $RPM_BUILD_ROOT%{_datadir}/boswars/maps

%files
%{_datadir}/boswars/maps/*

%changelog
%autochangelog
