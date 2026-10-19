%global source0_hash 197da900aa08f60cb7c541241746771e90a1c1eb8e8e962241e3532d7fc334e5
Name:           smc-tools
Version:        1.8.8
Release:        1%{?dist}
Summary:        Shared Memory Communication Tools
License:        EPL-1.0
URL:            https://github.com/ibm-s390-linux/smc-tools
Source0:        https://github.com/ibm-s390-linux/smc-tools/archive/refs/tags/1.8.8.tar.gz#/smc-tools-1.8.7.tar.gz
%ifarch s390 s390x
Requires:       python3
Requires:       man
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
The Shared Memory Communication Tools (smc-tools) package enables usage of SMC
sockets in Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch ppc64le
%global optflags %optflags -D__SANE_USERSPACE_TYPES__
%endif
%set_build_flags
%make_build
%install
%make_install V=1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
