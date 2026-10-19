%global source0_hash 20bee5341bfa266dd17f7441adf49a9a5a46efc9ef2ce94897e503a4b407cac3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/philhofer/fwd
Version:                1.2.0
%gometa
%global common_description %{expand:
The fwd package provides a buffered reader and writer. Each has methods that
help improve the encoding/decoding performance of some binary protocols.
The fwd.Writer and fwd.Reader type provide similar functionality to their
counterparts in bufio, plus a few extra utility methods that simplify
read-ahead and write-ahead.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Buffered Reader/Writer
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fwd-%{version}.tar.gz
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
