%global source0_hash ce834a1e491ef8f028b5711fde615218e8d00dafdeca86e1b1bf32e0f8245376
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pbnjay/memory
%global commit          7b4eea64cf580186c0eceb10dc94ba3a098af46c
%gometa -f
%global common_description %{expand:
A Go function to report total system memory.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go function to report total system memory
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/memory-%{commit}.tar.gz
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
