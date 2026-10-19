%global source0_hash 670d14b003fb883efbd68f3e813b1022ce2325a6b4b6d2e9e6445f38db51f902
%bcond check 0
%global goipath         github.com/rakyll/statik
Version:                0.1.8
%gometa
%global common_description %{expand:
Statik allows you to embed a directory of static files into your Go binary to be
later served from an http.FileSystem.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Embed files into a Go executable
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/statik-%{version}.tar.gz
Patch0:         0001-Use-Modified.UTC-instead-of-ModTime.patch
Patch1:         0001-Fix-Println-arg-list-ends-with-redundant-newline.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
%patch -P1 -p1

%build

%gobuild -o %{gobuilddir}/bin/statik %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d fs
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
