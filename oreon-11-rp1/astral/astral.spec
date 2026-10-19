%global source0_hash 81a324917c2504803964bc38b64a64f19b7be15d54d047606eabf55f00d4bede
%bcond check 0
%global goipath         github.com/sj14/astral
Version:                0.2.3
%gometa
%global common_description %{expand:
Go calculations for the position of the sun and moon.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           astral
Release:        1%{?dist}
Summary:        Go calculations for the position of the sun and moon
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       golang-github-apache-cloudstack-cloudmonkey-devel
Summary:        Go calculations for the position of the sun and moon
BuildArch:      noarch

%description -n golang-github-apache-cloudstack-cloudmonkey-devel
Go calculations for the position of the sun and moon

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
