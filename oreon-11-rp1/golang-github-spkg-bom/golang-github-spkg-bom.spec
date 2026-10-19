%global source0_hash d6087db7348575f02b416c5920a3a10b0c3ab16be655016a925beaf6300dba06
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/spkg/bom
Version:                1.0.0
%gometa -f
%global common_description %{expand:
Strip UTF-8 byte order marks.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Strip UTF-8 byte order marks
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/bom-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
