%global source0_hash 54ab87315c94c2fbec2b863c6155c9d148c467845756d1647b61c9c80bb1427a
%global realname webmachine
Name:		erlang-%{realname}
Version:	1.13.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A REST-based system for building web applications
License:	Apache-2.0
URL:		https://github.com/webmachine/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/%{realname}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-webmachine-0001-Enable-verbose-output-during-testing.patch
Patch:		erlang-webmachine-0002-FIXME-this-test-fails-constantly.patch
# oreon:deps
BuildRequires:  erlang-ibrowse
BuildRequires:  erlang-meck
BuildRequires:  erlang-mochiweb
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
chmod 644 src/wmtrace_resource.erl
chmod -x priv/trace/wmtrace.css
chmod -x priv/trace/wmtrace.js

%build

%{erlang3_compile}
%install
%{erlang3_install}
cp -arv priv %{buildroot}%{erlang_appdir}/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
