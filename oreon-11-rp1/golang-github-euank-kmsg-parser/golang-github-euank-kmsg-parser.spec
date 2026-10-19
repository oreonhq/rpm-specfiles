%global source0_hash 386b5ad9486d5bf66e6da62c100021b887c39dfea3535d5f26ddfbd7e46f8bfd
%bcond check 0
%global goipath         github.com/euank/go-kmsg-parser
Version:                3.0.0
%gometa
%global common_description %{expand:
This package contains a library to allow parsing the /dev/kmsg device in Linux.
This device provides a read-write interface to the Linux Kernel's ring buffer.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simpler parser for the /dev/kmsg format
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-kmsg-parser-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
# /oreon:deps
%description
%{common_description}

%package -n    godmesg
Summary:        Simpler parser for the /dev/kmsg format
%description -n godmesg
A simple cli-tool that functions similarly to dmesg --ctime --follow. This code
serves both as a usage example and as a simple way to verify it works how you'd
expect on a given system.

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
%oreon_autofiles godmesg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n godmesg -f %{oreon_filedir}/godmesg.list

%changelog

%autochangelog
