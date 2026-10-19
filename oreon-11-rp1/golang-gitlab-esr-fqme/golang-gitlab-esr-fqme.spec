%global source0_hash 366f5fbca3ca6786f1aaddf1f720d286cfca203f8170d5a9916b0e96024d4fc1
%bcond check 0
%global debug_package %{nil}
%global goipath         gitlab.com/esr/fqme
%global forgeurl        https://gitlab.com/esr/fqme
Version:                1.0.0
%global tag             v%{version}
%gometa
%global common_description %{expand:
Fqme is Fully Qualified Me, a Go module that mines configuration files to
discover your full name and email address.}
%global golicenses      LICENSE
%global godocs          README.adoc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go module that mines configuration files to discover full name and email address
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/fqme-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm -rf demo

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
