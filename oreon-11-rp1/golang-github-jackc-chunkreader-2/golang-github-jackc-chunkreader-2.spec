%global source0_hash bf856bad6608fb7345707aba713a1d77eb984f1d217065738a12c97e37669be4
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/chunkreader/v2
Version:                2.0.1
%gometa
%global common_description %{expand:
Package Chunkreader provides an io.Reader wrapper that minimizes IO reads and
memory allocations.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        io.Reader wrapper that minimizes IO reads and memory allocations
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/jackc/chunkreader/archive/v%{version}/chunkreader-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
