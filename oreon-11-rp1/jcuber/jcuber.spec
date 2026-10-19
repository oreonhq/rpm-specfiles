%global source0_hash b897b85fa3909fc03b2640d3895960e8071c5a97cc88834568bdf4ee6eb83e9d
Name:           jcuber
Version:        4.9
Release:        1%{?dist}
Summary:        CUBE reader for Java
License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/%{version}/dist/%{name}-%{version}.tar.gz
Requires:       java-25 jpackage-utils
Obsoletes:      cube-java <= 4.3.2-1
Provides:       cube-java = %version-%release
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  make
BuildRequires:  xerces-j2
# /oreon:deps
%description
A CUBE reader written in Java.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Conflicts:      cube-java <= 4.3.2-1
%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
sed -i -e s/jCubeR/jcuber/ -e 's|/cube|/jcuber|' bin/jcuber-config
make
%check

make check
%install
make install install-html DESTDIR=%buildroot
cp -rp examples AUTHORS %buildroot%_defaultdocdir/%name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jcuber-doc -f %{oreon_filedir}/jcuber-doc.list

%changelog

%autochangelog
