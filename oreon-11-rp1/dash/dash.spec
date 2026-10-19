%global source0_hash 40090101a2a491f13e901d3d48e90414f26634628b9bfff35ff540363c227a7d
Name:           dash
Version:        0.5.13.5
Release:        1%{?dist}
Summary:        Small and fast POSIX-compliant shell
License:        BSD-3-Clause AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://gondor.apana.org.au/~herbert/%{name}/
Source0:        http://gondor.apana.org.au/~herbert/%{name}/files/%{name}-%{version}.tar.gz
Provides:       /bin/dash
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible. It does this without sacrificing speed where possible. In fact, it is
significantly faster than bash (the GNU Bourne-Again SHell) for most tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --bindir=%{_bindir}
%make_build
%install
%make_install
%oreon_autofiles main

%post

grep -q '^/bin/dash$' %{_sysconfdir}/shells || \
    echo '/bin/dash' >> %{_sysconfdir}/shells
%postun

if [ $1 -eq 0 ]; then
    sed -i '/^\/bin\/dash$/d' %{_sysconfdir}/shells
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
