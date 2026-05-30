%global source0_hash 2cb895fa0628141e83a2997d1b05ed39a5e104b0879f528ece8e077bf6b7bd4c

%bcond bootstrap 0

Name:           xmvn-generator
Version:        2.1.1
Release:        %autorelease
Summary:        RPM dependency generator for Java
License:        Apache-2.0
URL:            https://github.com/fedora-java/xmvn-generator
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:        https://github.com/fedora-java/xmvn-generator/releases/download/%{version}/xmvn-generator-%{version}.tar.zst

# https://github.com/fedora-java/xmvn-generator/pull/37
Patch:          0001-Add-commons-lang3-to-generator-classpath.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(io.kojan:dola-bsx-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
Requires:       dola-bsx
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0.2-9

%description
XMvn Generator is a dependency generator for RPM Package Manager
written in Java and Lua.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%mvn_file : %{name}

%build
%mvn_build -j -- -P\!quality

%install
%mvn_install
install -D -p -m 644 src/main/lua/xmvn-generator.lua %{buildroot}%{_rpmluadir}/xmvn-generator.lua
install -D -p -m 644 src/main/rpm/macros.xmvngen %{buildroot}%{_rpmmacrodir}/macros.xmvngen
install -D -p -m 644 src/main/rpm/macros.xmvngenhook %{buildroot}%{_sysconfdir}/rpm/macros.xmvngenhook
install -D -p -m 644 src/main/rpm/xmvngen.attr %{buildroot}%{_fileattrsdir}/xmvngen.attr
install -D -p -m 644 src/main/conf/xmvn-generator.conf %{buildroot}%{_javaconfdir}/dola/classworlds/90-xmvn-generator.conf

%files -f .mfiles
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%{_javaconfdir}/dola/classworlds/90-xmvn-generator.conf
%license LICENSE NOTICE
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-1
- Import
