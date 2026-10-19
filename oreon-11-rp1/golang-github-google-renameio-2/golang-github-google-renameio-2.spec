%global source0_hash b46ccf417206ab61191249aa483cda58cae61ff919834cc25cbab35ab2f12b28
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/renameio/v2
Version:                2.0.2
%gometa -f
%global common_description %{expand:
Provides a way to atomically create or replace a file or
symbolic link}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package renameio provides a way to atomically create or replace a file or symbolic link
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/google/renameio/archive/v%{version}/renameio-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
