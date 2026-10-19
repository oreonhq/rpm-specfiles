%global source0_hash e34cf5e8f25fc7e59b2ff5c56fed507cf1378d4eef2a4aa7957b3c7e80812d64
%global realname rebar
%global bootstrap 0
Name:     erlang-%{realname}3
Version:  3.27.1
Release:        1%{?dist}
Summary:        Tool for working with Erlang projects
License:  Apache-2.0 and MIT
URL:      https://github.com/erlang/%{realname}3
VCS:      git:%{url}.git
Source0:        https://github.com/erlang/%{realname}3/archive/%{version}/%{realname}3-%{version}.tar.gz
Source1:  rebar3.sh
Patch:    erlang-rebar3-0001-Skip-deps.patch
Patch:    erlang-rebar3-0002-Unbundle-hex_core-ver.-0.7.1.patch
Patch:    erlang-rebar3-0003-WIP-ignore-deps-on-demand.patch
Patch:    erlang-rebar3-0004-WIP-prefer-locally-installed-plugins.patch
Patch:    erlang-rebar3-0005-WIP-don-t-update-packages-if-IGNORE_MISSING_DEPS-is-.patch
Patch:    erlang-rebar3-0006-Adjust-for-hex_code-ver.-0.15.patch
%if 0%{?bootstrap}
%else
%endif
BuildArch: noarch
Requires:	erlang-cth_readable
Requires:	erlang-eunit_formatters
Requires:	erlang-rpm-macros >= 0.3.6
# oreon:deps
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-certifi
BuildRequires:  erlang-cf
BuildRequires:  erlang-cth_readable
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-edoc
BuildRequires:  erlang-erl_interface
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-erts
BuildRequires:  erlang-eunit_formatters
BuildRequires:  erlang-getopt
BuildRequires:  erlang-hex_core
BuildRequires:  erlang-parsetools
BuildRequires:  erlang-providers
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-relx
BuildRequires:  erlang-rpm-macros
BuildRequires:  erlang-ssl_verify_fun
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}3-%{version}

%build

ebin_paths=$(perl -e 'print join(":", grep { !/rebar/} (glob("%{_libdir}/erlang/lib/*/ebin"), glob("%{_datadir}/erlang/lib/*/ebin")))')
%if 0%{?bootstrap}
DIAGNOSTIC=1 ./bootstrap bare compile --paths $ebin_paths --separator :
%else
rm -rf ./vendor
DEBUG=1 %{realname}3 bare compile --paths $ebin_paths --separator :
%endif
%install
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/rebar3
mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%if 0%{?bootstrap}
install -p -m644 _build/bootstrap/lib/rebar/ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 _build/bootstrap/lib/rebar/ebin/%{realname}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%else
install -p -m644 ./ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 ./ebin/%{realname}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
%endif
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/priv
cp -a apps/rebar/priv/templates/ %{buildroot}%{_erllibdir}/%{realname}-%{version}/priv/templates
install -D -p -m644 ./apps/rebar/priv/shell-completion/bash/%{realname}3 %{buildroot}%{bash_completions_dir}/%{realname}3
install -D -p -m644 ./apps/rebar/priv/shell-completion/fish/%{realname}3.fish %{buildroot}%{fish_completions_dir}/%{realname}3.fish
install -D -p -m644 ./apps/rebar/priv/shell-completion/zsh/_%{realname}3 %{buildroot}%{zsh_completions_dir}/_%{realname}3
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m644 manpages/%{realname}3.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

