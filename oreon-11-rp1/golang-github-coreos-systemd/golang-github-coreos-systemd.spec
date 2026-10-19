%global source0_hash ff64fccd64a70123d513f979ea7a97f42300d7af33303890c1ab491f57a311ea
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/coreos/go-systemd
Version:                22.7.0
%gometa
%global goaltipaths     github.com/coreos/go-systemd/v22
%global common_description %{expand:
Go bindings to systemd. The project has several packages:
 - activation - for writing and using socket activation from Go
 - daemon - for notifying systemd of service status changes
 - dbus - for starting/stopping/inspecting running services and units
 - journal - for writing to systemd's logging service, journald
 - sdjournal - for reading from journald by wrapping its C API
 - login1 - for integration with the systemd logind API
 - machine1 - for registering machines/containers with systemd
 - unit - for (de)serialization and comparison of unit files
}
%global golicenses      LICENSE NOTICE
%global godocs          examples CONTRIBUTING.md README.md code-of-conduct.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go bindings to systemd socket activation, journal, D-Bus, and unit files
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-systemd-%{version}.tar.gz
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

%gocheck -d dbus \
         -d import1 \
         -d internal/dlopen \
         -d journal \
         -d login1 \
         -d machine1 \
         -d sdjournal \
         -d util
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
