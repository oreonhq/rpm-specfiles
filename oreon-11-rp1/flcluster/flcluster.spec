%global source0_hash 3df2d10b7886b72b857e972a319c6af4f476ba5e60ad200b4de46978395bc161
%bcond_without flxmlrpc
Name:           flcluster
Version:        1.0.7
Release:        1%{?dist}
Summary:        A management tool for accessing dxcluster nodes
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
Source99:       flcluster.appdata.xml
%if %{with flxmlrpc}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
flcluster can connect to and display data from DX cluster servers. The three
most common server types are A←-R-Cluster, CC-Cluster, and DX Spider. The
program is designed to work stand alone or as a helper application to fldigi.
It can move call, mode, and frequency data from a spotted QSO to the appropriate
fldigi controls. It can query fldigi for the same items when generating a spot
report.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%if %{with flxmlrpc}
# Remove bundled xmlrpc library.
rm -rf src/xmlrpcpp
%endif

%build

export LIBS="-lfltk"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
