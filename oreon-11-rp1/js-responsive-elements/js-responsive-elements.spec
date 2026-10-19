%global source0_hash 04bc46ba03e0f6444373a5e7ee8f9f50897b340aa04e69b77c2aeeb2daab9ee2
Name:       js-responsive-elements
Version:    1.0.2
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        A library that helps element to adapt and respond to the area they occupy
URL:        https://github.com/kumailht/responsive-elements
Source0:        https://github.com/kumailht/responsive-elements/archive/%{version}/%{name}-%{version}.tar.gz
Requires:      js-jquery
Requires:      web-assets-filesystem
# oreon:deps
BuildRequires:  web-assets-devel
# /oreon:deps
%description
Responsive elements makes it possible for any element to adapt and
respond to the area they occupy. It's a tiny javascript library that you
can drop into your projects today.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir responsive-elements-%{version}
%oreon_prep
%install
install -d -m 0755 %{buildroot}/%{_jsdir}
install -d -m 0755 %{buildroot}/%{_jsdir}/responsive-elements
install -D -p -m 0644 *.js %{buildroot}/%{_jsdir}/responsive-elements/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
