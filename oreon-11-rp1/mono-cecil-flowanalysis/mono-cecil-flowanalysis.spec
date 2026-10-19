%global source0_hash 4265dad76191b9e041a6d169f2623d3b3208bfbd03549d685d94f4514d955de1
%global debug_package %{nil}
Name:	 	mono-cecil-flowanalysis
Version:	0.1
Release:        1%{?dist}
Summary:        Flowanalysis engine for Cecil
URL:		https://github.com/mono/cecil/tree/master/flowanalysis
License:	MIT
Source0:        flowanalysis-20110512gitb34edf6.tar.bz2
Source1:	cecil-flowanalysis.pc
Patch0:		flowanalysis-build.patch
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%description
Flowanalysis engine for Cecil.

%package devel
Summary:	Flowanalysis engine for Cecil
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description devel
Development files for mono-cecil-flowanalysis

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n flowanalysis-20110512gitb34edf6
%patch -P0 -p1

%build

cp -a /etc/pki/mono/mono.snk Cecil.FlowAnalysis.snk
make LIBDIR=%{_prefix}/lib
%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp -p %{S:1} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!${prefix}/lib!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/cecil-flowanalysis.pc
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/mono/gac/
gacutil -i bin/Cecil.FlowAnalysis.dll -f -package Cecil.FlowAnalysis -root ${RPM_BUILD_ROOT}/%{_prefix}/lib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-cecil-flowanalysis-devel -f %{oreon_filedir}/mono-cecil-flowanalysis-devel.list

%changelog

%autochangelog
