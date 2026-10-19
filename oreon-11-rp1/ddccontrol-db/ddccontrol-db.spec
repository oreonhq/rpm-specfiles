%global source0_hash 717fa4b45d6bbc4fd9c44d58c5c3992588f5c6224396483a0cc041a811d9055b
Name:             ddccontrol-db
URL:              https://github.com/ddccontrol/ddccontrol-db
Version:          20260928
Release:        1%{?dist}
License:          GPL-2.0-or-later
Summary:        DDC/CI control database for ddccontrol
Source0:        https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:        noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
DDC/CU control database for DDCcontrol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

./autogen.sh

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
