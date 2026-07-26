%global source0_hash b897b85fa3909fc03b2640d3895960e8071c5a97cc88834568bdf4ee6eb83e9d

# Copyright (c) 2015  Dave Love, University of Liverpool
# MIT licence, per Fedora policy

Name:           jcuber
Version:        4.9
Release:        4%{?dist}
Summary:        CUBE reader for Java
# tarviewer is ASL
License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/%(echo %version|awk -F. '{print $1 "." $2}')/dist/jcuber-%version.tar.gz
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  xerces-j2
BuildRequires: make
Requires:       java-25 jpackage-utils
Obsoletes:      cube-java <= 4.3.2-1
Provides:       cube-java = %version-%release
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

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
# As an alternative to patching configure.ac and then worrying about
# autoconf268 in EPEL6:
sed -i -e s/jCubeR/jcuber/ -e 's|/cube|/jcuber|' bin/jcuber-config
# nothing to parallelize
make

%check
make check

%install
make install install-html DESTDIR=%buildroot
cp -rp examples AUTHORS %buildroot%_defaultdocdir/%name

%files
%dir %_defaultdocdir/%name
%license COPYING
%_defaultdocdir/%name/AUTHORS
%_datadir/java/CubeReader.jar
# rpmlint complains, but I don't think they should be in a devel package --
# at least the file extension should be relevant at runtime.
%_bindir/jcuber-config*
%_datadir/jcuber
%exclude %_docdir/jcuber

%files doc
%_defaultdocdir/%name
%license COPYING

%changelog
%autochangelog
