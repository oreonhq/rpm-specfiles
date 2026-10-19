%global source0_hash 00ce141869e009f102f51fb8f9c2a611decb67083e4c1de7842bc9eafad8676b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golang/freetype
%global commit          e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-BurntSushi-freetype-go-devel < 0-0.8
}
%global goaltipaths     github.com/BurntSushi/freetype-go
%global common_description %{expand:
The Freetype font rasterizer in the Go programming language.}
%global golicenses      LICENSE licenses/gpl.txt licenses/ftl.txt
%global godocs          example AUTHORS CONTRIBUTORS README
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Freetype font rasterizer in the Go programming language
License:        GPL-2.0-only OR FTL
Source0:        https://%{goipath}/archive/%{commit}/freetype-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/math/fixed)
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
