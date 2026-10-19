%global source0_hash f4203a605a3c9c50acdcc6eef4a366b9fdd36d95edcd76bcbfede01107cb5fe6
%global debug_package %{nil}
%if 0%{?fedora} || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global java_version 21
%else
%global java_version 17
%endif
Summary:        Open Source implementation of JSR-56 better known as Java Web Start
Name:              icedtea-web
Version:           1.8.8
Release:        1%{?dist}
License:           GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Classpath-exception-2.0 AND LGPL-2.1-or-later AND Zlib
URL:               https://github.com/AdoptOpenJDK/IcedTea-Web
Source0:        https://github.com/AdoptOpenJDK/IcedTea-Web/archive/%{name}-%{version}/%{name}-%{version}.tar.gz#/icedtea-web-1.8.8.tar.gz
Patch0:            https://github.com/AdoptOpenJDK/IcedTea-Web/compare/icedtea-web-1.8.8...af67182516b22e8caa3ff2c3c81be9ef9233563f.patch#/icedtea-web-1.8.8-upstream-changes.patch
Patch1:        icedtea-web-1.8.8-remove-dunce.patch
Patch2:        icedtea-web-1.8.8-alt-java.patch
Patch3:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/907.patch#/icedtea-web-1.8.8-disable-pluginjar.patch
Patch4:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/899.patch#/icedtea-web-1.8.8-bash-completion.patch
Patch5:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/901.patch#/icedtea-web-1.8.8-untranslated-man-pages.patch
Patch6:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/908.patch#/icedtea-web-1.8.8-javadoc-param.patch
Patch7:        icedtea-web-1.8.8-java18-no-pack200.patch
Patch8:        icedtea-web-1.8.8-java21-jarindex.patch
Patch9:        icedtea-web-1.8.8-java21-autoconf.patch
Patch10:           https://github.com/AdoptOpenJDK/IcedTea-Web/pull/970.patch#/icedtea-web-1.8.8-javadoc-21.patch
Patch11:           https://github.com/AdoptOpenJDK/IcedTea-Web/pull/971.patch#/icedtea-web-1.8.8-java21-security-manager.patch
ExclusiveArch:     %{java_arches}
Recommends:        bash-completion
Requires:          java-%{java_version}-openjdk
Requires:          javapackages-tools
Requires:          tagsoup
Requires(post):    alternatives
Requires(post):    GConf2
Requires(postun):  alternatives
Requires(postun):  GConf2
Obsoletes:         javaws < 1.8.8-1
Provides:          javaws = %{version}-%{release}
Provides:          javaws%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  cargo
BuildRequires:  desktop-file-utils
BuildRequires:  java-21-openjdk-devel
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  javapackages-tools
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  tagsoup
BuildRequires:  zip
# /oreon:deps
%description
The IcedTea-Web project provides a free software implementation of Java
Web Start, originally based on the NetX, project.

IcedTea's NetX currently supports verification of signed jars, trusted
certificate storing, system certificate store checking, and provides the
services specified by the jnlp API.

In addition it also provides a full desktop integration, an offline run,
many extended security features, an own policy editor and much more.

%package javadoc
Summary:           API documentation for IcedTea-Web
Requires:          %{name} = %{version}-%{release}
BuildArch:         noarch
%description javadoc
This package contains the API documentation for the IcedTea-Web project.

%package devel
Summary:           Pure sources for debugging IcedTea-Web
Requires:          %{name} = %{version}-%{release}
BuildArch:         noarch
%description devel
This package contains the zipped sources of the IcedTea-Web project for
debugging IcedTea-Web.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IcedTea-Web-%{name}-%{version}
%patch -P0 -p1 -b .upstream-changes
%patch -P1 -p1 -b .remove-dunce
%patch -P2 -p1 -b .alt-java
%patch -P3 -p1 -b .disable-pluginjar
%patch -P4 -p1 -b .bash-completion
%patch -P5 -p1 -b .untranslated-man-pages
%patch -P6 -p1 -b .javadoc-param
%if 0%{?java_version} >= 17
%patch -P7 -p1 -b .java18-no-pack200
%endif
%if 0%{?java_version} >= 21
%patch -P8 -p1 -b .java21-jarindex
%patch -P9 -p1 -b .java21-autoconf
%patch -P10 -p1 -b .javadoc-21
%patch -P11 -p1 -b .java21-security-manager
%endif

# Remove applet support
rm -rf plugin netx/sun netx/net/sourceforge/jnlp/{NetxPanel,runtime/RhinoBasedPacEvaluator,util/WindowsDesktopEntry}.java

# Remove unused sources
rm -rf tests win-installer

%build

autoreconf --force --install
%configure \
  --with-pkgversion=fedora-%{release}-%{_arch} \
  --docdir=%{_datadir}/javadoc/%{name} \
  --with-jdk-home=%{_jvmdir}/java-%{java_version}-openjdk \
  --with-jre-home=%{_jvmdir}/jre-%{java_version}-openjdk \
  --program-suffix=.itweb \
  --disable-native-plugin \
  --disable-pluginjar \
  --with-itw-libs=DISTRIBUTION \
  --with-modularjdk-file=%{_sysconfdir}/java/%{name} \
  --enable-shell-launchers
%make_build
%install
%make_install
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop
install -D -p -m 0644 metadata/%{name}.metainfo.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml
install -D -p -m 0644 metadata/%{name}-javaws.appdata.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}-javaws.metainfo.xml
mkdir -p $RPM_BUILD_ROOT%{_javadir}/
ln -s ../%{name}/javaws.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -p -m 0644 metadata/%{name}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom
%mvn_artifact $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -p -m 0644 netx.build/lib/src.zip $RPM_BUILD_ROOT%{_datadir}/%{name}/javaws.src.zip
touch $RPM_BUILD_ROOT%{_bindir}/{javaws,itweb-settings,policyeditor}
rm -f $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/javaws
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml
%post

alternatives \
  --install %{_bindir}/javaws         javaws.%{_arch} %{_bindir}/javaws.itweb    %{java_version}0000 --family java-%{java_version}-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings itweb-settings  %{_bindir}/itweb-settings.itweb \
  --slave   %{_bindir}/policyeditor   policyeditor    %{_bindir}/policyeditor.itweb
alternatives \
  --install %{_bindir}/javaws         javaws.%{_arch} %{_bindir}/javaws.itweb.sh %{java_version}0000 --family java-%{java_version}-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings itweb-settings  %{_bindir}/itweb-settings.itweb.sh \
  --slave   %{_bindir}/policyeditor   policyeditor    %{_bindir}/policyeditor.itweb.sh
gconftool-2 --set /desktop/gnome/url-handlers/jnlp/command  --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlp/enabled  --type=bool true &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/command --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/enabled --type=bool true &> /dev/null || :
%postun

if [ $1 -eq 0 ]; then
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb.sh
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/command  &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/enabled  &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/command &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/enabled &> /dev/null || :
fi
exit 0
%files -f %{oreon_filedir}/main.list
%files -n icedtea-web-javadoc -f %{oreon_filedir}/icedtea-web-javadoc.list
%files -n icedtea-web-devel -f %{oreon_filedir}/icedtea-web-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.8-11
- Import
