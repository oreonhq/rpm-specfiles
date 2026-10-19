%global source0_hash 02f57c2cc795a7ec9d74354d182fcff5cc69734c7a46f82b33b656f8bdb19703
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/microcosm-cc/bluemonday
Version:                1.0.27
%gometa -L
%global common_description %{expand:
Bluemonday is a fast golang HTML sanitizer (inspired by the OWASP Java HTML
Sanitizer) to scrub user generated content of XSS.}
%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md CREDITS.md README.md SECURITY.md
Name:           golang-github-microcosm-cc-bluemonday
Release:        1%{?dist}
Summary:        Fast golang HTML sanitizer
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/bluemonday-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
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
