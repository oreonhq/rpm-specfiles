%global source0_hash 1273853b404e6a5ab79ab6ec411cdc89638d9b42abae8acde9ed2e1295295a51
%bcond check 1
%global goipath         github.com/xo/terminfo
%global commit          abceb7e1c41eed2857facd9bbdaaa5ff8137d901
%gometa
%global common_description %{expand:
A terminfo package in pure go!}
%global golicenses      LICENSE
%global godocs          _examples README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        A terminfo package in pure go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/terminfo-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
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
