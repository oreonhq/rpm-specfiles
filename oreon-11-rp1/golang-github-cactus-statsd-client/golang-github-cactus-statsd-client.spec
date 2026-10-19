%global source0_hash d720436cf6e6f6190220ad31beb74b5b9f3afe5a5854bba8cb63442b286d3f45
%bcond check 0
%global goipath         github.com/cactus/go-statsd-client
Version:                6.0.0
%gometa
%global goaltipaths     github.com/cactus/go-statsd-client/v5
%global common_description %{expand:
A StatsD client for Go.}
%global golicenses      LICENSE.md
%global godocs          README.md CHANGELOG.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Statsd client for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-statsd-client-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jessevdk/go-flags)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in test-client; do
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
