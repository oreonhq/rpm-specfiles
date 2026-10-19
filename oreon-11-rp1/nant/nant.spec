%global source0_hash 72d4d585267ed7f03e1aa75087d96f4f8d49ee976c32d974c5ab1fef4d4f8305
%global debug_package %{nil}
%global monodir %{_prefix}/lib
%global bootstrap 0
Summary:        NAnt is a build tool for Mono and .NET
Name: nant
Version: 0.92
Release:        1%{?dist}
Epoch: 1
License: GPL-2.0-or-later
Url: http://nant.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nant/%{name}-%{version}-src.tar.gz
Patch1: nant-0.92-no_ndoc.patch
Patch2: nant-0.92-system_nunit.patch
Patch3: nant-0.90-no_sharpcvslib.patch
Patch4: nant-0.90-system_sharpziplib.patch
Patch5: nant-0.92-system_log4net.patch
Patch6: nant-0.92-no_netdumbster.patch
Patch7: nant-fixmono42_scripttask.patch
Patch8: nant-0.92-mono-4.5.patch
Patch9: nant-0.92-mono-4.5-config.patch
%if 0%{bootstrap}
%else
%endif
Requires:      nunit2
ExclusiveArch: %mono_arches
ExcludeArch:    armv7hl
%if 0%{bootstrap}
%filter_requires_in %{_prefix}/lib/NAnt/
%filter_provides_in %{_prefix}/lib/NAnt/
%filter_setup
%endif
# oreon:deps
BuildRequires:  log4net-devel
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  nunit2-devel
# /oreon:deps
%description
NAnt is a free .NET build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.

%package docs
Summary:	Documentation package for nant
Requires:	%{name} = %{epoch}:%{version}-%{release}
%description docs
Documentation for nant

%package devel
Summary:	Development file for nant
Requires:	%{name} = %{epoch}:%{version}-%{release}
%description devel
Development file for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# install to libdir instead of datadir
sed -i -e "/property name=\"install\.share\"/ s/'share'/'lib'/" NAnt.build
sed -i -e "s,/share/,/lib/," etc/nant.pc.in

# Remove NDoc support
%patch -P1 -p1 -b .no_ndoc
rm src/NAnt.DotNet/Tasks/NDocTask.cs
rm -Rf src/NDoc.Documenter.NAnt
find lib -name 'NDoc*.dll' | xargs rm

# Remove NUnit1 support and fix build with system NUnit.
# Based on Debian's 004-nant-nunit_2.4.dpatch
%patch -P2 -p1 -b .system_nunit
find lib -iname 'nunit*' | xargs rm

# Remove SharpCvsLib support
%patch -P3 -p1 -b .no_sharpcvslib
find lib -name "*SharpCvsLib*.dll" | xargs rm
find lib -name "scvs.exe" | xargs rm

# Use system SharpZipLib which is older than the one bundled with nant
# https://bugzilla.novell.com/show_bug.cgi?id=426065
%patch -P4 -p1 -F 3 -b .system_sharpziplib
find lib -name "*SharpZipLib*.dll" | xargs rm

%patch -P6 -p1 -b .no_netdumbster
rm tests/NAnt.Core/Tasks/MailTaskTest.cs

find . -type d|xargs chmod 755
find . -type f|xargs chmod 644
sed -i 's/\r//' doc/license.html
sed -i 's/\r//' COPYING.txt
sed -i 's/\r//' README.txt
sed -i 's/\r//' doc/releasenotes.html

# Clean out the prebuilt files (unless we're bootstrapping)
# If we're not bootstrapping, leave the files alone:
%if 0%{bootstrap}
echo "BOOTSTRAP BUILD"
%else
echo "NORMAL BUILD, NUKING PREBUILT BUNDLED DLL FILES"
rm -rf lib/*
%endif

# Use system log4net, unless we're bootstrapping.
%if 0%{bootstrap}
# do nothing
%else
%patch -P5 -p1 -b .system_log4net
%endif

%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1

#Fixes for Mono 4
sed -i "s#gmcs#mcs#g" Makefile
sed -i "s#TARGET=mono-2.0#TARGET=mono-4.5#g" Makefile
sed -i "s#dmcs#mcs#g" src/NAnt.Console/App.config
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build

make
%install
make install prefix=%{_prefix} DESTDIR=%{buildroot}
find examples -name \*.dll -o -name \*.exe|xargs rm -f
rm -rf %{buildroot}%{_datadir}/NAnt/doc
rm -rf %{buildroot}%{_prefix}/lib/doc/NAnt
%if 0%{bootstrap}
%else
rm -rf %{buildroot}%{_prefix}/lib/NAnt/bin/lib
rm -rf %{buildroot}%{_prefix}/lib/NAnt/bin/log4net.dll
%endif
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nant-docs -f %{oreon_filedir}/nant-docs.list
%files -n nant-devel -f %{oreon_filedir}/nant-devel.list

%changelog

%autochangelog
