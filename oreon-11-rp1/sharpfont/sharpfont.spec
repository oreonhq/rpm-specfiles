%global source0_hash dab06061050020a1706cd50b00108c211dbed0bfbc88337129d83c29a2a8dc2a

#
# spec file for package sharpfont
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global libname SharpFont
%global debug_package %{nil}

Name:           sharpfont
Version:        4.0.1
Release:        21%{?dist}
Url:            https://github.com/Robmaister/%{libname}
Summary:        Cross-platform FreeType bindings for .NET
License:        MIT
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  %mono_arches

BuildRequires:  pkgconfig(mono)

%description
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.

%package devel
Summary:        Cross-platform FreeType bindings for .NET
Requires:       %{name} = %{version}-%{release}

%description devel
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n%{libname}-%{version}
rm -r Build Dependencies

%build
#make debug
pushd Source/%{libname}
# override the .NET Framework Target for predefined types
# https://stackoverflow.com/questions/27594393/compiled-mono-missing-default-net-libraries-system-object-is-not-defined-or-i
xbuild /p:TargetFrameworkVersion=v4.5 /p:Configuration=Debug

%install
mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i Binaries/%{libname}/Debug/%{libname}.dll -f -package %{name} -root %{buildroot}%{_prefix}/lib
cp -p Source/%{libname}.dll.config %{buildroot}%{_monodir}/%{name}

mkdir -p %{buildroot}/%{_datadir}/pkgconfig
cat <<EOT >>%{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
Name: %{libname}
Description: %{summary}
Version: 4.0.1
Requires: mono
Libs: -r:%{_monodir}/%{name}/%{libname}.dll
Libraries=%{_monodir}/%{name}/%{libname}.dll
EOT

%files
%license LICENSE
%doc README.md
%doc Source/Examples/
%{_monogacdir}/%{libname}
%{_monodir}/%{name}/%{libname}.dll*
%dir %{_monodir}/%{name}
 

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
