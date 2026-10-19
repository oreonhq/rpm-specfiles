%global source0_hash dda8be9c9c594e164e664479001e7113d0f6571b3fc93253ef132096540f0673
%bcond check 0
%global goipath         github.com/GeertJohan/go.rice
Version:                1.0.3
%gometa
%global common_description %{expand:
Go.rice is a Go package that makes working with resources such as
html,js,css,images,templates, etc very easy.}
%global golicenses      LICENSE
%global godocs          example AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package that makes working with resources such as html, js, css very easy
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go.rice-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in rice; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
