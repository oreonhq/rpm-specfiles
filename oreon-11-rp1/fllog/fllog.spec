%global source0_hash dde26f4fd3e31d3acc9f4fe902b50320813b4fbcb56276b21b93ee1a8930b519
Name:           fllog
Version:        1.2.9
Release:        1%{?dist}
Summary:        Amateur Radio Log Program
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            http://w1hkj.com/fllog-help/index.html
Source0:        http://downloads.sourceforge.net/fldigi/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  make
# /oreon:deps
%description
Fllog is a transceiver control program for Amateur Radio use.  It does
not use any 3rd party transceiver control libraries.  It is a c++ pro-
gram that encapsulates each transceiver in its own class.  Where ever
possible the transceiver class(s) use polymorphism to reuse code that
is portable across a series of transceivers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

rm -rf src/xmlrpcpp
rm -f src/include/XmlRpc*.h

%build

%{?rhel:export LDFLAGS="%{optflags}"}
%configure
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
