%global source0_hash 1b863d045a565d41a02296f5a0112c1b9bbd25300478f7a7fa9ad7d5436b3f2b
%ifnarch s390x aarch64 ppc64le
%bcond check 0
%endif
%global goipath         github.com/rcrowley/go-metrics
%global commit          cf1acfcdf4751e0554ffa765d03e479ec491cad6
%gometa
%global common_description %{expand:
Go port of coda hale's metrics library.}
%global golicenses      LICENSE
%global godocs          README.md memory.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go port of coda hale's metrics library
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-metrics-%{commit}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stathat/go)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
