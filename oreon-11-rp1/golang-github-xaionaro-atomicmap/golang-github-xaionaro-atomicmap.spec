%global source0_hash d399d6cd4079abeec98f018f2aa413990a8b8ff8a7fb0dc0bfeb6f4bf849371a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xaionaro-go/atomicmap
%global commit          96a7f1f95a7093253c3ca2a9dad34e56b63ea6a2
%gometa
%global common_description %{expand:
A high performance thread-safe implementation of hash map for Golang (accent on
high throughput, not at latency).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        High performance thread-safe implementation of hash map for Go
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/atomicmap-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/OneOfOne/xxhash)
BuildRequires:  golang(github.com/cornelk/hashmap)
BuildRequires:  golang(github.com/xaionaro-go/spinlock)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
