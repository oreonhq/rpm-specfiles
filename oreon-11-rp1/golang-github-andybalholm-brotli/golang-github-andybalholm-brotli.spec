%global source0_hash a585d6fc199d5a09d7654e970b4f09caa1a2e4902d89101c8d955b8ef0d5855f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/andybalholm/brotli
Version:                1.2.0
%gometa -L -f
%global common_description %{expand:
This package is a brotli compressor and decompressor implemented in Go. It was
translated from the reference implementation (https://github.com/google/brotli)
with the c2go tool at https://github.com/andybalholm/c2go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-andybalholm-brotli
Release:        1%{?dist}
Summary:        Pure Go Brotli encoder and decoder
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/brotli-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
