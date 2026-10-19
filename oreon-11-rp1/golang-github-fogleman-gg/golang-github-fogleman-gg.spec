%global source0_hash 7f0607390a4450e2ee505648f065c69df8f85b5d11997ba05b4e99b9dca79528
%ifnarch aarch64 ppc64le s390x
%bcond check 0
%endif
%global goipath         github.com/fogleman/gg
Version:                1.3.0
%global commit          ad4d1eafac46916fde6a6b375f7389e555f7e040
%gometa
%global common_description %{expand:
Gg is a library for rendering 2D graphics in pure Go.}
%global golicenses      LICENSE.md
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        2D rendering in Go with a simple API
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gg-%{commit}.tar.gz
Patch0:         0001-fix-test-for-1.13.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/freetype/raster)
BuildRequires:  golang(github.com/golang/freetype/truetype)
BuildRequires:  golang(golang.org/x/image/draw)
BuildRequires:  golang(golang.org/x/image/font)
BuildRequires:  golang(golang.org/x/image/font/basicfont)
BuildRequires:  golang(golang.org/x/image/font/gofont/goregular)
BuildRequires:  golang(golang.org/x/image/math/f64)
BuildRequires:  golang(golang.org/x/image/math/fixed)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
