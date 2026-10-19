%global source0_hash 2be4716ba2bba5f7c125a8fe72ba534f02cf0d7d98d3a372d4ebe54b170f7329
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/eapache/queue
Version:                1.1.0
%gometa
%global common_description %{expand:
A fast Golang queue using a ring-buffer, based on the version suggested by
Dariusz Górecki. Using this instead of other, simpler, queue implementations
(slice+append or linked list) provides substantial memory and time benefits,
and fewer GC pauses.
The queue implemented here is as fast as it is in part because it is not
thread-safe.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast golang queue using ring-buffer
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/queue-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
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
