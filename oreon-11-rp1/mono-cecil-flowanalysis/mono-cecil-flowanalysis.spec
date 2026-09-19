%global source0_hash 4265dad76191b9e041a6d169f2623d3b3208bfbd03549d685d94f4514d955de1

%global debug_package %{nil}

Name:	 	mono-cecil-flowanalysis
Version:	0.1
Release:	0.49.20110512svn100264%{?dist}
Summary:	Flowanalysis engine for Cecil
URL:		https://github.com/mono/cecil/tree/master/flowanalysis
License:	MIT
# No source tarball, source from here:
# git clone https://github.com/mono/cecil.git
# mv cecil/flowanalysis flowanalysis-20110512gitb34edf6
# tar cvfj flowanalysis-20110512gitb34edf6.tar.bz2 flowanalysis-20110512gitb34edf6/
Source0:	flowanalysis-20110512gitb34edf6.tar.bz2
Source1:	cecil-flowanalysis.pc
Patch0:		flowanalysis-build.patch
BuildRequires: make
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

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
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk Cecil.FlowAnalysis.snk
make LIBDIR=%{_prefix}/lib

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp -p %{S:1} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!${prefix}/lib!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/cecil-flowanalysis.pc
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/mono/gac/
gacutil -i bin/Cecil.FlowAnalysis.dll -f -package Cecil.FlowAnalysis -root ${RPM_BUILD_ROOT}/%{_prefix}/lib

%files
%doc decompiler-notes.txt AUTHORS README
%{_prefix}/lib/mono/gac/Cecil.FlowAnalysis/
%{_prefix}/lib/mono/Cecil.FlowAnalysis/

%files devel
%{_libdir}/pkgconfig/cecil-flowanalysis.pc

%changelog
%autochangelog
