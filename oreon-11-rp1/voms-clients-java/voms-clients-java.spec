%global source0_hash 37a1b0092f259027c93ccf38db218d64c94a23869160515a1f54d7bd1583f7b3
Name:		voms-clients-java
Version:	3.3.7
Release:        1%{?dist}
Summary:        Virtual Organization Membership Service Java clients
License:	Apache-2.0
URL:		https://github.com/italiangrid/voms-clients
Source0:        https://github.com/italiangrid/voms-clients/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch
Requires:	mvn(org.italiangrid:voms-api-java) >= 3.3.7
Requires:	(java-headless or java-21-headless or java-25-headless)
Suggests:	java-headless
Requires:	javapackages-tools
Requires(post):		%{_sbindir}/update-alternatives
Requires(preun):	%{_sbindir}/update-alternatives
Conflicts:	voms-clients < 2.0.12
Provides:	voms-clients = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  maven-local
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.italiangrid:voms-api-java)
# /oreon:deps
%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the Java version of the command line clients for VOMS:
voms-proxy-init, voms-proxy-destroy and voms-proxy-info.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n voms-clients-%{version}

# Remove maven-javadoc-plugin configuration
# We are not building the javadoc for this package
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Don't do assembly
%pom_remove_plugin :maven-assembly-plugin

# The asciidoctor plugin is not available in Fedora
# Run asciidoctor explicitly in the build section instead
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin

%build

%mvn_build -j
pushd man
for x in *.adoc ; do asciidoctor -b manpage $x ; done
popd
%install
%mvn_install
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/voms-proxy-init3 << EOF
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx32m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcutil bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInit "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-init3
cat > %{buildroot}%{_bindir}/voms-proxy-info3 << EOF
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx32m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcutil bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInfo "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-info3
cat > %{buildroot}%{_bindir}/voms-proxy-destroy3 << EOF
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx32m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcutil bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyDestroy "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-destroy3
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 man/voms-proxy-init.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-init3.1
install -p -m 644 man/voms-proxy-info.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-info3.1
install -p -m 644 man/voms-proxy-destroy.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-destroy3.1
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for b in voms-proxy-init voms-proxy-info voms-proxy-destroy; do
  ln -s %{_bindir}/${b}3 %{buildroot}%{_sysconfdir}/alternatives/${b}
  ln -s %{_sysconfdir}/alternatives/${b} %{buildroot}%{_bindir}/${b}
  ln -s %{_mandir}/man1/${b}3.1.gz %{buildroot}%{_sysconfdir}/alternatives/${b}.1.gz
  ln -s %{_sysconfdir}/alternatives/${b}.1.gz %{buildroot}%{_mandir}/man1/${b}.1.gz
done
mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 644 man/vomsdir.5 %{buildroot}%{_mandir}/man5/vomsdir.5
install -p -m 644 man/vomses.5 %{buildroot}%{_mandir}/man5/vomses.5
%oreon_autofiles main

%post

%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-init \
    voms-proxy-init %{_bindir}/voms-proxy-init3 90 \
    --slave %{_mandir}/man1/voms-proxy-init.1.gz voms-proxy-init-man \
    %{_mandir}/man1/voms-proxy-init3.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-info \
    voms-proxy-info %{_bindir}/voms-proxy-info3 90 \
    --slave %{_mandir}/man1/voms-proxy-info.1.gz voms-proxy-info-man \
    %{_mandir}/man1/voms-proxy-info3.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-destroy \
    voms-proxy-destroy %{_bindir}/voms-proxy-destroy3 90 \
    --slave %{_mandir}/man1/voms-proxy-destroy.1.gz voms-proxy-destroy-man \
    %{_mandir}/man1/voms-proxy-destroy3.1.gz
%preun

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove voms-proxy-init \
    %{_bindir}/voms-proxy-init3
    %{_sbindir}/update-alternatives --remove voms-proxy-info \
    %{_bindir}/voms-proxy-info3
    %{_sbindir}/update-alternatives --remove voms-proxy-destroy \
    %{_bindir}/voms-proxy-destroy3
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
