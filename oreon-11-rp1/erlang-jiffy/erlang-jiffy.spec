%global source0_hash f0accdb3ec1b651afdacc92e72a99fa2fdb4f8bcd21a05ee845071ddaa263949
%global realname jiffy
Name:           erlang-%{realname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Erlang JSON parser
SourceLicense:  MIT AND BSD-3-Clause AND BSD-3-Clause-Modification
License:        MIT
URL:            https://github.com/davisp/%{realname}
VCS:            git:%{url}.git
Source0:        https://github.com/davisp/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:          erlang-jiffy-0001-Use-double-conversion-from-the-system.patch
Provides:       %{realname} = %{version}
Obsoletes:      %{realname} < %{version}
# oreon:deps
BuildRequires:  double-conversion-devel
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc-c++
# /oreon:deps
%description
A JSON parser for Erlang implemented as a NIF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}
# Use double conversion from the system instead of the bundled one
rm -r c_src/double-conversion

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
