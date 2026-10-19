%global source4_hash 4ade24e26c2e07a8708af699c24a8fb327c27bca7b64039f7b4825db711f6d8c
%global source3_hash a7bd20827c3c8da4a242c289b1610109d1b366ec2f52c46fc7301e9f5a75c2a8
%global source2_hash 956e6ad6a0eb9f7fb766e648a344c833b37e22691c9f7a4595be779ad8fef8c8
%global source1_hash cbba704e224837ff83dd37a75b9e8a2c509aaf4881d1df3dc43403549482b41f
%global source0_hash 2a32f645c1b111cfdb6b6e0b74b3127ee5706709b5950546881443ebe009a2cb
%global snapshot 20230911
%global debug_package %{nil}
Name:       libecb
Version:    0.%{snapshot}
Release:        7%{?dist}
Summary:        Compiler built-ins
License:    BSD-2-Clause OR GPL-2.0-or-later
URL:        http://software.schmorp.de/pkg/libecb.html
Source0:        http://cvs.schmorp.de/libecb/ecb.h?revision=1.216&view=co#/ecb.h
Source1:    http://cvs.schmorp.de/libecb/ecb.pod?revision=1.107&view=co#/ecb.pod
Source2:    http://cvs.schmorp.de/libecb/LICENSE?revision=1.2&view=co#/LICENSE
Source3:    http://cvs.schmorp.de/libecb/README?revision=1.3&view=co#/README
Source4:    http://cvs.schmorp.de/libecb/Changes?revision=1.47&view=co#/Changes
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl-podlators
# /oreon:deps
%description
This project delivers you many GCC built-ins, attributes and a number of
generally useful low-level functions, such as popcount, expect, prefetch,
noinline, assume, unreachable and so on.

This is a dummy package. All the useful files are delivered by %{name}-devel
package.

%package devel
Summary:    Compiler built-ins
Provides:   libecb-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:   libecb = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:  libecb < 0.20150218
%description devel
This project delivers you many GCC built-ins, attributes and a number of
generally useful low-level functions, such as popcount, expect, prefetch,
noinline, assume, unreachable and so on.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -T -c -n libecb-%{snapshot}
cp -a %{SOURCE0} ecb.h
cp -a %{SOURCE1} ecb.pod
cp -a %{SOURCE2} LICENSE
cp -a %{SOURCE3} README
cp -a %{SOURCE4} Changes

%build

pod2man ecb.pod > ecb.3
%install
install -d %{buildroot}%{_includedir}
install -m 0644 -t %{buildroot}%{_includedir} *.h
install -d %{buildroot}%{_mandir}/man3
install -m 0644 -t %{buildroot}%{_mandir}/man3 *.3
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libecb-devel -f %{oreon_filedir}/libecb-devel.list

%changelog

%autochangelog
