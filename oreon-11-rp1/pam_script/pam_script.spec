%global source0_hash 0aab103d318e3048ccc6f8285950f99284c814f996d2dcbcae8f10d3b8bd8cfe
%global upstream_name pam-script
Name:           pam_script
Version:        1.1.9
Release:        20%{?dist}
Summary:        PAM module for executing scripts
License:        GPL-2.0-or-later
URL:            https://github.com/jeroennijhof/pam_script
Source0:        https://github.com/jeroennijhof/pam_script/archive/%{version}/pam_script-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
# /oreon:deps
%description
pam_script allows you to execute scripts during authorization, password
changes and session openings or closings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#generate our configure script
autoreconf -vfi

%build

%configure --libdir=/%{_lib}/security
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_sysconfdir}/README
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
