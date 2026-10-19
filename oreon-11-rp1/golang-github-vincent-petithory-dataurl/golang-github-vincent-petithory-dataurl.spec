%global source0_hash 47a177c37c9dba5cb7d36c03b4eec8d38375216a024416171eb84e4a2f69b33a
%bcond check 0
%global goipath         github.com/vincent-petithory/dataurl
%global commit          d1553a71de50473073e188aa79cebf7f993f20fe
%gometa
%global common_description %{expand:
Data URL Schemes in Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Data URL Schemes in Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/dataurl-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%package -n dataurl
Summary: Data URL encoder/decoder
%description
%{common_description}

%description -n dataurl
dataurl is a command-line data-scheme URL encoder and decoder written in Golang.

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
%oreon_autofiles dataurl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n dataurl -f %{oreon_filedir}/dataurl.list

%changelog

%autochangelog
