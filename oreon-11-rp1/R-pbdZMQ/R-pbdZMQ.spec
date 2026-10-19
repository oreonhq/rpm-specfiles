%global source0_hash 60154f66db9378655d7c39c8c2e02e74ac6bd801a9aac1bc73003c7eeeb23223
Name:           R-pbdZMQ
Version:        %R_rpm_version 0.3-14
Release:        1%{?dist}
Summary:        Programming with Big Data -- Interface to ZeroMQ
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pbdZMQ&version=0.3-14#/pbdZMQ_0.3-14.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  zeromq-devel
# /oreon:deps
%description
'ZeroMQ' is a well-known library for high-performance asynchronous
messaging in scalable, distributed applications.  This package provides
high level R wrapper functions to easily utilize 'ZeroMQ'. We mainly focus
on interactive client/server programming frameworks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -rf pbdZMQ/inst/zmq_copyright

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
