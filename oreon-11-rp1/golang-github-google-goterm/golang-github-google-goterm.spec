%global source0_hash 7becae0a9112f568df89c0c9b0016862b2575397f91ca6ef78511f441f4d2897
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/goterm
%global commit          555d40f16ae2fad8b4429d18d5cb777e75e5a9dc
%gometa
%global common_description %{expand:
Go Terminal library with PTY support and colors.}
%global golicenses      LICENSE
%global godocs          example AUTHORS README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go Terminal library with PTY support and colors
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goterm-%{commit}.tar.gz
ExcludeArch:    ppc64le s390x
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
