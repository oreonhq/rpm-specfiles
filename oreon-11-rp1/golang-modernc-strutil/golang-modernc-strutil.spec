%global source0_hash f4b5734413855f4d053f6753492118c70b506218f99feb8047796a85e5ff6f5c
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/strutil
%global forgeurl        https://gitlab.com/cznic/strutil
Version:                1.2.1
%global tag             v%{version}
%gometa
%global common_description %{expand:
Package strutil collects utils supplemental to the standard strings package.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Utils supplemental to the standard strings package
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/strutil-%{tag}.tar.bz2
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
