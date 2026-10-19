%global source0_hash 11ff33cf1bb4fe121665ba7a159518689c0b656695f2ff4e0cd2d3f8d64ed30e
%global realname erlsom
Name:		erlang-%{realname}
Version:	1.5.2
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Support for XML Schema in Erlang
License:	LGPL-3.0-or-later
URL:		https://github.com/willemdj/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/willemdj/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Erlsom is a set of functions to deal with XML Schema (XSDs) in Erlang.
First you 'compile' the schema, and after that you can parse XML
documents that conform to the schema. The result is a structure of
Erlang records, based on the types that are defined by the Schema.
Or, the other way around, a structure of records can be translated
to an XML document.

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
