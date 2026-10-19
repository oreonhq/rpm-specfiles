%global source0_hash efbfebd86797eb7d78cca6cf27a90e1424d958a21c7e8603dc0bf94f5d9e9c46
%global realname ebloom
Name:		erlang-%{realname}
Version:	2.1.0
Release:        1%{?dist}
Summary:        A NIF wrapper around a basic bloom filter
License:	Apache-2.0 AND CPL-1.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
rm -f rebar.config

%build

%{erlang3_compile}
mkdir -p ./priv
g++ c_src/ebloom_nifs.cpp $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/ebloom_nifs.o
g++ c_src/ebloom_nifs.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/ebloom_nifs.so
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
