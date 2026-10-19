%global source0_hash 91fe3822427db43b5bdaa158d39387fc01e4e03d999457da658f9b223b762020
%bcond check 0
%global goipath         github.com/guptarohit/asciigraph
Version:                0.10.0
%gometa
%global common_description %{expand:
Go package to make lightweight ASCII line graph ╭┈╯ in command line apps with
no other dependencies.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           asciigraph
Release:        1%{?dist}
Summary:        Makes lightweight ASCII line graphs
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       golang-github-apache-cloudstack-cloudmonkey-devel
Summary:        Makes lightweight ASCII line graphs
BuildArch:      noarch

%description -n golang-github-apache-cloudstack-cloudmonkey-devel
Makes lightweight ASCII line graphs

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
%oreon_autofiles golang-github-apache-cloudstack-cloudmonkey-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n golang-github-apache-cloudstack-cloudmonkey-devel -f %{oreon_filedir}/golang-github-apache-cloudstack-cloudmonkey-devel.list

%changelog

%autochangelog
