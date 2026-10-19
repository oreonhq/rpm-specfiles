%global source0_hash 7ffb701de438168a11e50abe7167e2fe942365883bf5b837560e2de2071821dd
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/martinhoefling/goxkcdpwgen
Version:                0.1.1
%global commit          e51aa57005ca8a60bfc62cab891338c0282effdb
%gometa -L -f
%global common_description %{expand:
Xkcd style password generator library and cli tool.}
%global golicenses      LICENSE
%global godocs          CHANGES.md README.md
Name:           golang-github-martinhoefling-goxkcdpwgen
Release:        1%{?dist}
Summary:        Xkcd style password generator library and cli tool
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goxkcdpwgen-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%build

%gobuild -o %{gobuilddir}/bin/goxkcdpwgen %{goipath}
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
