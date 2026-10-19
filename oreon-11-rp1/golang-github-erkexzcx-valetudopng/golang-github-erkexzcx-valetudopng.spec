%global source0_hash eb598f28448839ca39f50fd2e5e3327ed612737cddf608cd8eb4dd41b23a16c3
%bcond check 0
%global goipath         github.com/erkexzcx/valetudopng
Version:                1.0.15
%gometa -f
%global common_description %{expand:
A Valetudo map renderer (ex Hypfer/ICantBelieveItsNotValetudo) for Home
Assistant.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Valetudo map renderer for Home Assistant
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/valetudopng-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  js-jquery
# /oreon:deps
%description %{common_description}

%package -n     valetudopng
Summary:        Valetudo map renderer for Home Assistant
%description -n valetudopng %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

# Replace bundled jquery with the system one
ln -sf %{_datadir}/web-assets/jquery/3/jquery.min.js web/static/js/JQuery.js

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles valetudopng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n valetudopng -f %{oreon_filedir}/valetudopng.list

%changelog

%autochangelog
