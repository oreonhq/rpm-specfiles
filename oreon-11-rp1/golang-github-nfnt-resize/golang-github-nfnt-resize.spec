%global source0_hash 8e10018e7e272917a57525dc42d443075a5c040c9f2ee73907562a8d84a45f4b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/nfnt/resize
%global commit          83c6a9932646f83e3267f353373d47347b6036b2
%gometa
%global common_description %{expand:
Image resizing for the Go programming language with common interpolation
methods.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Pure golang image resizing
License:        ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/resize-%{commit}.tar.gz
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
