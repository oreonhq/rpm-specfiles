%global source0_hash aaf0638ba78eac56b667f504433580b9edba43e861d7d8596091c8542313583b
Name:           ipv6gen
Version:        1.0
Release:        1%{?dist}
Summary:        IPv6 prefix generator
License:        GPL-2.0-only
URL:            https://github.com/vladak/%{name}
Source0:        https://github.com/vladak/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
ipv6gen is a tool which generates lists of IPv6 prefixes using the
process described by RFC 3531.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -Dp -m 0755 check-overlap.pl $RPM_BUILD_ROOT/%{_bindir}/check-overlap
install -Dp -m 0755 ipv6gen.pl       $RPM_BUILD_ROOT/%{_bindir}/ipv6gen
install -Dp -m 0644 ipv6gen.1        $RPM_BUILD_ROOT/%{_mandir}/man1/ipv6gen.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
