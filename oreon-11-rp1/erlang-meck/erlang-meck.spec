%global source0_hash 423f3404602cc3dea784ff5cf95f87c9b223113407d6f3585a09919d224167a3
%global realname meck
Name:		erlang-%{realname}
Version:	1.2.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A mocking library for Erlang
License:	Apache-2.0
URL:		https://github.com/eproxus/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/eproxus/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-meck-0001-Disable-erlang-unite-test-output-highlighting.patch
Patch:		erlang-meck-0002-Temporary-disable-ex_doc-and-rebar3_ex_doc.patch
Patch:		erlang-meck-0003-Fix-tests-with-short-domain-names-default.patch
# oreon:deps
BuildRequires:  erlang-hamcrest
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-tools
# /oreon:deps
%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
