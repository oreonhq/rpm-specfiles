%global source0_hash da6279d3f8ee31ef04de2b82fb0d42ce8dcd72cedb9a8e6ae7b18e42590cb108

%global srcname pkix

Name:       erlang-%{srcname}
Version:    1.0.10
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    PKIX certificates management for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3
Requires: ca-certificates

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

# pkix includes a CA bundle in priv/cacert.pem. Let's use a symlink to Fedora's CA bundle instead.
install -d -m 0755 %{buildroot}/%{erlang_appdir}/priv
ln -s /etc/pki/tls/certs/ca-bundle.trust.crt %{buildroot}/%{erlang_appdir}/priv/cacert.pem

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
