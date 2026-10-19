%global source0_hash 7b60429dd142c12b2e42e60fd49bb3aa1ec0c8452a1b6989bc2d47a001254ffd
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/linuxdeepin/go-gir
Version:                3.0.4
%gometa -L
%global common_description %{expand:
Project go-gir-generator implements GObject-introspection based bindings
generator for Go.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           deepin-gir-generator
Release:        1%{?dist}
Summary:        GObject-introspection based bindings generator for Go
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-gir-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
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

export CGO_CFLAGS="%{optflags} -std=gnu17"
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
