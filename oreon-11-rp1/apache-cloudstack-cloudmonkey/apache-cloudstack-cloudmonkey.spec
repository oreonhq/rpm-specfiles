%global source0_hash 06c2cd7ad49baac57beea244a90f0030b43c853d15a8aa25ce49ec40651dc303
%bcond check 0
%global goipath         github.com/apache/cloudstack-cloudmonkey
Version:                6.6.0
%global tag             6.2.0
%gometa
%global common_description %{expand:
Apache Cloudstack Cloudmonkey is a command line interface (CLI) for Apache
CloudStack.
CloudMonkey can be use both as an interactive shell and as a command line tool
which simplifies Apache CloudStack configuration and management.}
%global golicenses      LICENSE
%global godocs          README.md CHANGES.md
Name:           apache-cloudstack-cloudmonkey
Release:        1%{?dist}
Summary:        Apache Cloudstack Cloudmonkey
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/cloudstack-cloudmonkey-%{tag}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       golang-github-apache-cloudstack-cloudmonkey-devel
Summary:        Apache Cloudstack Cloudmonkey
BuildArch:      noarch

%description -n golang-github-apache-cloudstack-cloudmonkey-devel
Apache Cloudstack Cloudmonkey

%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/cmk %{goipath}
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
