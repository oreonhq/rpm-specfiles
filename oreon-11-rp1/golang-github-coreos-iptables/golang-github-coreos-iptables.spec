%global source0_hash 77eb68017d6e5257759f8b6f4de9541a8ac59d384dbcc66f8a2e9def475391e3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/coreos/go-iptables
Version:                0.8.0
%gometa
%global common_description %{expand:
Go bindings for iptables utility.
In-kernel netfilter does not have a good userspace API. The tables are
manipulated via setsockopt that sets/replaces the entire table. Changes to
existing table need to be resolved by userspace code which is difficult and
error-prone. Netfilter developers heavily advocate using iptables utlity for
programmatic manipulation.
go-iptables wraps invocation of iptables utility with functions to append and
delete rules; create, clear and delete chains.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md code-of-conduct.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go wrapper around iptables utility
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-iptables-%{version}.tar.gz
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

%gocheck -d iptables
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
