%global source0_hash 9a95e9462308ebc2796eafa7733bc094168008e8575c9189e353249708d65983
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cention-sany/utf7
%global commit          26cad61bd60aa9fe1819b49717dda49ab82cc929
%gometa
%global common_description %{expand:
UTF7 UTF8 transcoder. With transformer interface.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        UTF7 UTF8 transcoder. With transformer interface
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/utf7-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/transform)
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
