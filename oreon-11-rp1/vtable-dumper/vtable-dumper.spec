%global source0_hash 6993781b6a00936fc5f76dc0db4c410acb46b6d6e9836ddbe2e3c525c6dd1fd2

Name:           vtable-dumper
Version:        1.2
Release:        23%{?dist}
Summary:        Tool to list content of virtual tables in a C++ shared library

# Automatically converted from old format: GPL+ or LGPLv2+ - review is highly recommended.
License:        GPL-1.0-or-later OR LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/lvc/vtable-dumper
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  elfutils-libelf-devel

%description
Vtable-Dumper is a tool to list content of virtual tables in a C++ shared
library. It is intended for developers of software libraries and maintainers of
Linux distributions who are interested in ensuring backward binary
compatibility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README
%{_bindir}/%{name}

%changelog
%autochangelog
