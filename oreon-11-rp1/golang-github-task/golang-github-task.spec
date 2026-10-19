%global source0_hash 41784e166ef1a6bf429829195a727345296dd9fb94d59a274f2e158383167753
%bcond check 1
%global goipath         github.com/go-task/task
%global goialtpath      github.com/go-task/task/v3
Version:                3.48.0
%gometa -L -f
%global common_description %{expand:
A task runner / simpler Make alternative written in Go.}
Name:           golang-github-task
Release:        1%{?dist}
Summary:        A task runner / simpler Make alternative written in Go
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/task-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%package -n       go-task
Summary:        Provides the go-task task-runner binary
BuildArch:      noarch

%description -n go-task
Provides the go-task task-runner binary

%package -n       golang-github-task-doc
Summary:        Extended documentation for golang-github-task
BuildArch:      noarch

%description -n golang-github-task-doc
Extended documentation for golang-github-task

%description
%{common_description}

%package -n go-task
Summary: Provides the go-task task-runner binary
%description -n go-task
%{common_description}

%package doc
Summary: Extended documentation for %{name}
%description doc
%{common_description}
This package contains extended documentation for go-task.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
sed -i "s/unknown/v%{version}/" internal/version/version.go
sed -i "s/task-version\"\, expected\: \"unknown\"/task-version\"\, expected\: \"v%{version}\"/" task_test.go
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/task -v %{goialtpath}/cmd/task
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                        %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/task %{buildroot}%{_bindir}/go-task
%oreon_autofiles go-task usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list
%files -n go-task -f %{oreon_filedir}/go-task.list
%files -n golang-github-task-doc -f %{oreon_filedir}/golang-github-task-doc.list

%changelog

%autochangelog
