%global source0_hash 1579b5da2a7816918135bf174c514d0f02f9880b513951da0c407e4648f80f6e
%global commit d696f1609852254038f208c0d163abb39976a57e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           config-kernel
Version:        0.3
Release:        6%{?dist}
Summary:        An easy way to edit kernel configuration files and templates
License:        GPL-2.0-or-later
URL:            https://github.com/pjps/config-kernel
Source0:        https://github.com/pjps/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  bison-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
config-kernel tool helps to edit kernel configuration files and templates.
User can query, enable, disable or toggle CONFIG options via command line
switch or an $EDITOR program, without worrying about option dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

CFLAGS="${CFLAGS} -g -fPIE -pie" \
%make_build %{?_smp_mlags}
%check

./configk -h > /dev/null
./configk -v
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0755 configk %{buildroot}/%{_bindir}/
install -m 0644 configk.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
