%global source0_hash 0e2f2e452431ac4375cda737c9d21009b77e5bb5ef0c6c441273d2b0700c140c
%global date 20240730
%global commit b123373e8aed9966c29c0a5981d3a62bd9996e50
%global shortcommit %global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           aer-inject
Version:        0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Linux AER Test Suite
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://github.com/intel/aer-inject
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
aer-inject allows to inject PCIE AER errors on the software level into a
running Linux kernel. This is intended for validation of the PCIE driver error
recovery handler and PCIE AER core handler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

# Preseve timestamps on install and set permissions
sed -i 's/install aer-inject/install -pm0755 aer-inject/' Makefile

%build

%make_build CFLAGS="%{build_cflags}"
%install
%make_install PREFIX="%{_bindir}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
