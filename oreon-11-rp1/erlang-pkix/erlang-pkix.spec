%global source0_hash da6279d3f8ee31ef04de2b82fb0d42ce8dcd72cedb9a8e6ae7b18e42590cb108
%global srcname pkix
Name:       erlang-%{srcname}
Version:    1.0.10
Release:        1%{?dist}
BuildArch:  noarch
License:    Apache-2.0
Summary:        PKIX certificates management for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires: ca-certificates
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
A library for managing TLS certificates in Erlang.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf ./rebar ./rebar.config ./rebar.config.script

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -d -m 0755 %{buildroot}/%{erlang_appdir}/priv
ln -s /etc/pki/tls/certs/ca-bundle.trust.crt %{buildroot}/%{erlang_appdir}/priv/cacert.pem
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
