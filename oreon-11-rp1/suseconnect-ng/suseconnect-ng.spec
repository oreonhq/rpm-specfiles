%global source0_hash 1d4955e39969382551465a80f72350b06c0fd77253e05112cd49b3c4fbd435f1
%bcond check 0
%global libsofedbasever 0.n
%global libsomajor 1
%global libsoversion %{libsofedbasever}.%{libsomajor}
%global goipath         github.com/SUSE/connect-ng
Version:                1.4.0
%gometa -f
%global common_description %{expand:
SUSEConnect is a command line tool for connecting a client system
to the SUSE Customer Center. It will connect the system to your
product subscriptions and enable the product repositories/services
locally.}
%global golicenses      LICENSE LICENSE.LGPL
%global godocs          DIFFERENCES.md README.md\\\
                        man/SUSEConnect.5.md man/SUSEConnect.8.md\\\
                        suseconnect/migrationUsage.txt\\\
                        suseconnect/searchPackagesUsage.txt\\\
                        suseconnect/connectUsage.txt
Name:           suseconnect-ng
Release:        1%{?dist}
Summary:        Utility to register a system with the SUSE Customer Center
License:        LGPL-2.1-or-later
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/connect-ng-%{version}.tar.gz
Patch:          suseconnect-ng-PR189.patch
Provides:       SUSEConnect = %{version}-%{release}
Provides:       SUSEConnect-ng = %{version}-%{release}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%package -n libsuseconnect
Summary:        Library to interface with the SUSE Customer Center
%description -n libsuseconnect %{common_description}
This package provides the library for applications to
interface with the SUSE Customer Center.

%package -n libsuseconnect-devel
Summary:        Development files to use libsuseconnect
Requires:       libsuseconnect%{?_isa} = %{version}-%{release}
%description -n libsuseconnect-devel %{common_description}
This package provides the development files for applications
to use the library to interface with the SUSE Customer Center.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
echo "%{version}-%{release}" > internal/connect/version.txt

%build

for cmd in libsuseconnect; do
  %define gocompilerflags -buildmode=c-shared -compiler gc
  %define __golang_extldflags -Wl,-soname,$(basename $cmd).so.%{libsoversion}
  %gobuild -o %{gobuilddir}/lib/$(basename $cmd).so.%{libsoversion} %{goipath}/$cmd
  ln -sr %{gobuilddir}/lib/$(basename $cmd).so.%{libsoversion} %{gobuilddir}/lib/$(basename $cmd).so
  mv %{gobuilddir}/lib/$(basename $cmd).so.%{libsofedbasever}.h %{gobuilddir}/lib/$(basename $cmd).h
done
for cmd in suseconnect; do
  %define gocompilerflags -buildmode=pie -compiler gc
  %define __golang_extldflags %{nil}
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
ln -sr %{gobuilddir}/bin/suseconnect %{gobuilddir}/bin/SUSEConnect
%install
%gopkginstall
install -m 0755 -vd                       %{buildroot}%{_bindir}
cp -av %{gobuilddir}/bin/*                %{buildroot}%{_bindir}/
install -m 0755 -vd                       %{buildroot}%{_libdir}
cp -av %{gobuilddir}/lib/*.so*            %{buildroot}%{_libdir}/
install -m 0755 -vd                       %{buildroot}%{_includedir}
install -m 0644 -vp %{gobuilddir}/lib/*.h %{buildroot}%{_includedir}/
install -m 0755 -vd                       %{buildroot}%{_unitdir}
install -m 0644 -vp *.service *.timer     %{buildroot}%{_unitdir}/
%oreon_autofiles libsuseconnect usr/*/lib*.so.*
%oreon_autofiles libsuseconnect-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%gocheck
%endif
%post

%systemd_post suseconnect-keepalive.timer
%preun

%systemd_preun suseconnect-keepalive.timer
%postun

%systemd_postun_with_restart suseconnect-keepalive.timer
%files -f %{oreon_filedir}/main.list
%files -n libsuseconnect -f %{oreon_filedir}/libsuseconnect.list
%files -n libsuseconnect-devel -f %{oreon_filedir}/libsuseconnect-devel.list

%changelog

%autochangelog
