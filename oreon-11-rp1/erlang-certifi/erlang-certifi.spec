%global source0_hash 71d31daaff3bdf6b7aacc19a24ff975b083a1620c9f052a669a113c54b56f442
%global realname certifi
Name:     erlang-%{realname}
Version:  2.17.0
Release:        1%{?dist}
BuildArch:noarch
Summary:        Dummy certifi (certificate bundle) package for erlang
License:  BSD-3-Clause
URL:      https://github.com/%{realname}/erlang-%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/%{realname}/%{name}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:   erlang-certifi-0001-Enforce-Fedora-CA-bundle.patch
# oreon:deps
BuildRequires:  erlang-parse_trans
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Upstream certifi provides a custom CA bundle to erlang. Since custom CA bundles
cannot be packaged in Fedora, this 'dummy' package patches certifi to point to
the default Fedora CA bundle.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n erlang-%{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
