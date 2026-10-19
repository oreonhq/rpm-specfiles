%global source0_hash 652a7c5352d55e8063dea091eee54f651fbca8ffd796b2376d4b8ea4aeba83be
%bcond check 0
%global debug_package %{nil}
%global goipath         rsc.io/qr
%global forgeurl        https://github.com/rsc/qr
Version:                0.2.0
%global commit          b6857d426aa506d5bf7efb8f73928d72bcf4e73d
%gometa
%global common_description %{expand:
Golang generator of QR codes.}
%global godocs        README.md
%global golicenses    LICENSE
%global godevelheader %{expand:
Requires:       pkgconfig(libqrencode)
}
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang generator of QR codes
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/qr-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libqrencode)
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

rm -rfv coding/qr_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
