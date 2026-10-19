%global source0_hash ab1af7b982617f349d6e38641979d3929ce99a89e9b962ac4fd6b159c138042c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/eapache/go-xerial-snappy
%global commit          776d5712da21bc4762676d614db1d8a64f4238b0
%gometa
%global common_description %{expand:
Xerial-compatible Snappy framing support for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Xerial-compatible Snappy framing support for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-xerial-snappy-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/snappy)
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
