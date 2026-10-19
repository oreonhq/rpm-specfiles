%global source0_hash d03f688dabaae408ab6d8a5d827adb594eba1c2f07d18da088e7ba8a960fd171
%global realname gpb
Name:		erlang-%{realname}
Version:	5.0.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A Google Protobuf implementation for Erlang
License:	LGPL-2.1-or-later AND BSD-3-Clause
URL:		https://github.com/tomas-abrahamsson/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/tomas-abrahamsson/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	protoc-erl
Obsoletes:	erlang-protobuffs < 0.9.3
Provides:	erlang-protobuffs = %{version}-%{release}
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
echo "%{version}" > gpb.vsn

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/protoc-erl
cp -arv priv/ %{buildroot}%{erlang_appdir}/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
