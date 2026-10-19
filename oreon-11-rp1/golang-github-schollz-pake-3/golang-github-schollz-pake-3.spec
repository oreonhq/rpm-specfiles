%global source0_hash 088f131e8714d248f0895858bc33f41bc7eac3a1af3b5c41c6f46cf5e870520e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/schollz/pake/v3
Version:                3.0.3
%gometa
%global common_description %{expand:
PAKE library for generating a strong secret between parties over an insecure
channel.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        PAKE library for generating a strong secret between parties
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/schollz/pake/archive/v%{version}/pake-%{version}.tar.gz
Patch1:         %{url}/commit/e49974075fb2bbc8b9fbaef1d1ee4358e004a0cc.patch
Patch2:         %{url}/commit/f3884c59208188000a93fd2dfe414651c3558b42.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
