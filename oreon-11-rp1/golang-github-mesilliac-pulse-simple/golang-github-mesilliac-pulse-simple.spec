%global source0_hash 3e44d7c5a5b26eb94bcb5b63d9c36c74704a0045d6eaa19187ce7c2650fef780
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mesilliac/pulse-simple
%global commit          75ac54e19fdff88f4fbd82f45125134b602230b0
%gometa -L -f
%global common_description %{expand:
Cgo bindings to PulseAudio's Simple API, for easily playing or capturing raw
audio.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           golang-github-mesilliac-pulse-simple
Version:        0
Release:        1%{?dist}
Summary:        Easily play or capture raw audio via PulseAudio's Simple API
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pulse-simple-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
