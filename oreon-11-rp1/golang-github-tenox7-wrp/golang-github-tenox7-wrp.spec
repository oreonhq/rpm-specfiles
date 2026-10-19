%global source0_hash 4692c0f51a6d168f1c1acd1b23f7fa1c1d03981758f62cf4052843bf66f540aa
%bcond check 0
%global goipath         github.com/tenox7/wrp
Version:                4.6.0
%global tag             4.6.0
%gometa -f
%global common_description %{expand:
Web Rendering Proxy (WRP) is a browser-in-browser "proxy" server that allows to
use historical / vintage web browsers on the modern web. It works by rendering
a web page in to a GIF or PNG image with clickable imagemap.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Web Rendering Proxy to use legacy browsers on the modern web
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/wrp-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       wrp
Summary:        Web Rendering Proxy to use legacy browsers on the modern web
BuildArch:      noarch

%description -n wrp
Web Rendering Proxy to use legacy browsers on the modern web

%description %{common_description}

%package -n     wrp
Summary:        Web Rendering Proxy to use legacy browsers on the modern web
%description -n wrp %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/wrp %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles wrp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n wrp -f %{oreon_filedir}/wrp.list

%changelog

%autochangelog
