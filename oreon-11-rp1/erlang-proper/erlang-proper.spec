%global source0_hash 68fcc3b23ea98537d7a2b926de688dc347e02804c54d0f8d79ca7092c9456b68
%global realname proper
Name:       erlang-%{realname}
Version:    1.5.0
Release:        1%{?dist}
BuildArch:  noarch
License:    GPL-3.0-or-later
Summary:        A QuickCheck-inspired property-based testing tool for Erlang
URL:        https://github.com/proper-testing/%{realname}
VCS:        git:%{url}.git
Source0:        https://github.com/%{realname}-testing/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
sed -i -e "/covertool/d" ./rebar.config

%build

./scripts/make_doc
%{erlang3_compile}
ln -s _build/default/lib/proper/ebin .
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
