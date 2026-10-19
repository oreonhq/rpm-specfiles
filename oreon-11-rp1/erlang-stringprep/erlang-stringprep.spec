%global source0_hash bc74b00da6ffff415d1e088473802932131abcb16cfd89f2eafb47d9e6b562f9
%global srcname stringprep
%global p1_utils_ver 1.0.28
Name: erlang-%{srcname}
Version: 1.0.34
Release:        1%{?dist}
License: Apache-2.0 and TCL
Summary:        A framework for preparing Unicode strings to help input and comparison
URL: https://github.com/processone/stringprep/
VCS: git:%{url}.git
Source0:        https://github.com/processone/%{srcname}//archive/%{version}/%{srcname}-%{version}.tar.gz
Provides: erlang-p1_stringprep = %{version}-%{release}
Obsoletes: erlang-p1_stringprep < 1.0.3
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
