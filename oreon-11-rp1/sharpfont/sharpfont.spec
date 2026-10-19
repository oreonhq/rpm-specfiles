%global source0_hash dab06061050020a1706cd50b00108c211dbed0bfbc88337129d83c29a2a8dc2a
%global libname SharpFont
%global debug_package %{nil}
Name:           sharpfont
Version:        4.0.1
Release:        21%{?dist}
Url:            https://github.com/Robmaister/%{libname}
Summary:        Cross-platform FreeType bindings for .NET
License:        MIT
Source0:        https://github.com/Robmaister/%{libname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %mono_arches
# oreon:deps
BuildRequires:  pkgconfig(mono)
# /oreon:deps
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

pushd Source/%{libname}
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sharpfont-devel -f %{oreon_filedir}/sharpfont-devel.list

%changelog

%autochangelog
