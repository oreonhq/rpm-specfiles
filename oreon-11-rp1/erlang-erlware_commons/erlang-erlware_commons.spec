%global source0_hash a175fb07146912dea9d3ada2fa7a0d123d2d7d73c6cffa6d90d15ade74f4eda1
%global realname erlware_commons
Name:     erlang-%{realname}
Version:  1.9.1
Release:        1%{?dist}
Summary:        Extension to Erlang's standard library
License:  MIT
URL:      https://github.com/erlware/%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/erlware/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:    erlang-erlware_commons-0001-Disable-color-test.patch
Patch:    erlang-erlware_commons-0002-Use-correct-version-instead-of-relying-to-git-one.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  erlang-cf
BuildRequires:  erlang-rebar3
BuildRequires:  git-core
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
