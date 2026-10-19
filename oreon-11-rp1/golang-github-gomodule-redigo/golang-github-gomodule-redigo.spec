%global source0_hash b97a9b0298c371c80b4ba141cb683eaa003c8825a5b02526a03435f6e7568289
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/gomodule/redigo
Version:                2.0.0
%gometa
%global goaltipaths     github.com/garyburd/redigo
%global common_description %{expand:
Redigo is a Go client for the Redis database.
Features:
 - A Print-like API with support for all Redis commands.
 - Pipelining, including pipelined transactions.
 - Publish/Subscribe.
 - Connection pooling.
 - Script helper type with optimistic use of EVALSHA.
 - Helper functions for working with command replies.}
%gometa
%global golicenses      LICENSE
%global godocs          README.markdown
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Go client for redis
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/redigo-%{version}.tar.gz
Source1:        glide.lock
Source2:        glide.yaml
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
